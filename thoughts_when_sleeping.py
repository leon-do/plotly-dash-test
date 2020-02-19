import dash_core_components as dcc

# https://plot.ly/python/v3/pie-charts/


def layout():
    return [
        dcc.Graph(
            figure={
                'data': [{
                    'type': 'pie',
                    'hole': 0.4,
                    'labels': ["I'm sleepy", "This sucks", "Why"],
                    'values': [20, 30, 50]
                }
                ],
                'layout': {
                    'title': {
                        'text': 'Thoughts When Sleeping'
                    }
                }
            }
        )
    ]
