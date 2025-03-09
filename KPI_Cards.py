import dash
from dash import html, dcc
import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Coding\Data Science\Advance VIsualization\covid19_high_value_data.csv")

# Print column names to check available names
print("Columns in CSV:", df.columns)

# Ensure correct column names are used
total_cases = df["Total Cases"].sum()
total_deaths = df["Total Deaths"].sum()
total_recovered = df["Total Recovered"].sum()
recovery_rate = round((total_recovered / total_cases) * 100, 2)

# Initialize Dash App
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("COVID-19 Dashboard", style={"textAlign": "center"}),

    html.Div(children=[
        html.Div([
            html.H3("Total Cases"),
            html.P(f"{total_cases:,}", style={"color": "red", "fontSize": "30px"})
        ], style={"width": "30%", "display": "inline-block", "textAlign": "center"}),

        html.Div([
            html.H3("Total Deaths"),
            html.P(f"{total_deaths:,}", style={"color": "black", "fontSize": "30px"})
        ], style={"width": "30%", "display": "inline-block", "textAlign": "center"}),

        html.Div([
            html.H3("Recovery Rate"),
            html.P(f"{recovery_rate}%", style={"color": "green", "fontSize": "30px"})
        ], style={"width": "30%", "display": "inline-block", "textAlign": "center"})
    ])
])

if __name__ == "__main__":
    app.run_server(debug=True)
