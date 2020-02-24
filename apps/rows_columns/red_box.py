import dash_html_components as html


def layout():
    return html.Div([
        html.Div(
            '🍎',
            style={
                'backgroundColor': '#ff928b',
                'textAlign': 'center'
            }
        )
    ])
