def classify_intent(question: str) -> str:
    q = question.lower()
    if "top" in q and "selling" in q:
        return "top_selling_products"
    if "inventory" in q or "stock" in q:
        return "inventory"
    if "customer" in q:
        return "customers"
    return "unknown"
