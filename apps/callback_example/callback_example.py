import dash_html_components as html
from apps.callback_example import input_to_div


def layout():
    return html.Div([
        html.H4('callback example takes the value of my-input and outputs it to my-div'),
        html.Div(input_to_div.layout())
    ])
