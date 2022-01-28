class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_items(self, name, price):
        a = {"name": name, "price": price}
        self.items.append(a)
        print(self.items)

    def stock_price(self):
        return sum(i["price"] for i in self.items)

a = Store("alex")
print(a.add_items("test", 25.0))
print(a.add_items("Bob", 4))
print(a.stock_price())