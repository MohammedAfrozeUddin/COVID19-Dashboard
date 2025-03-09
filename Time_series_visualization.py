import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv(r"C:\Coding\Data Science\Advance VIsualization\covid19_high_value_data.csv")

# Print column names for debugging
print(df.columns)

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Correct column name
fig = px.line(df, x="Date", y="Total Cases", color="Country",
              title="COVID-19 Cases Over Time",
              labels={"Total Cases": "Number of Cases", "Date": "Date"},
              template="plotly_dark")

fig.update_traces(mode="lines+markers", marker=dict(size=4))

fig.show()
