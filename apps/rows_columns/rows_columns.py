import dash_html_components as html
from apps.rows_columns import red_box, green_box


def layout():
    return html.Div([
        html.H4('Use className="row" and className="six columns". Max 12 columns/row'),

        html.Div([
            html.Div(red_box.layout())
        ], className='row'),

        html.Div([
            html.Div(green_box.layout(), className='one columns'),
            html.Div(red_box.layout(), className='one columns'),
            html.Div(green_box.layout(), className='one columns'),
            html.Div(green_box.layout(), className='one columns'),
            html.Div(red_box.layout(), className='one columns'),
            html.Div(green_box.layout(), className='one columns'),
            html.Div(green_box.layout(), className='one columns'),
            html.Div(red_box.layout(), className='one columns'),
            html.Div(green_box.layout(), className='one columns'),
            html.Div(green_box.layout(), className='one columns'),
            html.Div(red_box.layout(), className='one columns'),
            html.Div(green_box.layout(), className='one columns'),
        ], className='row'),

        html.Div([
            html.Div(green_box.layout(), className='nine columns'),
            html.Div(red_box.layout(), className='three columns'),
        ], className='row'),

    ])
