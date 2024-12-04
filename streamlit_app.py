from google.colab import drive

drive.mount('/content/drive')
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Energy Prediction App",
    page_icon="⚡",
    layout="wide"
)

# Load dataset
def load_data():
    data = pd.read_csv("FullSet.csv")  # Ensure the CSV file is in the correct directory
    return data.dropna()

data = load_data()

# Title and Description
st.title("Energy Prediction App Group 2⚡")
st.markdown("We are the best coders in this class")

# Create columns for layout
row1_col1, row1_col2, row1_col3 = st.columns([1, 1, 1])

# Header for Country Section
st.header("Select a Country")
if 'country' in data.columns:  # Ensure the 'country' column exists in the dataset
    # Create a dropdown with unique countries
    country = row1_col1.selectbox("Select a Country", sorted(data['country'].unique()))
    
    # Display the selected country
    st.write(f"You selected: {country}")
    
    # Filter and display country-specific data
    st.subheader(f"Data for {country}")
    country_data = data[data['country'] == country]
    st.write(country_data)
    
    # Plot a bar chart for Energy Consumption over years
    if 'year' in data.columns and 'EnergyConsumption' in data.columns:
        st.subheader(f"Energy Consumption in {country} Over Time")
        st.bar_chart(country_data.set_index('year')['EnergyConsumption'])
    else:
        st.write("The dataset does not have the required 'year' or 'EnergyConsumption' columns.")
else:
    st.write("The dataset does not have a 'country' column.")

# Allow variable selection in another column
names = data.columns
variable = row1_col3.selectbox("Select Variable to Compare", names)
row1_col3.markdown(f"You selected: {variable}")
