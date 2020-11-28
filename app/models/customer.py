from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship

class Customer(Base):
    __tablename__ = 'customers'
    CustomerId = sa.Column(sa.INTEGER, primary_key=True)
    CustomerName = sa.Column(sa.String(250), nullable=False)
    CustomerPhone = sa.Column(sa.String(45), nullable=False)
    CustomerEmail = sa.Column(sa.String(45), nullable=False)
    Cars = relationship("Car", back_populates="Owner")


    def __repr__(self):
        return f'Customer({self.CustomerId}, {self.CustomerName}, {self.CustomerPhone}, {self.CustomerEmail}, {"".join(car.Manufacturer +" "+ car.Model +" " + car.Year + "," for car in self.Cars)})'
