# Choropleth Map with Plotly
*Credits to : Tanisha Patil*
## [LINK](https://tanishapatil1234.github.io/choropleth/)
<img width="1179" alt="image" src="https://github.com/tanishapatil1234/choropleth/assets/111611921/cfc7b350-7539-49a9-a371-394d0dd15b29">



This project demonstrates how to create a choropleth map using Plotly in Python. A choropleth map is a thematic map where areas are shaded or patterned in proportion to the value of a variable being represented.

## Features

- Utilizes Plotly library to create interactive choropleth maps.
- Loads GeoJSON data for mapping county boundaries.
- Retrieves unemployment data by county from an external CSV file.
- Personalizes the map by adjusting color scale, range, title, and hover information.
- Saves the generated map as an HTML file for easy sharing and embedding.

## Getting Started

1. Clone the repository to your local machine:

`git clone https://github.com/your_username/choropleth-map.git`


2. Install the required dependencies using pip:

`pip install pandas plotly`


3. Run the Python script to generate the choropleth map:

`python choropleth.py`


4. Open the generated `index.html` file in a web browser to view the interactive map.

## Customization

You can customize the choropleth map by modifying the parameters in the Python script:

- Adjust the color scale, range, and legend by modifying the `color_continuous_scale`, `range_color`, and `coloraxis_colorbar` parameters.
- Change the title of the map using the `title` parameter.
- Modify hover information by adjusting the `hover_data` parameter.

## Resources

- [Plotly Documentation](https://plotly.com/python/)
- [GeoJSON County Data](https://github.com/plotly/datasets/blob/master/geojson-counties-fips.json)
- [Unemployment Data](https://github.com/plotly/datasets/blob/master/fips-unemp-16.csv)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
