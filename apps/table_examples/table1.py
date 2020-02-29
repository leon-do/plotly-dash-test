import dash_table

# this displays hard coded table


def layout():
    return dash_table.DataTable(
		# each column should have a 'name' and 'id'
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
