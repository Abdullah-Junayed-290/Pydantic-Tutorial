from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    password: str
    
new_user = {
    "id": 1,
    "name": "Junayed",
    "password": "123456"
}

user1 = User(**new_user)

print(user1)