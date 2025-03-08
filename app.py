import streamlit as st

#Functionality
def length_converter(from_unit,to_unit,value):
    units = {
        "Metre": 1,
        "Kilometre": 1000,
        "Foot": 0.3048,
        "Mile": 1609.34,
    }
    result = value * units[from_unit]/units[to_unit]
    return result

def temperature_converter(from_unit,to_unit,value):
    if from_unit == "Degree Celsius" and to_unit == "Fahrenheit":
        result = (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Degree Celsius":
        result = (value - 32) * 5/9
    else:
        result = value
    return result  

def mass_converter(from_unit,to_unit,value):
    units = {
        "Kilogram": 1,
        "Gram": 0.001,
        "Pound": 0.453592,
        "Ounce": 0.0283495,
    }
    result = value * units[from_unit]/units[to_unit]
    return result

def pressure_converter(from_unit,to_unit,value):
    units = {
        "Pascal": 1,
        "HectoPascal": 100,
        "KiloPascal": 1000,
        "Bar": 100000,
    }
    result = value * units[from_unit]/units[to_unit]
    return result

st.title("Unit Converter")
# Select Category
category = st.selectbox("Select Category",["Length","Temperature","Mass","Pressure"]) #For Dropdown List

if category == "Length":
    from_unit = st.selectbox("From",["Metre","Kilometre","Foot","Mile"])
    to_unit = st.selectbox("To",["Metre","Kilometre","Foot","Mile"])
    value = st.number_input("Enter Value")
    if st.button("Convert"):
        result = length_converter(from_unit,to_unit,value)
        st.success(f"{value} {from_unit} = {result} {to_unit}")

elif category == "Temperature":
    from_unit = st.selectbox("From",["Fahrenheit","Degree Celsius"])
    to_unit = st.selectbox("To",["Fahrenheit","Degree Celsius"])
    value = st.number_input("Enter Value")
    if st.button("Convert"):
        result = temperature_converter(from_unit,to_unit,value)
        st.success(f"{value} {from_unit} = {result} {to_unit}")

elif category == "Mass":
    from_unit = st.selectbox("From",["Kilogram","Gram","Pound","Ounce"])
    to_unit = st.selectbox("To",["Kilogram","Gram","Pound","Ounce"])
    value = st.number_input("Enter Value")
    if st.button("Convert"):
        result = mass_converter(from_unit,to_unit,value)
        st.success(f"{value} {from_unit} = {result} {to_unit}")

elif category == "Pressure":
    from_unit = st.selectbox("From",["Pascal","HectoPascal","KiloPascal","Bar"])
    to_unit = st.selectbox("To",["Pascal","HectoPascal","KiloPascal","Bar"])
    value = st.number_input("Enter Value")
    if st.button("Convert"):
        result = pressure_converter(from_unit,to_unit,value)
        st.success(f"{value} {from_unit} = {result} {to_unit}")