import dash
from dash import html, dcc

dash.register_page(__name__, path='/')

layout = html.Div(children=[

    html.Div(children='''
       Select links above to view the visualizations
    '''),

])