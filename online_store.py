class Products:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

class Costumer:
    def __init__(self, name, costumer_id, contact ):
        self.name = name
        self.costumer_id = costumer_id
        self.contact = contact
        self.orders = []

class OnlineShop:
    def __init__(self, order_id, date):
        self.order_id = order_id
        self.date = date

    def order(self, ):
        pass