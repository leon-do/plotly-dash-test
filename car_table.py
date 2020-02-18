import dash_table
import pandas as pd

# https://dash.plot.ly/datatable/interactivity


def graph():
    return dash_table.DataTable(
        id='table',
        columns=[
            {'name': 'car', 'id': 'car'},
            {'name': 'model', 'id': 'model'}
        ],
        data=[
            {'car': 'honda', 'model': 'civic'},
            {'car': 'ford', 'model': 'fusion'},
            {'car': 'tesla', 'model': '3'}
        ],
        sort_action="native",

    )
