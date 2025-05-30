from pydantic import BaseModel

# TODO: Create product model with id, name, price, in_stock


class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool


new_product = {"id": 1, "name": "Snapdragon 8 Elite", "price": 20000, "in_stock": True}

product1 = Product(**new_product)
print(product1)
