import dash
from dash import Dash, html, dcc, Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from werkzeug.security import generate_password_hash

from app import *

def render_layout(username = None):
    register = dbc.Card([
        html.Legend('Register'),

        dbc.Input(id='user-register', placeholder='Username', type='text'),
        dbc.Input(id='pwd-register', placeholder='Password', type='text'),
        dbc.Input(id='email-register', placeholder='E-mail', type='text'),

        dbc.Button('Register!', id='register-button'),
        html.Span('', style={"text-align": "center"}),

        html.Div([
            html.Label('Or', style={'margin-right':'5px'}),
            dcc.Link('Login', href='/login')
        ], style={'padding': '20px', 'justify-content':'center', 'display':'flex'})

    ], className='login_card')
    return register

# ========== CALLBACKS ========== #
import pandas as pd

@app.callback(
    Output(component_id='register-state', component_property='data'),

    Input(component_id='register-button', component_property='n_clicks'),

    [State(component_id='user-register', component_property='value'),
     State(component_id='pwd-register', component_property='value'),
     State(component_id='email-register', component_property='value')]
)
def registering(n_clicks, username, password, email):
    if n_clicks == None:
        print('startup')
        raise PreventUpdate
    
    print(n_clicks)

    if all([username, password, email]): # All elements in the list are NOT None!
        hashed_pwd = generate_password_hash(password, method = 'sha256')
        print(username, password, hashed_pwd, email)

        ins = Users_tbl.insert().values(username = username,
                                        password = hashed_pwd,
                                        email = email)
        
        # sql = f"INSERT INTO {Users_tbl.name} (username, email, password) VALUES ({username}, {email}, {hashed_pwd})"

        conn = engine.connect()
        conn.execute(ins)        
        conn.close()
        print('done')
        return ''
    else:
        print('error')
        return 'Error'