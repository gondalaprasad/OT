import streamlit as st
import pandas as pd
import random

# Set the page title
st.title("Options Terminal")

# Create a row with 4 columns for indices (Nifty, Bank Nifty, Fin Nifty, Sensex)
col1, col2, col3, col4 = st.columns(4)

# Display real-time data for each index in respective columns
with col1:
    st.subheader("Nifty")
    st.write(f"LTP: {random.randint(17000, 18000)}")
    st.write(f"Change (Points): {random.randint(-100, 100)}")
    st.write(f"Change (%): {random.uniform(-2, 2):.2f}%")
    st.write(f"Prev Close: {random.randint(16900, 17900)}")

with col2:
    st.subheader("Bank Nifty")
    st.write(f"LTP: {random.randint(38000, 40000)}")
    st.write(f"Change (Points): {random.randint(-200, 200)}")
    st.write(f"Change (%): {random.uniform(-2, 2):.2f}%")
    st.write(f"Prev Close: {random.randint(37500, 39500)}")

with col3:
    st.subheader("Fin Nifty")
    st.write(f"LTP: {random.randint(17000, 18000)}")
    st.write(f"Change (Points): {random.randint(-100, 100)}")
    st.write(f"Change (%): {random.uniform(-2, 2):.2f}%")
    st.write(f"Prev Close: {random.randint(16900, 17900)}")

with col4:
    st.subheader("Sensex")
    st.write(f"LTP: {random.randint(58000, 60000)}")
    st.write(f"Change (Points): {random.randint(-500, 500)}")
    st.write(f"Change (%): {random.uniform(-2, 2):.2f}%")
    st.write(f"Prev Close: {random.randint(57500, 59500)}")

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

# Show the table with headers
st.subheader("Strategy Execution")
st.write("List of strategies and their execution details:")

# Add the "Execution" button for each row in the table
def execution_button(row):
    if row['Order Status'] == "Waiting":
        if st.button(f"Execute {row['Instruments']}"):
            # Logic to execute the order would go here (for now, it just changes the status)
            st.success(f"Order for {row['Instruments']} executed!")
            return "Success"
    return row['Order Status']

# Apply execution button to each row
df['Order Status'] = df.apply(execution_button, axis=1)

# Show the updated DataFrame with Order Status changes
st.dataframe(df)
