

import dash
from dash import html, dcc, callback, Input, Output
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import json
from dash import Dash, dcc, html, Input, Output
import warnings
warnings.filterwarnings("ignore")
with open('.././gz_2010_us_040_00_500k.json') as f:
   geo_data = json.load(f)

dash.register_page(__name__)

merged_df = pd.read_csv("../extracted_data_vis2.csv")

layout = html.Div([
    html.H4('Percentage of Prisoners abusing drug among all prisoners by State'),
    html.P("Select a drug type:"),
    dcc.RadioItems(
        id='candidate_1', 
        options=["Alcohol_percentage", "Marijuana_percentage", "Heroin_percentage","Cocaine_percentage"],
        value="Alcohol_percentage",
        inline=True
    ),
    dcc.Graph(id="graph_1"),
])

candidate_dict = {'Alcohol_percentage': 'Alcohol',
 'Marijuana_percentage': 'Marijuana',
 'Heroin_percentage': 'Heroin',
 'Cocaine_percentage': 'Cocaine'}

@callback(
    Output("graph_1", "figure"), 
    Input("candidate_1", "value"))
def display_choropleth(candidate):
    df = px.data.election() # replace with your own data source
    geojson = px.data.election_geojson()

    fig = px.choropleth_mapbox(merged_df, geojson=geo_data, color=candidate,
                           locations='State', featureidkey="properties.NAME",
                           hover_data= {candidate:True, 'total_prisoners':True, candidate_dict[candidate]:True, "State":False},
                           hover_name="State",
                           center= {"lat":39.8283, "lon" : -98.5795}, zoom= 3,
                            color_continuous_scale = 'blues',
                            labels={'Alcohol': 'Prisoners using Alcohol',
                                    'Marijuana': 'Prisoners using Marijuana',
                                    'Heroin': 'Prisoners using Heroin',
                                    'Cocaine': 'Prisoners using Cocaine',
                                    'Alcohol_percentage': 'Alcohol use %',
                                    'Marijuana_percentage': 'Marijuana use %',
                                    'Heroin_percentage': 'Heroin use %',
                                    'Cocaine_percentage': 'Cocaine use %'},
                            
                            width=1000, height=800,

                           mapbox_style="carto-positron")

    return fig
