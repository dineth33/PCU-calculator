import streamlit as st
from multiapp import MultiApp
from apps import home, data, model # import your app modules here

app = MultiApp()

# st.markdown("""
# # Multi-Page App
#
# This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
#
# """)
st.title('Passenger Car Unit (PCU) Calculator')

# Add all your application here
app.add_app("Description", home.app)
app.add_app("Standard Data Format", data.app)
app.add_app("Calculator", model.app)

# The main app
app.run()
