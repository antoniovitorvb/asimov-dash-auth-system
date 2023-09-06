import dash
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import numpy as np
import plotly.express as px

from app import *

def render_layout():
    login = dbc.Card([
        html.Legend('Login'),

        dbc.Input(id='user-login', placeholder='Username', type='text'),
        dbc.Input(id='pwd-login', placeholder='Password', type='text'),

        dbc.Button('Login', id='login-button'),
        html.Span('', style={"text-align": "center"}),

        html.Div([
            html.Label('Or', style={'margin-right':'5px'}),
            dcc.Link('Register', href='/register')
        ], style={'padding': '20px', 'justify-content':'center', 'display':'flex'})

    ], className='login_card')
    return login