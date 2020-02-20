import dash
import dash_html_components as html
import bar_graph
import pie_chart
import line_chart 
import static_table
import json_table
import callback_example

# https://github.com/plotly/dash-oil-and-gas-demo/blob/master/app.py


# init app and loads ./assets
app = dash.Dash(__name__)

# put on screen
app.layout = html.Div([
    html.Div([
        html.Div(bar_graph.layout())
    ], className='row'),

    html.Div([
        html.Div(pie_chart.layout(), className='six columns'),
        html.Div(line_chart.layout(), className='six columns')
    ], className='row'),

    html.Div([
        html.Div(static_table.layout(), className="three columns"),
        html.Div(json_table.layout(), className="three columns"),
		html.Div(callback_example.layout(), className="six columns")
    ], className='row'),

])

# $ python app.py
if __name__ == "__main__":
    app.run_server(debug=True)
