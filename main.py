from fastapi import FastAPI
from fastapi.params import Depends

from DB_Design.ProductRequest import Product
from DB_Design.DBConnection import engine, SessionLocal
from sqlalchemy.orm import Session
from DB_Design.ProductResponse import Base, ProductDetails

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


# delete specific the row
@app.delete("/product/{id}")
def delete_product(id, db: Session = Depends(get_db)):
    product_delete = db.query(ProductDetails).filter(ProductDetails.id == id).delete(synchronize_session=False)
    db.commit()
    return {"message": "Product deleted successful", "deleted_product": product_delete}


# update data
@app.put("/product/{id}")
def update_product(id, products: Product, db: Session = Depends(get_db)):

        product_update = db.query(ProductDetails).filter(ProductDetails.id == id)
        if not product_update.first():
            pass
            # return {"message": "Product not found"}  # Return a message if product not found
        product_update.update(products.dict())
        db.commit()
        return {"message": "Product updated successfully"}  # Return success message Return the error messagev
