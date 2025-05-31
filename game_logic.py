import random
from bag import Bag
import items
import time


def bot_play(bot, bag):
    """
    Logic for bot to play their turn, given a play call by the bot to select the item based on their characteristic

    :param bot: The bot currently in play
    :param bag: Bag to hold the items
    """
    if bot.pass_turn == True:
        return
    elif len(bot.inventory) <= 0:
        bot.passed()
        return
    else:
        item = bot.play()
        if (int(item.get_weight()) + bag.get_weight()) > bag.max_weight:
            bot.inventory.remove(item)
            bot_play(bot, bag)
        else:
            bag.add_item(item)
            bot.add_value(item)
            bot.inventory.remove(item)
            return


def coin_flip():
    """
    Include some randomness to the game by deciding who goes first each game
    :return: 0 for "heads", player goes first, 1 for "tails", bot goes first
    """
    if random.randint(0,1) == 0:
        return 0    # Player goes first
    else:
        return 1    # Bot goes first


def end_game(player, bot, bag):
    """
    Tally total scores from items loaded into the bag and declare the winner.

    :param player: Player object for retrieving total sum value
    :param bot: Bot object for retrieving total sum value
    :param bag: Bag object, currently unused. Will look to add an upacking function to show what is in the bag at game
                end.
    """
    print("Both players have passed! Lets look at the score!\n")
    loading_pause()
    print(f"Player total value in bag: {player.get_value()}\n")
    loading_pause()
    print(f"Bot total value in bag: {bot.get_value()}\n")
    if player.get_value() > bot.get_value():
        print("You win!\n\n")
    elif player.get_value() == bot.get_value():
        print("It was a tie!\n\n")
    else:
        print("Bot won!\n\n")


def item_select(player, bag):
    """
    Give the player options to view their total score or select an item currently in their possession. Checks to ensure
    item selected does not exceed bag weight. Also includes instructions to type 'pass' if no plays are possible.

    :param player: Player object to retrieve items in inventory and make a play.
    :param bag: Bag object to check weight and add item if proper item is selected.
    """
    print("Here are the items currently in your inventory...\n")
    player.check_inventory()
    print("Please input the number for the item you wish to add or type 'pass' if you want to pass\n")
    item_choice = input("--> ")
    if item_choice == 'pass':
        player.passed()
        return
    else:
        item_choice = int(item_choice) - 1
        item = player.inventory[item_choice]

    if (int(item.get_weight()) + bag.get_weight()) > bag.max_weight:
        print("That item is too big to fit in the bag. Please choose another item.\n")
        item_select(player, bag)
    else:
        bag.add_item(item)
        player.add_value(item)
        player.inventory.remove(item)


def loading_pause():
    """
    Visual representation of logic moving forward. Provide a break in the flow.
    """
    i = 0
    while i > 5:
        print(". ")
        time.sleep(1)
        i += 1


def menu_options():
    """
    Display of options available to player during their turn.
    """
    print("1. Add item to bag\n")
    print("2. Check total value of your items already in the bag.\n")
    print("3. Pass")


def start_game(player, bot):
    """
    Begin game, giving instructions on how to win. Initialize bag object.

    :param player: Player object for item selection and turn passing.
    :param bot: Bot object for bot plays
    """
    bag = Bag()
    bag.set_size(player, bot)
    print("To win the game, you must place items in the bag. Should the value of said items be greater than the \n")
    print("the value of your opponents items, you win! We will start with a coin toss to determine who goes first!\n")

    coin = coin_flip()
    if coin == 1:
        print("Bot will go first!\n\n")
        bot_play(bot, bag)

    while True:
        if player.pass_turn and bot.pass_turn:
            end_game(player, bot, bag)
            print("Returning to the main menu\n")
            loading_pause()
            break

        menu_options()
        choice = input("Please make a selection: ")
        if choice == '1':
            item_select(player, bag)
            bot_play(bot, bag)
        if choice == '2':
            print(player.get_value(), "\n")
        if choice == '3':
            player.passed()

