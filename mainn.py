from utils.Game import Game

def init_game():
    """Inicia o jogo
    """
    game = Game()
    menu_choice = 1
    while menu_choice == 1:
        # start the game
        game.start_new()
        # menu
        print("Menu")
        print("1 - Play again")
        print("2 - Quit")
        menu_choice = int(input("choice : "))        


if __name__ == "__main__":
    init_game()
