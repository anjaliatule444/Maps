import pandas as pd
import geopandas as gpd
import plotly.express as px

def Canedian_Election():
    data=pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/election.csv')
    data_geojson=gpd.read_file('https://raw.githubusercontent.com/plotly/datasets/master/election.geojson')
    map=px.choropleth_mapbox(data,
                             geojson=data_geojson,
                             color='winner',
                             locations='district',
                             featureidkey='properties.district',
                             opacity=0.3,
                             mapbox_style='carto-positron',
                             zoom=8.5,
                             center={'lat':45.5517,'lon':-73.7073},
                             color_discrete_map={
                                 'Beregon':'Blue',
                                 'Joly':'magenta',
                                 'Coderre':'Yellow'
                             }
    )
    map.show()