import dash_html_components as html
import dash_core_components as dcc
import dash_table

# https://dash.plot.ly/getting-started-part-2


def layout():
    return html.Div([
        html.Div(children="callback_example"),
        dcc.Input(id='my-id', value='type here', type='text'),
        html.Div(id='my-div', children="this text will change")
    ])
