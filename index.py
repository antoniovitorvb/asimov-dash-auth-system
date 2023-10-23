from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np

from app import *
from pages import login

app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
            dcc.Location(id='base-url', refresh=False),

            html.Div(id='page-content', style={'height':'100vh'}),
        ]),
    ])
], fluid = True)

# ========== CALLBACKS ========== #
@app.callback(
    Output(component_id='page-content', component_property='children'),
    Input(component_id='base-url', component_property='pathname')
)
def render_content(pathname):
    if (pathname == '/' or pathname == '/login'):
        return login.render_layout()


if __name__ == '__main__':
    app.run_server(port=8050, debug=True)