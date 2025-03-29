# user_guide_router.py
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional

from ..requests import SearchRequest
from ..responses import SearchResponse


router = APIRouter()

# Simulated User Guide Data (Replace with your actual data source)
user_guides = [
    {"id": 1, "title": "Getting Started", "content": "This guide helps you get started."},
    {"id": 2, "title": "Advanced Features", "content": "Learn about advanced features."},
    {"id": 3, "title": "Troubleshooting", "content": "Solutions to common problems."},
    {"id": 4, "title": "API Reference", "content": "Documentation of the API endpoints."},
]


@router.post("/user-guides/search", response_model=SearchResponse)
async def search_user_guides(search_request: SearchRequest):
    """
    Search user guides based on a query.
    """
    results = [
        guide
        for guide in user_guides
        if search_request.query.lower() in guide["title"].lower() or search_request.query.lower() in guide["content"].lower()
    ]

    if search_request.limit:
        results = results[:search_request.limit]

    return SearchResponse(results=results)

@router.get("/user-guides/{guide_id}")
async def get_user_guide(guide_id: int):
    for guide in user_guides:
        if guide["id"] == guide_id:
            return guide
    raise HTTPException(status_code=404, detail="User guide not found")

@router.get("/user-guides")
async def get_all_user_guides():
    return user_guides
