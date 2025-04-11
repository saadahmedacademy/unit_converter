import streamlit as st

st.title('Unit Converter App')
st.markdown('### Convert weight, length and time instantly')
st.write("Welcome, select the category, set the value, and get the result instantly")

category = st.selectbox('Select the category', ["weight", "length", "time"])
value = st.number_input("Enter the value", 0.0)

unit = None
if category == "length":
    unit = st.selectbox("Select the unit", ["Kilometers to miles", "Miles to kilometers"])
elif category == "weight":
    unit = st.selectbox("Select the unit", ["Kilograms to pounds", "Pounds to kilograms"])
elif category == "time":
    unit = st.selectbox("Select the unit", [
        "Seconds to minutes", "Minutes to seconds", "Hours to minutes",
        "Minutes to hours", "Hours to days", "Days to hours"
    ])

def converter(category, value, unit):
    if category == "weight":
        if unit == "Kilograms to pounds":
            return value * 2.20462
        elif unit == "Pounds to kilograms":
            return value / 2.20462

    elif category == "length":
        if unit == "Kilometers to miles":
            return value * 0.621371
        elif unit == "Miles to kilometers":
            return value / 0.621371

    elif category == "time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24

    return 0

if st.button("Convert"):
    result = converter(category, value, unit)
    st.success(f"The result is {result:.2f}")
