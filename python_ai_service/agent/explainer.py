def explain_results(intent: str, data: list):
    if intent == "top_selling_products" and data:
        top_product = data[0]
        return (
            f"Your top-selling product last week was {top_product['name']} "
            f"with {top_product['units']} units sold. "
            "These products drove most of your sales."
        )

    return "I couldn't find enough data to answer this question."
