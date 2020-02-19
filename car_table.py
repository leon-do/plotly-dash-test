import dash_table

# https://dash.plot.ly/datatable


def layout():
    return dash_table.DataTable(
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
