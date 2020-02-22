import dash_core_components as dcc

# https://plot.ly/python/
# https://plot.ly/javascript/figure-labels/


def layout():
    return [
        dcc.Graph(
            figure={
                'data': [
                    {'type': 'bar',
                     'x': ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'],
                     'y': [20, 15, 12, 10, 18, 4, 1]
                     }
                ],
                'layout': {
                    'title': {
                        'text': 'barGraphTitle'
                    },
                    'xaxis': {
                        'title': {
                            'text': 'barGraphXaxis'
                        }
                    },
                    'yaxis': {
                        'title': {
                            'text': 'barGraphYaxis'
                        }
                    },
                }
            }
        )
    ]
