from pydantic import BaseModel, Field, ValidationError
from typing import Optional

# TODO: Create Employee model
# Fields:
# - id: int
# - name: str-(min-3 chars)
# -department: optional str-(default-'General')
# - salary: float (must be >= 10000)


class Employee(BaseModel):
    id: int
    name: str = Field(..., min_length=3)
    department: Optional[str] = "General"
    salary: float = Field(ge=10000)


try:
    new_employee = {
        "id": 1,
        "name": "Abdullah Junayed",
        "department": "Manager",
        "salary": 50000,
    }
    employee1 = Employee(**new_employee)
    print(employee1)
except ValidationError as err:
    print(err.errors())
