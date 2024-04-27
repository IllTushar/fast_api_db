from pydantic import BaseModel


class Product(BaseModel):
    name: str
    email: str
    product_name: str
    description: str
