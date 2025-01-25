from typing import Optional
from pydantic import BaseModel, Field

class BookRequest(BaseModel): 
    id: Optional[int] = Field(default=None, title='id is not needed')
    title: str = Field(min_length=3, description="title")
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=11)
    published_year: int = Field(gt=0, lt=2026)

    model_config = {
        "json_schema_extra": {
            "example": 
                {
                    "title": "The name of the book",
                    "author": "The full name of the author",
                    "description": "A brief summary of the book",
                    "rating": 10,
                    "published_year": 2025
                }
            
        }
    }