class Player:
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
        print("\n")

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

