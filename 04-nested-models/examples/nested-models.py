from pydantic import BaseModel
from typing import List, Optional


class Address(BaseModel):
    country: str
    city: str
    post_code: str


class User(BaseModel):
    id: int
    name: str
    address: Address


class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List["Comment"]] = None


Comment.model_rebuild()

address = Address(country="Bangladesh", city="Dhaka", post_code="140")

print("\n\n", address)

user = User(id=1, name="Md. Abdullah Junayed", address=address)

print("\n\n", user)

comment = Comment(
    id=1,
    content="First Comment.",
    replies=[
        Comment(
            id=2,
            content="First Reply.",
            replies=[
                Comment(
                    id=4,
                    content="replying in first reply.",
                )
            ],
        ),
        Comment(id=3, content="Second Reply."),
    ],
)

print("\n\n", comment)
