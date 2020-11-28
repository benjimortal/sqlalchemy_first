from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship

class Car(Base):
    __tablename__ = 'cars'
    CarId = sa.Column(sa.INTEGER, primary_key=True)
    Manufacturer = sa.Column(sa.String(250), nullable=False)
    Model = sa.Column(sa.String(45), nullable=False)
    Year = sa.Column(sa.String(45), nullable=False)
    CustomerId = sa.Column(sa.INTEGER, sa.ForeignKey('customers.CustomerId'))
    Owner = relationship("Customer", back_populates="Cars")


    def __repr__(self):
        return f'Car({self.CustomerId}, {self.Manufacturer}, {self.Model}, {self.Year}, {self.Owner})'
