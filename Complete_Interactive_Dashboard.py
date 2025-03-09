import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv(r"C:\Coding\Data Science\Advance VIsualization\covid19_high_value_data.csv")

# Initialize Dash App
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("COVID-19 Interactive Dashboard", style={"textAlign": "center"}),

    # Dropdown to select country
    dcc.Dropdown(
        id="country_dropdown",
        options=[{"label": country, "value": country} for country in df["Country"].unique()],
        value="USA",
        clearable=False
    ),

    # Time-series plot
    dcc.Graph(id="cases_chart"),

    # Choropleth map
    dcc.Graph(id="world_map", figure=px.choropleth(
        df, locations="Country", locationmode="country names",
        color="Total Cases",  # Fixed the column name
        hover_name="Country",
        color_continuous_scale="Reds",
        title="Global COVID-19 Case Distribution"
    )),
])

# Callback to update the graph
@app.callback(
    dash.dependencies.Output("cases_chart", "figure"),
    [dash.dependencies.Input("country_dropdown", "value")]
)
def update_chart(selected_country):
    filtered_df = df[df["Country"] == selected_country]
    fig = px.line(filtered_df, x="Date", y="Total Cases", title=f"COVID-19 Cases in {selected_country}")
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
