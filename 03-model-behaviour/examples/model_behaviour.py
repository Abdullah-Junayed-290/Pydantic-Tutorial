from pydantic import (
    BaseModel,
    ValidationError,
    field_validator,
    model_validator,
    computed_field,
)


class User(BaseModel):
    username: str

    @field_validator("username")
    def username_length(cls, values):
        if len(values) < 4:
            raise ValueError("username must be 4 characters!")
        return values

    @field_validator("username")
    def username_max_length(cls, values):
        if len(values) > 6:
            raise ValueError("username smaller than 6 characters!")
        return values

    @field_validator("username")
    def username_required(cls, values):
        if values == "":
            raise ValueError("username is required!")
        return values

    @field_validator("username")
    def username_type_validation(cls, values):
        if values == str:
            raise ValueError("username must be a string!")
        return values


try:
    new_user = {
        "username": "Abdul",
    }
    user1 = User(**new_user)
    print(user1)
except ValidationError as err:
    print(err.errors())
