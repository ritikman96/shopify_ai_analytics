# AI-Powered Shopify Analytics App (Mock Mode)

## Overview
This project is a mini AI-powered analytics application for Shopify stores.
It allows users to ask natural-language business questions (sales, inventory, customers),
which are interpreted by an AI agent and translated into ShopifyQL queries.
The system returns clear, business-friendly insights instead of raw data.

This implementation uses **mocked Shopify data** to focus on architecture,
agent reasoning, and API design, as allowed by the assignment.

---

## Architecture

Client (Swagger / API Client)
|
v
FastAPI Backend
|
v
AI Agent
(Intent → Plan → ShopifyQL → Execute → Explain)
|
v
Mock ShopifyQL Execution


### Components
- **FastAPI**: API layer that accepts user questions
- **Agent Layer**:
  - Intent classification
  - ShopifyQL generation
  - Query execution (mock)
  - Business explanation
- **Shopify Client (Mock)**:
  - Simulates ShopifyQL execution and returns realistic data

---

## Agent Workflow
1. **Understand Intent**
   - Detects whether the question is about sales, inventory, or customers
2. **Plan**
   - Determines required data and time range
3. **Generate ShopifyQL**
   - Produces a realistic ShopifyQL query
4. **Execute**
   - Executes query against mocked Shopify data
5. **Explain Results**
   - Converts raw metrics into simple business language

---

## API Endpoint

### POST `/ask`

#### Request Body
```json
{
  "store_id": "demo-store.myshopify.com",
  "question": "What were my top 5 selling products last week?"
}



RESPONSES
{
  "answer": "Your top-selling product last week was Basic T-Shirts with 120 units sold. These products drove most of your sales.",
  "confidence": "high",
  "shopifyql": "FROM sales SHOW sum(quantity) GROUP BY product_title SINCE -7d ORDER BY sum(quantity) DESC LIMIT 5"
}



PROJECT STRUCTURE
python_ai_service/
│
├── main.py
├── shopify_client.py
├── requirements.txt
├── README.md
│
├── agent/
│   ├── __init__.py
│   ├── intent.py
│   ├── shopifyql.py
│   ├── executor.py
│   └── explainer.py


Assumptions & Notes

Shopify API and OAuth are mocked

ShopifyQL queries are simulated

Focus is on system design and agent reasoning

Real Shopify integration can be added later