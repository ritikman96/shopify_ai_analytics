import time

def run_shopifyql_query(store_id: str, shopifyql: str):
    """
    Mock execution of ShopifyQL query
    """
    print(f"Running ShopifyQL for store: {store_id}")
    print(f"Query: {shopifyql}")

    time.sleep(1)  # simulate network delay

    if "group by product_title" in shopifyql.lower():
        return {
            "status": "success",
            "data": [
                {"name": "Basic T-Shirts", "units": 120},
                {"name": "Sneakers", "units": 95},
                {"name": "Hoodie", "units": 80},
                {"name": "Cap", "units": 60},
                {"name": "Jeans", "units": 50}
            ]
        }

    return {
        "status": "...",
        "data": [...]
    }
