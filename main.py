from player import Player
from bot import RandomBot, GreedyBot
import random
import display
import game_logic
from items import Items

# Global Variables #
file_path = "items.txt"     # Item list to create item objects from
name = ""                   # Helper variable for item object creation.
value = 0                   # Helper variable for item object creation.
weight = 0                  # Helper variable for item object creation.

def create_item_list(file_path, delimiter=":"):
    """
    Create item objects from item text file that will be used for the game.

    :param file_path: File location where the "items.txt" file lives.
    :param delimiter: Delimiter used to separate values from descriptions to parse the data.

    :return: list_of_items - A list of the item objects created.
    """
    list_of_items = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                item = Items(name, value, weight)
                list_of_items.append(item)
                continue
            line = line.split(delimiter, 1)
            if line[0] == "name":
                name = line[1].strip()
            elif line[0] == "value":
                value = line[1].strip()
            elif line[0] == "weight":
                weight = line[1].strip()
    return list_of_items


def load_inventories(item_list, player, bot):
    """
    Give each player and both a selection of random items from the list of items, ensuring no duplicates.

    :param item_list: List of item objects
    :param player: Player object to load items into said player's inventory list.
    :param bot: Bot object to load items into said bot's inventory list.
    """
    for _ in range(4):
        item = random.choice(item_list)
        player.load_inventory(item)
        item_list.remove(item)

    for _ in range(4):
        item = random.choice(item_list)
        bot.load_inventory(item)
        item_list.remove(item)


def main():
    display.welcome()

    while True:
        display.menu()
        choice = input("Please make a selection: \n")
        item_list = create_item_list(file_path)

        if choice == '1':
            bot = RandomBot()
            player = Player()
            load_inventories(item_list, player, bot)
            game_logic.start_game(player, bot)
        elif choice == '2':
            bot = GreedyBot()
            player = Player()
            load_inventories(item_list, player, bot)
            game_logic.start_game(player, bot)
        elif choice == '3':
            print("Exiting game...")
            break
        else:
            print("Please choose from the available menu options")


if __name__ == "__main__":
    main()