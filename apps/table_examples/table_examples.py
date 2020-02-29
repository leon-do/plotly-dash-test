import dash_html_components as html
from apps.table_examples import table1, table2


def layout():
    return html.Div([
        html.Div(table1.layout()),
        html.Div(table2.layout()),
    ])
