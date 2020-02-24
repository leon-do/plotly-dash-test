import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from apps.navbar import navbar
from apps.sidebar import sidebar
from apps.graph_examples import graph_examples
from apps.rows_columns import rows_columns
from apps.callback_example import callback_example

app.layout = html.Div([
    html.Div(navbar.layout()),
    html.Div(sidebar.layout()),
    html.Div(id='page-content', className='container')
])

# input from sidebar.py
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


if __name__ == '__main__':
    app.run_server(debug=True)
