from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'
class Shop:
    def __init__(self):
        self.__textfile = "products.txt"
    def get_products(self):
        file = open(self.__textfile, 'r')
        b = file.read()
        file.close()
        return b
    def add(self, *products):
        for i in products:
            file = open(self.__textfile, mode='r')
            existing_products = file.read()
            if f"{i.name}, {i.weight}" in existing_products:
                print(f'Продукт {i.name} уже есть в магазине')
            else:
                file = open(self.__textfile, 'a')
                file.write(f'{i}\n')
            file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
