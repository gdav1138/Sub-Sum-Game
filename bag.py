from player import Player
from bot import Bot
import items

class Bag:
    def __init__(self):
        self.max_weight = 0
        self.items = []
        self.current_weight = 0

    def set_size(self, player, bot):
        """
        Determine the total weight the bag can hold based on items in play at the start of the game.

        :param player: Player object for retrieving items held by the player.
        :param bot: Player object for retrieving items held by the bot.
        """
        bag_weight = 0
        for item in player.inventory:
            bag_weight += int(item.get_weight())
        for item in bot.inventory:
            bag_weight += int(item.get_weight())
        self.max_weight = bag_weight/2

    def get_weight(self):
        """
        Retrieve the current weight of the bag. Used to assist in ensuring items to be added don't exceed max_weight.
        :return: self.current_weight - current weight of items held in the bag.
        """
        return self.current_weight

    def add_item(self, item):
        """
        Add the item passed in to the bag, placing it in the items list and increasing current_weight be the item's
        weight value.
        :param item:
        :return:
        """
        self.items.append(item)
        self.current_weight += int(item.get_weight())