from fastapi import FastAPI
from fastapi.params import Depends

from Model.Product import Product
from Model.database import engine, SessionLocal
from sqlalchemy.orm import Session
from Model.product_table import Base, ProductDetails

app = FastAPI()

# Create tables
Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/product")
def product_name(product: Product, db: Session = Depends(get_db)):
    product_data = ProductDetails(name=product.name, email=product.email, product_name=product.product,
                                  description=product.description)
    db.add(product_data)
    db.commit()
    db.refresh(product_data)
    return product
