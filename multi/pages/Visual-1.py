

import dash
from dash import html, dcc, callback, Input, Output
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

import warnings
warnings.filterwarnings("ignore")

dash.register_page(__name__)

df_2 = pd.read_csv("../extracted_data_vis1.csv")
layout = html.Div([
    html.H4('Distribution of Different Types of Drugs Among Prisoners Using a Selected Criteria'),
    html.P("Select a criteria to view:"),
    dcc.RadioItems(
        id='candidate', 
        options=["time_of_use", "Age_group", "Sex", "Race"],
        value="time_of_use",
        inline=True
    ),
    dcc.Graph(id="graph"),
])
text_dict = {'Alcohol_percentage': 'Alcohol',
 'Marijuana_percentage': 'Marijuana',
 'Heroin_percentage': 'Heroin',
 'Cocaine_percentage': 'Cocaine',
 "count": "num_prisoners"}

@callback(
    Output("graph", "figure"), 
    Input("candidate", "value"))
def display_choropleth(candidate):
    fig = px.sunburst(df_2, path=["num_drugs", candidate],
                      color_discrete_sequence=px.colors.qualitative.D3,
                      height=800, width=900
)   
    # fig.update_layout(
    #     margin = dict(t=0, l=0, r=10, b=0),

    # )

    # fig.show()

    return fig