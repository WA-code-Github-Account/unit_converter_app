import streamlit as st

# 🎨 Streamlit App Title
st.title("🔄 Advanced Unit Converter")
st.write("Convert multiple units instantly!")

# 📌 Conversion Options
options = {
    "Length": ["Meters to Centimeters", "Centimeters to Meters", "Kilometers to Miles", "Miles to Kilometers", "Feet to Inches", "Inches to Feet"],
    "Temperature": ["Celsius to Fahrenheit", "Fahrenheit to Celsius"],
    "Weight": ["Kilograms to Pounds", "Pounds to Kilograms", "Grams to Kilograms", "Kilograms to Grams"],
    "Time": ["Minutes to Seconds", "Seconds to Minutes", "Hours to Minutes", "Minutes to Hours"],
    "Speed": ["Kilometers per Hour to Miles per Hour", "Miles per Hour to Kilometers per Hour"],
    "Data Storage": ["Megabytes to Gigabytes", "Gigabytes to Megabytes", "Terabytes to Gigabytes", "Gigabytes to Terabytes"]
}

# 🔽 Dropdown for Conversion Type
conversion_type = st.selectbox("Select conversion type:", list(options.keys()))

# 🔽 Dropdown for Specific Conversion
conversion_choice = st.selectbox("Select conversion:", options[conversion_type])

# 🔢 User Input
value = st.number_input("Enter value to convert:", min_value=0.0, format="%.2f")

# 🔄 Conversion Logic
def convert(conversion_choice, value):
    conversions = {
        "Meters to Centimeters": value * 100,
        "Centimeters to Meters": value / 100,
        "Kilometers to Miles": value * 0.621371,
        "Miles to Kilometers": value / 0.621371,
        "Feet to Inches": value * 12,
        "Inches to Feet": value / 12,
        "Celsius to Fahrenheit": (value * 9/5) + 32,
        "Fahrenheit to Celsius": (value - 32) * 5/9,
        "Kilograms to Pounds": value * 2.20462,
        "Pounds to Kilograms": value / 2.20462,
        "Grams to Kilograms": value / 1000,
        "Kilograms to Grams": value * 1000,
        "Minutes to Seconds": value * 60,
        "Seconds to Minutes": value / 60,
        "Hours to Minutes": value * 60,
        "Minutes to Hours": value / 60,
        "Kilometers per Hour to Miles per Hour": value * 0.621371,
        "Miles per Hour to Kilometers per Hour": value / 0.621371,
        "Megabytes to Gigabytes": value / 1024,
        "Gigabytes to Megabytes": value * 1024,
        "Terabytes to Gigabytes": value * 1024,
        "Gigabytes to Terabytes": value / 1024
    }
    return conversions.get(conversion_choice, "Invalid conversion")

# 🎯 Convert Button
if st.button("Convert"):
    result = convert(conversion_choice, value)
    st.success(f"Converted Value: {result:.4f}")

# 🎉 End of App
st.write("🚀 Made with ❤️ using Streamlit")