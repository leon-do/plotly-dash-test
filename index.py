import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from apps.sidebar import sidebar
from app import app

app.layout = html.Div([
    html.Div(sidebar.layout())
])


if __name__ == '__main__':
    app.run_server(debug=True)
