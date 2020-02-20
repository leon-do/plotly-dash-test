import dash_core_components as dcc

# https://plot.ly/python/line-charts/


def layout():
    return [
        dcc.Graph(
            figure={
                'data': [
                    {'type': 'line',
                     'x': ['9am', '12pm', '3pm', '5pm', '9pm', '11pm'],
                     'y': [5, 2, 7, 1, 9, 2]
                     }
                ],
                'layout': {
                    'title': {
                        'text': 'lineChartTitle'
                    },
                    'xaxis': {
                        'title': {
                            'text': 'lineChartXaxis'
                        }
                    },
                    'yaxis': {
                        'title': {
                            'text': 'lineChartYaxis'
                        }
                    },
                }
            }
        )
    ]
