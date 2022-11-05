def get_select_query_string(table, stock):
    """
    Generate query string (SELECT)
    :param table: [string] name of the table
    :param stock: [string] stock code of the company
    :return: [string] SQL statement
    """
    query_str = "SELECT * FROM " + table + " WHERE Ticker='" + stock + "';"
    return query_str

def update_annual_report_string(table, ticker, value_to_update, kpi_to_update, year):
    value_to_update = str(value_to_update)
    year = str(year)
    update_string = 'UPDATE ' + \
                    table + ' SET Value=' + \
                    value_to_update + ' WHERE Ticker = "' + ticker + \
                    '" AND KPI ="' + kpi_to_update + \
                    '" AND Year ="' + year + '";'

    return update_string


#ADD A CONNECT TO DBC FUNCTION