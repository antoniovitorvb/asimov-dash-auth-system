import dash
from dash import Dash, html, dcc, Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from werkzeug.security import generate_password_hash

from app import *

def render_layout():
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
@app.callback(
    Output(component_id='register-state', component_property='data'),
    Input(component_id='register-button', component_property='n_clicks'),

    [State(component_id='user-register', component_property='value'),
     State(component_id='pwd-register', component_property='value'),
     State(component_id='email-register', component_property='value')]
)
def register(n_clicks, name, pwd, email):
    if n_clicks == None:
        raise PreventUpdate
    
    if all([name, pwd, email]): # All elements in the list are NOT None!
        hashed_pwd = generate_password_hash(pwd, method='sha256')
        ins = Users_tbl.insert().values(username=name, email=email, password=hashed_pwd)

        # sql = f"INSERT INTO {Users_tbl.name} (username, email, password) VALUES ('{name}', '{email}', '{hashed_pwd}')"

        conn = engine.connect()
        conn.execute(ins)
        conn.close()
        print('Done!')
        return ''
    else:
        print('erro')
        return 'error'