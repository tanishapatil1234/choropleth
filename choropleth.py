from urllib.request import urlopen
import json
import pandas as pd
import plotly.express as px

# Load GeoJSON data
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

# Load unemployment data
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                   dtype={"fips": str})

# Create choropleth map with personalized adjustments
fig = px.choropleth(df, geojson=counties, locations='fips', color='unemp',
                    color_continuous_scale="Blues",  # Change color scale
                    range_color=(0, 10),  # Adjust range
                    scope="usa",
                    labels={'unemp':'Unemployment Rate (%)'},  # Adjust label
                    title='Unemployment Rate by County',  # Add title
                    hover_data={'fips': False, 'unemp': True},  # Add hover data
                    )

# Update layout with personalized adjustments
fig.update_layout(
    margin={"r":0,"t":40,"l":0,"b":0},  # Adjust margins
    coloraxis_colorbar=dict(title='Unemployment Rate (%)'),  # Adjust colorbar title
)

# Save the figure as HTML file
fig.write_html("index.html")
