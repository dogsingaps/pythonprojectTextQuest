import json
import random
from curses import wrapper


def print_d():
    print('----------------------------------------')


def get_item(item):
    global current_location
    global bag
    if item in current_location['items']:
        current_location['items'].remove(item)
        bag.append(item)
        print(item, "was added in your bag")
        look_into()
    else:
        print("You can't see ", item)


def put_item(item):
    global current_location
    global bag
    if item in bag:
        bag.remove(item)
        print(item, 'was removed from your bag')
        look_into()
        look_around()
    else:
        print(item, 'is not in your bag ')
        look_into()
        look_around()


def look_into():
    print_d()
    if bag:
        if len(bag) == 1:
            print('You only one item:, ', bag[0])
        else:
            print('Items in your bag:' ', '.join(bag))
    else:
        print('Your bag is empty')


def look_around():
    print_d()
    desc = current_location['desc']
    print("You're in", desc)
    print("Items:", ','.join(current_location["items"]))


def change_location(new_location):
    global current_location
    if current_location["next"]:
        if new_location in current_location["next"]:
            current_location = locations[new_location]
            look_around()
        else:
            print_d()
            print("You can't go to", new_location)
    else:
        print_d()
        print("It's a dead end. Sorry:(")


def commands():
    print_d()
    print('List of commands:\nlook_around\ngo to X\nget X\nlook into\n')


with open('config.json') as f:
    conf = json.load(f)


    class SimpleItem:
        def __init__(self, name, weight):
            self.name = name
            self.weight = weight

        def show_desc(self):
            print(self.name, self.weight)


    class Location:
        def __init__(self, name):
            self.name = name
            self.items = items
            self.next = next
            self.desc = desc

    for i in conf["locations"]:
        locations = {}


        def add_item(self, item):
            self.items.append(item)

        def show_items(self):
            for i in self.items:
                print(i.show_desc())

class NPC:
    def __init__(self, name, riddles):
        self.name = name
        self.riddles = riddles
    def give_riddle(self):
        rd = random.choice(self.riddles)
        print(rd.question)

class Riddles:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

def change_size(self, new_cell_max):
    for i in range (len(self.items) - new_cell_max):
        self.drop_item(random.choices(self.items).name)
    sell_max = new_cell_max

def get_status(f):
    def wrapper(*args, **kwargs):
        rating = f()
        if 0 < rating < 25:
            return rating, 'Bad'
        elif 26 < rating < 75:
            return rating, 'Good'
        else:
            return rating, 'Very Good'
    return wrapper


@get_status
def get_rating():
    return random.randint(0, 100)


class Gamer:
    def __init__(self, login, location):
        self.name = login
        self.location = location
        self.bag = Bag()
        self.xp = 0
        self.health = 10

