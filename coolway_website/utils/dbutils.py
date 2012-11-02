import django.db

def run_single_value_query(query, *params):
    """
    Helper: run a query returning a single value (e.g. a COUNT) and return the value.
    """
    c = django.db.connections['default'].cursor()
    c.execute(query, params)
    return c.fetchone()[0]