from dash import Dash, html, dcc
import dash
from pathlib import Path
import flask

app = Dash(__name__, use_pages=True)

app.layout = html.Div([
	html.H1('Group 10:Drug Abuse Among Incarcerated People in the USA '),
	html.H5('List of Visualizations'),

    html.Div(
        [
            html.Div(
                dcc.Link(
                    f"{page['name']}", href=page["relative_path"]
                )
            )
            for page in dash.page_registry.values()
        ],
    ),
    html.Div([
    html.A("Visual_5", href="/get_report", target="_blank") # actually vis 4
]),

	dash.page_container
])
HERE = Path(__file__).parent

# app = dash.Dash()


@app.server.route("/get_report")
def get_report():
    return flask.send_from_directory(HERE, "circles.html")
if __name__ == '__main__':
	app.run_server(debug=True)