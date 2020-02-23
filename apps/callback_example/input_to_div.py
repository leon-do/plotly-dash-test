import dash_html_components as html
import dash_core_components as dcc
from app import app
from dash.dependencies import Input, Output

# https://dash.plot.ly/getting-started-part-2


def layout():
    return html.Div([
        dcc.Input(id='my-input', placeholder='my-input here', type='text'),
        html.Div(id='my-div')
    ])


@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-input', component_property='value')]
)
def update_output_div(input_value):
    return input_value
