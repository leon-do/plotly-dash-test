import dash_core_components as dcc

# https://plot.ly/python/
# https://plot.ly/javascript/figure-labels/


def graph():
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
                        'text': 'Bank Account'
                    },
                    'xaxis': {
                        'title': {
                            'text': 'day of the week'
                        }
                    },
                    'yaxis': {
                        'title': {
                            'text': 'dollars'
                        }
                    },
                }
            }
        )
    ]
