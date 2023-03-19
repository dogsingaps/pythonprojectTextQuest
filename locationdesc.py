class User:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = Inventory()

    def get_info(self):
        print(self.health, self.name)
        self.inventory.get_items_list()


class Location:
    # def __init__(self) -> None:
    def __init__(self, name):
        self.name = name


class Inventory:
    def __init__(self):
        self.items = ['gold', 'axe']

    def get_items_list(self):
        print(self.items)


class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def get_info(self):
        print(self.name, self.weight)


class ComplexItem(Item):
    def __init__(self, name, weight, *items):
        super().__init__(name, weight)
        self.items = items


user1 = User('Chupakabra')
user1.get_info()
user2 = User('johnny')
user2.get_info()
user2.health += 10
user2.get_info()

locations = [Location('forest'), Location('field')]
