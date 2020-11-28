from db import Base, engine, session
from models.customer import  Customer
from models.car import Car



def main():
    Base.metadata.create_all(engine)

    customer = Customer(CustomerName= 'mosh', CustomerPhone='123403492', CustomerEmail='mosh@gmail.com')
    session.add(customer)
    car = Car(Manufacturer='VW', Model='V60', Year='2020', CustomerId= 7)
    session.add(car)
    session.commit()
    customers = session.query(Customer).all()
    for customer in customers:
        print(customer)



if __name__ == '__main__':
    main()
