from fastapi import FastAPI
from fastapi.params import Depends

from Model.Product import Product
from Model.database import engine, SessionLocal
from sqlalchemy.orm import Session
from Model.product_table import Base, ProductDetails

app = FastAPI()

# Create tables
Base.metadata.create_all(engine)


# connect to the db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# add product in database
@app.post("/product")
def product_name(product: Product, db: Session = Depends(get_db)):
    product_data = ProductDetails(name=product.name, email=product.email, product_name=product.product,
                                  description=product.description)
    db.add(product_data)
    db.commit()
    db.refresh(product_data)
    return product


# get all the product list
@app.get("/products")
def all_products_list(db: Session = Depends(get_db)):
    products = db.query(ProductDetails).all()
    return products


# get specific product
@app.get("/product/{id}")
def product(id, db: Session = Depends(get_db)):
    product = db.query(ProductDetails).filter(ProductDetails.id == id).first()
    return product
