from pydantic import BaseModel, Field, ValidationError, computed_field

# TODO: Create Booking model
# Fields:
#  -  user_id: int
#  -  room_id: int
#  -  nights: int (must be >=1)
#  -  rate_per_night: float
# Also, add computed field: total_amount = nights * rate_per_night

class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)
    rate_per_night: float
    @computed_field(return_type=float)
    @property
    def total_amount(self):
        return self.nights * self.rate_per_night
        
try:
    new_booking = {
        "user_id": 1,
        "room_id": 101,
        "nights": 3,
        "rate_per_night": 1000,
    }
    
    booking1 = Booking(**new_booking)
    print(booking1)
except ValidationError as err:
    print(err.errors())