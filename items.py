class Items:
    def __init__(self, name, value, weight):
        """
        Init for each item object to be created.

        :param name: Name of item.
        :param value: Value of item.
        :param weight: Weight of item.
        """
        self.name = name
        self.value = value
        self.weight = weight

    def get_name(self):
        """
        Retrieve the name of the object.

        :return: self.name - object's name.
        """
        return self.name

    def get_value(self):
        """
        Retrieve the value of the object.

        :return: self.value - object's value.
        """
        return self.value

    def get_weight(self):
        """
        Retrieve the weight of the object.

        :return: self.weight - object's weight.
        """
        return self.weight

