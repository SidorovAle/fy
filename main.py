class item:
    name = " "
    postion = "start"

    def __init__(self,name):
        self. name = name


class game:
    wolf = item('wolf')
    goat = item('goat')
    cabbage = item('cabbage')
    position = 'start'

    def is_boat_empty(self):
        return self.wolf.position != 'boat' and self.goat.position != 'boat' and self.cabbage.position != 'boat'

    def add_to_boat(self, added_item):
        if self.is_boat_empty():
            added_item.position = 'boat'
        else:
            print('Лодка уже занята!')

    def remove_from_boat(self, removed_item, place):
        if removed_item.position == 'boat':
            removed_item.position = place
        else:
            print('Предмет находится не в лодке!')

    def is_failed(self):
        return self.wolf.position == self.goat.position and self.position != self.goat.position \
               or self.goat.position == self.cabbage.position and self.position != self.goat.position

print('Игра "Волк, коза и капуста".')
my_game = game()
while not game.is_win() and not game.is_failed():
    while True:
        item1 = input('Введите предмет, который вы хотите положить/достать из лодки. (W, G, C) или S чтобы переправить лодку на другой берег.')
        if item1 == 'W' or item1 == 'G' or item1 == 'C':
            break
        else:
            print('Ошибка! Введите корректный символ.')
    if item1 == 'W':
        if my_game.wolf.position == 'start' or 'end':
            my_game.add_to_boat(my_game.wolf)
    elif item1 == 'G':
        if my_game.goat.position == 'start' or 'end':
            my_game.add_to_boat(my_game.goat)
    elif item1 == 'C':
        if my_game.cabbage.position == 'start' or 'end':
            my_game.add_to_boat(my_game.cabbage)
    else:
        my_game.change_position()
