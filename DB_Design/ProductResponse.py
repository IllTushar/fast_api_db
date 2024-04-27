from sqlalchemy import INTEGER, VARCHAR, Column
from .DBConnection import Base


class ProductDetails(Base):
    __tablename__ = "product_details"
    id = Column(INTEGER, autoincrement=True, primary_key=True)
    name = Column(VARCHAR)
    email = Column(VARCHAR)
    product_name = Column(VARCHAR)
    description = Column(VARCHAR)
