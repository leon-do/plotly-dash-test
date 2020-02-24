import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


# https://dash.plot.ly/urls


def layout():
    return html.Div([
        html.H4('header'),
        html.A('Google', href='https://www.google.com', target='_blank'),
    ], className='navbar')
