import dash_html_components as html
from apps.rows_columns import red_box, green_box


def layout():
    return html.Div([
        html.H4('Rows and Columns'),

        html.H5('use "className"="row" to create a row'),
        html.Div([
            html.Div(red_box.layout())
        ], className='row'),

        html.H5('Max 12 columns/row'),
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

        html.H5('green 9 rows, red 3 rows'),
        html.Div([
            html.Div(green_box.layout(), className='nine columns'),
            html.Div(red_box.layout(), className='three columns'),
        ], className='row'),

        html.H5('nested rows and columns'),
        html.Div([
            html.Div([
                html.Div(green_box.layout()),
                html.Div(red_box.layout()),
            ], className='row six columns'),
            html.Div(red_box.layout(), className='six columns'),
        ], className='row')

    ])
