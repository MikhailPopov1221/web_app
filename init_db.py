from database.db import Base, Sessionlocal, engine
from models.orders import Order
from models.products import Product


def init_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    
    session = Sessionlocal()
    
    p1 = Product(name = "Молоко 1л", price=85, count=15)
    session.add(p1)
    
    
    lst = [
        Product(name = "Хлеб", price=25, count=5),
        Product(name = "Гречка", price=85, count=56),
        Product(name = "Сахар 1кг", price=60, count=50)
    ]
    
    session.add_all(lst)
    session.commit()
    
    lst2 = [
        Order(
            customer_name="Петя",
            phone_number="89991112233", 
            product_id=1, 
            count=5
        ),
        Order(
            customer_name="Вася",
            phone_number="80001112244", 
            product_id=3, 
            count=3
        ),
        Order(
            customer_name="Костя",
            phone_number="89997775633", 
            product_id=2, 
            count=6
        )
    ]
    
    
    
    session.add_all(lst2)
    session.commit()
    
    session.close()
    
    
    
if __name__ == "__main__":
    init_database()