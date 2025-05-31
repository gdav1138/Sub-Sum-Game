import random

class Bot:
    def __init__(self):
        self.value = 0
        self.inventory = []
        self.pass_turn = False

    def add_value(self, item):
        """
        Track the total sum value of items added to the bag by the bot.

        :param item: Item added to the bag.
        """
        self.value += int(item.get_value())

    def check_inventory(self):
        """
        Retrieve items currently held in inventory. Prints the details of each item in the output window.
        """
        i = 1
        for item in self.inventory:
            print(f"{i}, {item.get_name()} - Value: {item.get_value()}, Weight: {item.get_weight()}")
            i += 1

    def get_value(self):
        """
        Retrieve current total sum value of items added to the bag.

        :return: self.value - total value
        """
        return self.value

    def load_inventory(self, item):
        """
        Add item objects to inventory list for later retrieval

        :param item: Item object passed in.
        """
        self.inventory.append(item)

    def passed(self):
        """
        Flag used to know when the player has passed.
        """
        self.pass_turn = True


class GreedyBot(Bot):
    """
    Branch of Bot class, used to differentiate plays. This particular class is for
    "Greedy" plays, meant to only select the most valuable item within bot's inventory.
    """
    def play(self):
        return max(self.inventory, key=lambda x: x.value)

class RandomBot(Bot):
    """
    Branch of Bot class, used to differentiate plays. This particular class is for
    "Random" plays, meant to select an item at random from within bot's inventory.
    """
    def play(self):
        return random.choice(self.inventory)
