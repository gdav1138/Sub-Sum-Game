def welcome():
    """
    Read welcome instructions to introduce player to the game.
    """
    with open("welcome_instructions.txt", "r") as file:
        content = file.read()
        print(content, "\n\n")

def menu():
    """
    Provide a menu selection of available options to start the game with a certain opponent. Also give option to exit
    the game.
    """
    print("Available opponents: \n")
    print("1. RandomBot\n")
    print("2. GreedyBot\n")
    print("3. Exit Game\n")
