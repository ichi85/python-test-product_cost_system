from lessontest2 import ProductItem

class Product(ProductItem):
    def info(self):
        return self.name + ": $" + str(self.price)