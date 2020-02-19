import dash_table


# https://dash.plot.ly/datatable

def getData():
    # get from api call
    return [
        {'name': 'joe', 'age': 22},
        {'name': 'jill', 'age': 44},
        {'name': 'james', 'age': 19}
    ]


def layout():
    data = getData()
    return dash_table.DataTable(
        columns=[{'name': i, 'id': i} for i in data[0].keys()],
        data=data,
        sort_action="native",
    )
