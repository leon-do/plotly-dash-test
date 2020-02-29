import dash_core_components as dcc
import dash_html_components as html

# https://dash.plot.ly/urls


def layout():
    return html.Div([
        dcc.Location(id='url', refresh=False),
        html.H4('navbar'),
        html.Div(dcc.Link('graph examples', href='/graph_examples')),
        html.Div(dcc.Link('table examples', href='/table_examples')),
        html.Div(dcc.Link('rows columns', href='/rows_columns')),
        html.Div(dcc.Link('callback example', href='/callback_example')),
    ])
