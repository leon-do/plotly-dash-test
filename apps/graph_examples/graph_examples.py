import dash_html_components as html
from apps.graph_examples import bar, line, pie


def layout():
    return html.Div([
        html.Div(bar.layout()),
        html.Div(line.layout()),
        html.Div(pie.layout()),
    ])
