from utils.Game import Game
from utils.HumanPlayer import HumanPlayer
from utils.MachinePlayerMinMax import MachinePlayerMinMax
from utils.MachinePlayerAlphaBeta import MachinePlayerAlphaBeta
from utils.MachinePlayerMonteCarlo import MachinePlayerMonteCarlo

def init_game():
    """Inicia o jogo
    """
    
    
    menu_choice = 1
    while menu_choice == 1:
        # start the game
        print("Tipo de Jogo")
        print("1 - Humano vs MinMax")
        print("2 - Humano vs AlphaBeta")
        print("3 - Humano vs MonteCarlo")
        print("4 - Quit")
        game_choice = int(input("choice : ")) 
        game = _choose_game(game_choice)
        game.start_new()
        # menu
        print("Menu")
        print("1 - Play again")
        print("2 - Quit")
        menu_choice = int(input("choice : "))        


def _choose_game(game_choice):
        if game_choice == 1:
                return Game(HumanPlayer, MachinePlayerMinMax)
        elif game_choice == 2:
                return Game(HumanPlayer, MachinePlayerAlphaBeta)
        elif game_choice == 3:
                return Game(Human, MachinePlayerMonteCarlo)
if __name__ == "__main__":
    init_game()
