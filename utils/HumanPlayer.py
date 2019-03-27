from .Player import Player

class HumanPlayer(Player):
    """ Human Player
    """

    def __init__(self, color):
        """
        Constructor
        :param color: character entered in the grid for example: `o` or `x`
        """
        super(HumanPlayer, self).__init__(color)
        self._type = "Human"

    def get_move(self, grid):
        """
        Ask and return the column entered by the user
        :param grid: list
        """
        column = None
        while column == None:
            try:
                column = int(input("Sua vez: ")) - 1
            except ValueError:
                column = None
            if 0 <= column <= 6:
                return column
            else:
                column = None
                print("Por favor, selecione um número entre 1 e 7")
