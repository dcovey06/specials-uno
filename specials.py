def draw_2(deck, current_player):
    # player to the right/left of current_player draws 2
    # skips next player after they draw
    # written in main code
    current_player.draw_many(deck, 2)


def draw_4(deck, current_player):
    # current_player decides color (red, green, blue, yellow)
    # player to the right/left of current_player draws 4
    # skips next player after they draw
    is_valid = False
    while not is_valid:
        chosen_color = input('What color would you like to change to? ')
        if chosen_color.lower() == "red" or chosen_color.lower() == "blue" or \
                chosen_color.lower() == "green" or chosen_color.lower() == "yellow":
            current_color = chosen_color.lower()
            print(f'\nThe color has been changed to {current_color}\n')

        is_valid = chosen_color.lower() == 'red' or chosen_color.lower() == 'blue' or \
            chosen_color.lower() == 'yellow' or chosen_color.lower() == 'green'
        if not is_valid:
            print('\nThat is not a valid color. Please input red, green, blue, or yellow.\n')

    # written in main code
    current_player.draw_many(deck, 4)


def wild():
    # current_player decides color (red, green, blue, yellow)
    # moves to next player
    is_valid = False
    while not is_valid:
        chosen_color = input('What color would you like to change to? ')
        if chosen_color.lower() == "red" or chosen_color.lower() == "blue" or \
                chosen_color.lower() == "green" or chosen_color.lower() == "yellow":
            current_color = chosen_color.lower()
            print(f'\nThe color has been changed to {current_color}\n')

        is_valid = chosen_color.lower() == 'red' or chosen_color.lower() == 'blue' or \
            chosen_color.lower() == 'yellow' or chosen_color.lower() == 'green'
        if not is_valid:
            print('\nThat is not a valid color. Please input red, green, blue, or yellow.\n')


def reverse(game):
    # reverse the order the players are going in
    # written in main code
    game.clockwise = not game.clockwise


def skip(game):
    # skip player to the right/left of the current_player
    # written in main code
    game.next_player()
