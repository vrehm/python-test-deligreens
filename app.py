# Import required libraries
import os
from random import randint

import plotly.plotly as py
from plotly.graph_objs import *

import flask
import dash
from dash.dependencies import Input, Output, State, Event
import dash_core_components as dcc
import dash_html_components as html


# Setup the app
# Make sure not to change this file name or the variable names below,
# the template is configured to execute 'server' on 'app.py'
server = flask.Flask(__name__)
server.secret_key = os.environ.get('secret_key', str(randint(0, 1000000)))
app = dash.Dash(__name__, server=server)


########### APP ###############
app = dash.Dash()

app.layout = html.Div([
        html.H1(children = 'Mot de passe :'),
        dcc.Input(id = 'input_X', type = 'number'),
        dcc.Slider(id = 'slider',
                   min=6,
                   max=36,
                   step=6,
                   marks={i: '{} Mois'.format(i) for i in range(6,37,6)},
                   value=18),
        html.Button(id = 'button_login', children = 'Login'),
#        html.Div(id = 'div1', children=),
        html.Div(id = 'out')
        ])

@app.callback(
        Output('out','children'),
        [Input('button_login', 'n_clicks')],
        [State('input_X', 'value')])
def outoutoutotut(n_clicks, password):
    res = html.H1(children = 'fghjk')
    return res

# Run the Dash app
if __name__ == '__main__':
    app.server.run(debug=True, threaded=True)
