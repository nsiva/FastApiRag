from pydantic import BaseModel
from typing import List, Optional

class SearchResponse(BaseModel):
    results: List[dict]
