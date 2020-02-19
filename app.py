import dash
import dash_html_components as html
import bank_account
import thoughts_when_sleeping
import productivity
import car_table
import person_table

# https://github.com/plotly/dash-oil-and-gas-demo/blob/master/app.py


# init app and loads ./assets
app = dash.Dash(__name__)

# put on screen
app.layout = html.Div([
    html.Div([
        html.Div(bank_account.layout())
    ], className='row'),

    html.Div([
        html.Div(thoughts_when_sleeping.layout(), className='six columns'),
        html.Div(productivity.layout(), className='six columns')
    ], className='row'),

    html.Div([
        html.Div(car_table.layout(), className="three columns"),
        html.Div(person_table.layout(), className="three columns")
    ], className='row'),

])

# $ python app.py
if __name__ == "__main__":
    app.run_server()
