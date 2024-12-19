import streamlit as st
import random
import pandas as pd

# Sample Data
data = {
    "Sl. No.": [1, 2, 3, 4],
    "Instruments": ["NIFTY24D1925000CE", "NIFTY24DEC25000CE", "BANKNIFTY24D40000CE", "BANKNIFTY24D42000CE"],
    "Net LTP": [random.uniform(20, 50), random.uniform(30, 60), random.uniform(100, 150), random.uniform(200, 250)],
    "Desired LTP": [random.uniform(25, 55), random.uniform(35, 65), random.uniform(110, 160), random.uniform(210, 260)],
    "Desired Qty": [25, 30, 20, 25],
    "Order Status": ["Waiting", "Success", "Partial", "Waiting"],
    "PNL": [random.uniform(-500, 500), random.uniform(-500, 500), random.uniform(-1000, 1000), random.uniform(-200, 200)],
}

# Create DataFrame from data
df = pd.DataFrame(data)

# Title
st.title("Options Terminal")

# Display the table with buttons
st.write("### Strategy Data")
for index, row in df.iterrows():
    # Display the row data
    col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 2, 1])
    
    with col1:
        st.write(row["Sl. No."])
    with col2:
        st.write(row["Instruments"])
    with col3:
        st.write(f"{row['Net LTP']:.2f}")
    with col4:
        st.write(f"{row['Desired LTP']:.2f}")
    with col5:
        # Add an "Execute" button for each row
        if st.button(f"Execute {row['Sl. No.']}"):
            st.write(f"You clicked the 'Execute {row['Sl. No.']}' button for instrument {row['Instruments']}.")

