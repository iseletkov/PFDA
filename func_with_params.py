from datetime import datetime, timedelta

# def print_cheque(name, price):
#     print_cheque(name, price, 1)

# def print_cheque(name, price, time):

#     print_cheque(name, price, 1, datetime.now())

# def print_cheque(name, price, quantity=1):
#     print_cheque(name, price, quantity, datetime.now()):

# def print_cheque(name, price, quantity, time=None):
#     if time==None:
#         time = datetime.now()
#     print(f"{time}")
#     print(f"{name} {quantity} {price}")


def print_cheque(**kwargs):
    """
        name - наименовние товара в чеке
        .

        ..
    """

    if "name" not in kwargs:
        print("Наименование товара не указано!")    
        return
    if "price" not in kwargs:
        print("Цена товара не указана!")    
        return
    
    quantity = kwargs.get("quantity", 1)
    dttm = kwargs.get("time", datetime.now())

    print(dttm)
    print(f"{kwargs["name"]} {quantity} {kwargs["price"]}")


print_cheque(
    name="Тестовый товар",
    price=123,
    # quantity=10,
    time = datetime.today() - timedelta(days=10)
)
