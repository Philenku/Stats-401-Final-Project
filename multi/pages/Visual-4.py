import dash
from dash import html, dcc, callback, Input, Output
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

from pathlib import Path
import flask


dash.register_page(__name__)
layout = html.Div([
    html.A("", href="/get_report", target="_blank")
])
# # layout = html.Div( 
# # html.A(href="/get_report", target="_blank"))

HERE = Path(__file__).parent

app = dash.Dash()


@app.server.route("/get_report")
def get_report():
    return flask.send_from_directory(HERE, "circles.html")

# # import os

# # STATIC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

# # server = flask(__name__)
# # app = dash.Dash(name = __name__, server = server)

# # app.layout = html.Div( 
# #    html.Img(src='/static/your_img.jpeg') 
# # )

# # @app.server.route('/static/<resource>')
# # def serve_static(resource):


# #     return flask.send_from_directory(STATIC_PATH, resource)