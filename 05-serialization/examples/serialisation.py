from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime


class Address(BaseModel):
    country: str
    city: str
    post_code: int


class User(BaseModel):
    id: int
    name: str
    email: str
    address: Address
    is_active: bool = True
    create_at: datetime
    tags: List[str] = []

    mmodel_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime("%d-%m-%Y %H:%M:%S")}
    )


user = User(
    id=1,
    name="Junayed",
    email="junayed123@ai.com",
    create_at=datetime(2007, 2, 23, 10, 00),
    tags=["vip", "developer"],
    address=Address(
        country="BD",
        city="Dhaka",
        post_code=140,
    ),
)
print(user)

print()
# pydantic model_dump() -> Convert to dict
python_dict = user.model_dump()
print(python_dict)

# pydantic model_dump_json() -> return json
json_str = user.model_dump_json()
print(json_str)
