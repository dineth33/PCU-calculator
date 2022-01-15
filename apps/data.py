import streamlit as st
import pandas as pd


@st.cache
def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv().encode('utf-8')

def app():

    st.write("Two data types as vehicle speed and area are required for the PCU calculation according to the utilized method"
             " Both data are required to be inserted to the calculator by `csv file` format. Please adhere to the given data format "
             "which can be downloaded from below. Note that other formats will not be accepted by the calculator")

    st.subheader('Vehicle Speed data')

    st.write("Speeds of selected vehicle types is required to determine PCU values from the selected method"
             " It is encouraged to collect the vehicle speed data (space mean speed) covering the all traffic states within a day "
             "for the selected road section to PCU estimation."
             "Temporal sampling as 5 mins for evey 15 mins for at least 12 hours (6:00 a.m. - 6:00 p.m.) is recommended to"
             " general transportation studies"
             " For the accuracy of the results to be obtained, it is encouraged to use a comprehensive set of vehicle speed data")

    speed_dataframe = pd.read_csv("Speed_data_format.csv")

    st.dataframe(speed_dataframe.head())

    csv = convert_df(speed_dataframe)
    st.download_button(label="Download speed data format", data=csv, file_name='speed_data_format.csv', mime='text/csv')

    st.subheader('Vehicle area data')

    st.write("Projected areas of vehicles is also required as a input for the pcu calculation, The given areas should "
             "be common to the available general vehicle models for the considered road section. Values should be given "
             "in `square meters`. Ensure that the areas are given to all the considered vehicle types")

    speed_dataframe = pd.read_csv("Areas_PCU.csv")

    st.dataframe(speed_dataframe.head())

    csv = convert_df(speed_dataframe)
    st.download_button(label="Download area data format", data=csv, file_name='area_data_format.csv',  mime='text/csv')
