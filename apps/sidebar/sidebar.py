import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from apps.graph_examples import graph_examples
from apps.rows_columns import rows_columns
from apps.callback_example import callback_example

# https://dash.plot.ly/urls


def layout():
    return html.Div([
        dcc.Location(id='url', refresh=False),
        html.H4('sidebar'),
        html.Div(dcc.Link('graph examples', href='/graph_examples')),
        html.Div(dcc.Link('rows columns', href='/rows_columns')),
        html.Div(dcc.Link('callback example', href='/callback_example')),
        html.Div(id='page-content')
    ])


@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return graph_examples.layout()
    elif pathname == '/graph_examples':
        return graph_examples.layout()
    elif pathname == '/rows_columns':
        return rows_columns.layout()
    elif pathname == '/callback_example':
        return callback_example.layout()
    else:
        return '404'
