import streamlit as st

st.set_page_config(page_title="Universal Unit Converter", page_icon="🔁")
st.title("🔁 Universal Unit Converter")
st.markdown("Convert Length, Weight, Time, Temperature, Volume & Currency")

# Category selection
category = st.selectbox("Select Category:", ["Length", "Weight", "Time", "Temperature", "Volume", "Currency"])

# LENGTH
if category == "Length":
    units = {
        "Metres": 1,
        "Kilometres": 1000,
        "Centimetres": 0.01,
        "Millimetres": 0.001,
        "Feet": 0.3048,
        "Inches": 0.0254
    }

# WEIGHT
elif category == "Weight":
    units = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Milligrams": 0.000001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495
    }

# TIME
elif category == "Time":
    units = {
        "Seconds": 1,
        "Minutes": 60,
        "Hours": 3600,
        "Days": 86400
    }

# TEMPERATURE
elif category == "Temperature":
    temp_units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From Unit", temp_units)
    to_unit = st.selectbox("To Unit", temp_units)
    value = st.number_input("Enter temperature:", format="%.2f")

    def convert_temp(val, from_u, to_u):
        if from_u == to_u:
            return val
        if from_u == "Celsius":
            return val * 9/5 + 32 if to_u == "Fahrenheit" else val + 273.15
        if from_u == "Fahrenheit":
            return (val - 32) * 5/9 if to_u == "Celsius" else (val - 32) * 5/9 + 273.15
        if from_u == "Kelvin":
            return val - 273.15 if to_u == "Celsius" else (val - 273.15) * 9/5 + 32

    result = convert_temp(value, from_unit, to_unit)
    st.success(f"{value:.2f} {from_unit} = {result:.2f} {to_unit}")

# VOLUME
elif category == "Volume":
    units = {
        "Litres": 1,
        "Millilitres": 0.001,
        "Cubic Metres": 1000,
        "Cups": 0.24,
        "Gallons": 3.78541
    }

# CURRENCY
elif category == "Currency":
    # Static rates (example, INR base)
    units = {
        "INR": 1,
        "USD": 0.012,
        "EUR": 0.011,
        "GBP": 0.0096,
        "JPY": 1.76
    }

# COMMON CONVERTER (for non-temperature)
if category not in ["Temperature"]:
    from_unit = st.selectbox("From Unit", list(units.keys()))
    to_unit = st.selectbox("To Unit", list(units.keys()))
    value = st.number_input(f"Enter value in {from_unit.lower()}:", format="%.4f")

    result = value * units[from_unit] / units[to_unit]
    st.success(f"{value:.4f} {from_unit} = {result:.4f} {to_unit}")



