class ProductItem:
    def __init__(self, name, price):
        self.name=name
        self.price=price

    def info(self):
        return self.name + ":$" + str(self.price)

    def get_total_price(self, count):
        total_postage_price=self.price * count

        if count >= 3:
            total_postage_price += 500
        return round(total_postage_price)



