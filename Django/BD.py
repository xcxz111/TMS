from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://TMS_USER:1234@host:5432/TMS')

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False, unique=True)
    user_name = Column(String(100), nullable=False)
    email = Column(String(100))
    orders = relationship("Order", back_populates="customer")


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, nullable=False)
    product_name = Column(String(100), nullable=False)
    price = Column(Float(precision=2), nullable=False)
    orders = relationship("Order", back_populates="product")
    __table_args__ = (UniqueConstraint('product_id', 'price', name='_product_uc'),)


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('customers.user_id'), nullable=False)
    product_id = Column(Integer, nullable=False)
    price = Column(Float(precision=2), nullable=False)
    customer = relationship("Customer", back_populates="orders")
    product = relationship("Product", back_populates="orders")
    __table_args__ = (ForeignKeyConstraint([product_id, price], [Product.product_id, Product.price]),)


Base.metadata.create_all(engine)
