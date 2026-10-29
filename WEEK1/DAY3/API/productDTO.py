from pydantic import BaseModel

class product_DTO(BaseModel):
    id: int
    name: str
    price: float | int 