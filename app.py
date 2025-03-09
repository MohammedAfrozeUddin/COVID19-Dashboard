import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("COVID-19 Dashboard 📊")

# Load Data
df = pd.read_csv("covid19_high_value_data.csv")

# Show Data
st.subheader("Raw Data")
st.write(df.head())

# Visualizations
st.subheader("COVID-19 Cases Over Time")
fig, ax = plt.subplots(figsize=(10, 5))
df['date'] = pd.to_datetime(df['Date'])
df = df.sort_values('date')
sns.lineplot(data=df, x="date", y="Daily Cases", hue="Country", ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# User Input - Country Selection
st.sidebar.title("Filter Data")
selected_country = st.sidebar.selectbox("Select a Country", df["Country"].unique())

# Filtered Data
st.subheader(f"COVID-19 Data for {selected_country}")
st.write(df[df["Country"] == selected_country])
