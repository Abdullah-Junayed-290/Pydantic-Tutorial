from pydantic import BaseModel
from typing import List, Dict, Optional


class Card(BaseModel):
    user_id: int
    items: List[str]
    quantities: Dict[str, int]


class BlogPost(BaseModel):
    id: int
    title: str
    image_uri: Optional[str] = None


new_card = {
    "user_id": 1,
    "items": ["apple keyboard"],
    "quantities": {
        "quantity": 10,
    },
}
new_post = {
    "id": 1,
    "title": "learning pydantic",
    "image_uri": "https://pydantic.com",
}

card1 = Card(**new_card)
post1 = BlogPost(**new_post)

print(card1)
print(post1)
