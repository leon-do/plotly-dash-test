import dash_table
import dash_html_components as html
import requests
from apps.error import error

# fetches data from api and fitlers table


def getData():
    response = requests.get('https://api.coincap.io/v2/assets').json()
    data = response['data']
    # only want symbol and priceUsd
    filtered_columns = [
        {'name': 'symbol', 'id': 'symbol'},
        {'name': 'priceUsd', 'id': 'priceUsd'}
    ]
    filtered_data = [{
        'symbol': i['symbol'],
        'priceUsd': float(i['priceUsd'])
    } for i in data]
    return {
        'columns': filtered_columns,
        'data': filtered_data
    }


def layout():
	# all requests should be wrapped in try/except
    try:
        data = getData()
        return dash_table.DataTable(
            columns=data['columns'],
            data=data['data'],
            sort_action="native",
        )
    except:
        return error.layout()
