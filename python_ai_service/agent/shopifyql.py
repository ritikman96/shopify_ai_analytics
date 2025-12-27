def generate_shopifyql(intent: str) -> str:
    if intent == "top_selling_products":
        return (
            "FROM sales "
            "SHOW sum(quantity) AS total_sold "
            "GROUP BY product_title "
            "SINCE -7d "
            "ORDER BY total_sold DESC "
            "LIMIT 5"
        )
    return "SELECT * FROM shop_data"
