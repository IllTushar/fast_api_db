from pydantic import BaseModel


class Product(BaseModel):
    name: str
    email: str
    product: str
    description: str
