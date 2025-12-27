from shopify_client import run_shopifyql_query

def execute_query(store_id: str, shopifyql: str):
    return run_shopifyql_query(store_id, shopifyql)
