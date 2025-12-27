# agent.py
import json
import asyncio
from shopify_client import run_shopifyql_query

class ShopifyAIAgent:
    """
    Mock AI Agent that interprets questions and returns simulated business insights.
    """

    async def process_question(self, store_id: str, question: str):
        print(f"[AGENT] Received question: {question}")

        # Step 1: Determine intent and fake ShopifyQL
        shopifyql = self._generate_fake_shopifyql(question)
        print(f"[AGENT] Generated ShopifyQL: {shopifyql}")

        # Step 2: Fetch mock Shopify data
        data = await run_shopifyql_query(store_id, shopifyql)

        # Step 3: Summarize into plain English
        answer = self._summarize_answer(data, question)

        return {
            "answer": answer,
            "confidence": "medium",
            "shopifyql": shopifyql,
            "data": data
        }

    def _generate_fake_shopifyql(self, question: str) -> str:
        question_lower = question.lower()
        if "inventory" in question_lower or "stock" in question_lower:
            return "SELECT product_name, inventory_quantity FROM products"
        elif "sales" in question_lower or "revenue" in question_lower:
            return "SELECT date, total_sales FROM orders"
        elif "customer" in question_lower:
            return "SELECT customer_name, order_count FROM customers"
        else:
            return "SELECT * FROM shop_data"

    def _summarize_answer(self, data, question: str) -> str:
        if "inventory" in question.lower():
            return "Based on recent data, products like Sneakers and T-shirts may run low next week."
        elif "sales" in question.lower():
            return "Sales have been stable around $3,800 per day this week."
        elif "customer" in question.lower():
            return "You have several repeat customers in the last 90 days."
        else:
            return "Here's a summary of your store data."
