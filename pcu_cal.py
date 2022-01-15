import pandas as pd
import numpy as np
import streamlit as st

# pcu calculation function
def pcu_calculation(hourly_vehicle_speeds, car_speeds, area_values):
    # calculate the hourly PCU values.
    for idx, row in hourly_vehicle_speeds.iterrows():
        vehicle = row['Vehicle']
        hour = row['HOUR']
        car_speed = car_speeds[car_speeds['HOUR'] == hour]['Speed']
        vehicle_area = area_values.loc[vehicle]

        pcu_value = (car_speed / row['Speed']) * (area_values.loc[vehicle, 'Area'] / area_values.loc['Car', 'Area'])
        hourly_vehicle_speeds.loc[idx, 'PCU'] = pcu_value.values[0]

    hourly_pcu_values = hourly_vehicle_speeds

    # General PCU values and SE value.
    pcu_table = hourly_vehicle_speeds.groupby('Vehicle')['PCU'].agg(['mean', 'std'])
    pcu_table = pcu_table.reset_index()
    pcu_table.columns = ['Vehicle type', 'PCU Value', 'Standard Error']

    return hourly_pcu_values, pcu_table

@st.cache
def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv().encode('utf-8')

# streamlit app
st.title('Passenger Car Unit (PCU) Calculator')

# input speed values
st.subheader('Speed data')
speed_data = st.file_uploader(label='Please upload the Cleaned csv file for vehicle speed data')

# input area values
st.subheader('Area data')
area_data = st.file_uploader(label='Please upload the Cleaned txt/csv file for vehicle areas')

# read the uploaded speed_data
global speed_values
if speed_data is not None:
    try:
        speed_values = pd.read_csv(speed_data)

        speed_values.columns = speed_values.columns.str.replace(' ', '')

        # clean the empty spaces at the end of vehicle names
        for idx, row in speed_values.iterrows():
            if row['Vehicle'][-1] == ' ':
                speed_values.loc[idx, 'Vehicle'] = row['Vehicle'][:-1]

        if area_data is not None:
             try:
                area_values = pd.read_csv(area_data)

                area_values.columns = area_values.columns.str.replace(' ', '')

                # clean the empty spaces at the end of vehicle names
                for idx, row in area_values.iterrows():
                    if row['VehicleName'][-1] == ' ':

                        area_values.loc[idx, 'VehicleName'] = row['VehicleName'][:-1]

                area_values = area_values.set_index('VehicleName')

                hourly_vehicle_speeds = speed_values.groupby(['Vehicle', 'HOUR'])['Speed'].mean()
                hourly_vehicle_speeds = hourly_vehicle_speeds.reset_index()
                car_speeds = hourly_vehicle_speeds[hourly_vehicle_speeds['Vehicle'] == 'Car']

                hourly_pcu_values, pcu_table = pcu_calculation(hourly_vehicle_speeds, car_speeds, area_values)

                st.subheader('Calculated PCU values')

                # streamlit output the PCU results as a table.
                st.dataframe(pcu_table)

                # download option
                csv = convert_df(pcu_table)
                st.download_button(label="Download PCU values", data=csv, file_name='pcu_values.csv', mime='text/csv')

             except Exception as e:
                     print(e)

    except Exception as e:
        print(e)











