import dash_html_components as html


def layout():
    return html.Div([
        html.Div(
            '🍎',
            style={
                'background-color': '#ff928b',
                'text-align': 'center'
            }
        )
    ])
