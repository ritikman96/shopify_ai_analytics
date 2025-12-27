from fastapi import FastAPI
from pydantic import BaseModel

from agent.intent import classify_intent
from agent.shopifyql import generate_shopifyql
from agent.explainer import explain_results
from agent.executor import execute_query

app = FastAPI(title="Shopify AI Analytics (Mock Mode)")

class QueryRequest(BaseModel):
    store_id: str
    question: str

@app.post("/ask")
def ask_question(req: QueryRequest):
    intent = classify_intent(req.question)
    shopifyql = generate_shopifyql(intent)

    result = execute_query(req.store_id, shopifyql)

    data = result["data"] if isinstance(result, dict) else []

    answer = explain_results(intent, data)

    return {
        "answer": answer,
        "confidence": "high" if data else "low",
        "shopifyql": shopifyql
    }
