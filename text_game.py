import json


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


locations = conf['locations']
bag = []
# print(locations)
start_location_name = conf["start"]
current_location = locations[start_location_name]
# print(current_location)
look_around()
# current_location = locations["Castle"]
change_location("Castle")
change_location("Cave")
while True:
    prompt = input('What do you want?\n')
    if prompt in ['help', 'commands']:
        commands()
    elif prompt in ['quit', 'exit']:
        answer = input('Do you really want to quit the game? y/n\n')
        if answer in ['y', 'yes']:
            print('Bye!')
            break
        else:
            print('ok')
    elif prompt == 'look around':
        look_around()
    elif prompt.startswith('go to'):
        loc = prompt[6:]
        change_location(loc)
    else:
        print('Unknown command')

locations = [Location("forest"), Location("castle")]
locations = {"forest": Location("forest")}
locations["forest"].add_item(Item("key"))
locations["forest"].show_items()
