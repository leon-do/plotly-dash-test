import dash
import dash_html_components as html
import bank_account, thoughts_when_sleeping, productivity, car_table, person_table

# https://github.com/plotly/dash-oil-and-gas-demo/blob/master/app.py


# init app and loads ./assets/style.css
app = dash.Dash(__name__ )

# put on screen
app.layout = html.Div([
    html.Div([
        html.Div(bank_account.graph())
    ], className='row'),

    html.Div([
        html.Div(thoughts_when_sleeping.graph(), className='six columns'),
        html.Div(productivity.graph(), className='six columns')
    ], className='row'),

    html.Div([
        html.Div(car_table.graph(), className="three columns"),
        html.Div(person_table.graph(), className="three columns")
    ], className='row'),

])

# $ python app.py
if __name__ == "__main__":
    app.run_server()
