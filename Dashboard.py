import streamlit as st
import pandas as pd
import random

# Set the page title
st.set_page_config(page_title="Options Terminal", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        .big-font {
            font-size: 30px !important;
            font-weight: bold;
        }
        .header {
            color: #ffffff;
            font-size: 25px;
        }
        .data-card {
            background-color: #000000;
            color: #ffffff;
            padding: 10px;
            border-radius: 10px;
            border: 2px solid white;
        }
        .table-container {
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("Options Terminal")

# Create a row with 5 columns for indices (Nifty, Bank Nifty, Fin Nifty, Sensex)
col1, col2, col3, col4, col5 = st.columns(5)

# Display real-time data for each index in respective columns
with col1:
    st.markdown("<h3 class='header'>Nifty</h3>", unsafe_allow_html=True)
    st.markdown(f"<div class='data-card'>LTP: {random.randint(17000, 18000)}<br>Change (Points): {random.randint(-100, 100)}<br>Change (%): {random.uniform(-2, 2):.2f}%<br>Prev Close: {random.randint(16900, 17900)}</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<h3 class='header'>Bank Nifty</h3>", unsafe_allow_html=True)
    st.markdown(f"<div class='data-card'>LTP: {random.randint(38000, 40000)}<br>Change (Points): {random.randint(-200, 200)}<br>Change (%): {random.uniform(-2, 2):.2f}%<br>Prev Close: {random.randint(37500, 39500)}</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<h3 class='header'>Fin Nifty</h3>", unsafe_allow_html=True)
    st.markdown(f"<div class='data-card'>LTP: {random.randint(17000, 18000)}<br>Change (Points): {random.randint(-100, 100)}<br>Change (%): {random.uniform(-2, 2):.2f}%<br>Prev Close: {random.randint(16900, 17900)}</div>", unsafe_allow_html=True)

with col4:
    st.markdown("<h3 class='header'>Sensex</h3>", unsafe_allow_html=True)
    st.markdown(f"<div class='data-card'>LTP: {random.randint(58000, 60000)}<br>Change (Points): {random.randint(-500, 500)}<br>Change (%): {random.uniform(-2, 2):.2f}%<br>Prev Close: {random.randint(57500, 59500)}</div>", unsafe_allow_html=True)


# Add Sensex data to each column with a button in each cell of col5
for i, col in enumerate([col1, col2, col3, col4, col5]):
    with col:
        if i < 4:
            # Displaying data for indices
            st.markdown(f"<h3 class='header'>Index {i + 1}</h3>", unsafe_allow_html=True)
            st.markdown(f"<div class='data-card'>LTP: {random.randint(58000, 60000)}<br>Change (Points): {random.randint(-500, 500)}<br>Change (%): {random.uniform(-2, 2):.2f}%<br>Prev Close: {random.randint(57500, 59500)}</div>", unsafe_allow_html=True)
        else:
            # Button in the last column
            st.markdown("<h3 class='header'>Action</h3>", unsafe_allow_html=True)
            if st.button(f"Execute {i + 1}"):
                st.write(f"You clicked 'Execute {i + 1}' button!")


# Dummy Data for the strategy table
data = {
    "Sl. No.": [1, 2, 3, 4],
    "Instruments": ["NIFTY24D1925000CE", "NIFTY24DEC25000CE", "BANKNIFTY24D40000CE", "BANKNIFTY24D42000CE"],
    "Net LTP": [random.uniform(20, 50), random.uniform(30, 60), random.uniform(100, 150), random.uniform(200, 250)],
    "Desired LTP": [random.uniform(25, 55), random.uniform(35, 65), random.uniform(110, 160), random.uniform(210, 260)],
    "Desired Qty": [25, 30, 20, 25],
    "Order Status": ["Waiting", "Success", "Partial", "Waiting"],
    "PNL": [random.uniform(-500, 500), random.uniform(-500, 500), random.uniform(-1000, 1000), random.uniform(-200, 200)],
}

# Create DataFrame for the table
df = pd.DataFrame(data)

# Show the table with headers and styling
st.subheader("Strategy Execution")

# Table container with custom margin-top
with st.container():
    st.markdown("<div class='table-container'>", unsafe_allow_html=True)
    
    # Display the dataframe with the serial number column
    df = df.rename(columns={"Sl. No.": "Sl. No."})
    st.write(df)

    st.markdown("</div>", unsafe_allow_html=True)
