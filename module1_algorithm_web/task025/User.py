class User:
    id = None
    name = None
    order = {}

    def __init__(self, identifier, first_name):
        self.id = identifier
        self.name = first_name

    def total_sum(self):
        purchase = 0

        for item, price in self.order.items():
            purchase += price

        return purchase

    def add_purchase(self, item, price):
        self.order.update({item: price})
