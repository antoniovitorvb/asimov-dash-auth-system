from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np

from app import *
from pages import login, register, data

navLink = {
    '/': login,
    '/login': login,
    '/register': register,
    '/data': data
}

app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
            dcc.Location(id='base-url', refresh=False),

            dcc.Store(id='login-state', data = ''),
            dcc.Store(id='register-state', data = ''),

            html.Div(
                id='page-content',
                style={'height':'100vh',
                       'display': 'flex',
                       'justify-content':'center'}
            ),
        ]),
    ])
], fluid = True)

# ========== CALLBACKS ========== #
@app.callback(
    Output(component_id='page-content', component_property='children'),
    Input(component_id='base-url', component_property='pathname')
)
def render_content(pathname):
    # if (pathname == '/' or pathname == '/login'):
    #     return login.render_layout()
    return navLink[pathname].render_layout('Antonio')

if __name__ == '__main__':
    app.run_server(port=5000, debug=True)