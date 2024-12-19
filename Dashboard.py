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
            color: #2e6b8a;
            font-size: 25px;
        }
        .data-card {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        .table-container {
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("Options Terminal")

# Create a row with 4 columns for indices (Nifty, Bank Nifty, Fin Nifty, Sensex)
col1, col2, col3, col4 = st.columns(4)

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

# Dummy Data for the strategy table
data = {
    "Instruments": ["NIFTY24D1925000CE", "NIFTY24DEC25000CE", "BANKNIFTY24D40000CE", "BANKNIFTY24D42000CE"],
    "Net LTP": [random.uniform(20, 50), random.uniform(30, 60), random.uniform(100, 150), random.uniform(200, 250)],
    "Desired LTP": [random.uniform(25, 55), random.uniform(35, 65), random.uniform(110, 160), random.uniform(210, 260)],
    "Desired Qty": [25, 30, 20, 25],
    "Order Status": ["Waiting", "Success", "Partial", "Waiting"],
    "PNL": [random.uniform(-500, 500), random.uniform(-500, 500), random.uniform(-1000, 1000), random.uniform(-200, 200)],
}

# Create DataFrame for the table
df = pd.DataFrame(data)

# Show the table with headers and styles
st.subheader("Strategy Execution")

# Table container with custom margin-top
with st.container():
    st.markdown("<div class='table-container'>", unsafe_allow_html=True)
    
    # Display the dataframe with formatting
    st.dataframe(df, use_container_width=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Add Execution Button (dynamic button per row)
for i in range(len(df)):
    if df.at[i, 'Order Status'] == "Waiting":
        if st.button(f"Execute {df.at[i, 'Instruments']}", key=f"exec_{i}"):
            # Update order status (in actual, logic would go here)
            df.at[i, 'Order Status'] = "Success"
            st.success(f"Order for {df.at[i, 'Instruments']} executed!")

st.write(df)  # To show updated dataframe after order execution
