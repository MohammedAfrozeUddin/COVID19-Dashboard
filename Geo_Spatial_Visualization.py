import plotly.express as px
import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Coding\Data Science\Advance VIsualization\covid19_high_value_data.csv")

# Print column names for debugging
print(df.columns)

# Create a choropleth map using the correct column name
fig = px.choropleth(df,
                    locations="Country",
                    locationmode="country names",
                    color="Total Cases",  # Fixed column name
                    hover_name="Country",
                    color_continuous_scale="Reds",
                    title="Global COVID-19 Case Distribution")

fig.show()
