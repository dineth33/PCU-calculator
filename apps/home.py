import streamlit as st

def app():

    st.write('Passenger car unit (PCU) is an important attribute for traffic '
             'capacity analysis and other relevant applications such as level of service (LOS) measures, '
             'determination of saturation flow rate, signal design and coordination, and development of traffic flow models.')

    st.write('This web application calculates the PCU values using Chandras method, which is a popular method '
             'to estimate PCU values for midblock road sections, For further details, please refer the following')

    st.markdown("""
    * 1. S. Chandra, V. Kumar, P.K. Sikdar Dynamic PCU and estimation of capacity 
    of urban roads Indian Highw. Indian Road Congr., 23 (4) (1995), pp. 17-28*.
    [click here](https://trid.trb.org/view/451757)
    """)

    st.markdown("""
    * 2. Dhananjaya, D. D., Fernando, W. W. P. M. & Sivakumar, T. Passenger Car
    Units for different midblock sections in Sri Lanka under mixed traffic conditions.
    ENGINEER: Journal of the Institution of Engineers, Sri Lanka (under review)*
    """)

    st.write('**If you use this application, please be kind enough to cite these papers in your work**')

