from utils.Board import Board

class Puzzle:
    """
    Classe que representa o jogo
    """
    def __init__(self, matrix_width, initial_config, final_config):
        self.initial_config = initial_config
        self.final_config = final_config
        self.matrix_width = matrix_width
        self.initial_board = Board(initial_config, matrix_width)
        self.final_board = Board(final_config, matrix_width)
        self.points = 0

    def match(self, copy):
        a = Board()
        a.board = copy
        for row in range(0, self.matrix_width):
            for col in range(0, self.matrix_width):
                if a.board[row][col] == 0:
                    a.empty = [row, col]
        result = []
        for i in a.board:
            result.append(list(i))
        a.board = result
        return a