import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from apps.header import header
from apps.navbar import navbar
from apps.footer import footer
from apps.graph_examples import graph_examples
from apps.table_examples import table_examples
from apps.rows_columns import rows_columns
from apps.callback_example import callback_example

app.layout = html.Div([
    html.Header(header.layout()),
    html.Nav(navbar.layout()),
    html.Main(id='page-content'),
    html.Footer(footer.layout())
], className='container')

# input from sidebar.py
@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return graph_examples.layout()
    elif pathname == '/graph_examples':
        return graph_examples.layout()
    elif pathname == '/table_examples':
        return table_examples.layout()
    elif pathname == '/rows_columns':
        return rows_columns.layout()
    elif pathname == '/callback_example':
        return callback_example.layout()
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)
