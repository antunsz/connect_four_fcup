import time
import math
from .MachinePlayerAbstract import MachinePlayerAbstract

class MachinePlayerMonteCarlo(MachinePlayerAbstract):
    """ Computer Player controlled by an IA (MinMax algorithm)
    """
    def __init__(self, color):
        """
        Constructor
        :param color: character entered in the grid for example: `o` or `x`
        :return:
        """
        super(MachinePlayerMonteCarlo, self).__init__(color)
        self._type = "AlphaBeta Player"
        self.visited = []
        self.qtd_visited =[]

    def _get_best_move(self, grid):
        """
        Search and return the best "move" (column index)
        :param grid: the grid of the connect four
        :return best_move: the best "move" (column index)
        """
        # start time
        start_time = int(round(time.time() * 1000))
        # determine opponent's color
        opponent_color = self._determine_color()

        # enumerate all legal moves
        # will map legal move states to their alpha values
        legal_moves = {}
        # check if the move is legal for each column
        
        for col in range(len(grid)):
            if self._is_legal_move(col, grid):
                # simulate the move in column `col` for the current player
                tmp_grid = self._simulate_move(grid, col, self._color)
                legal_moves[col] = -self._find(self._difficulty - 1, tmp_grid, opponent_color)

        best_alpha = -99999999
        best_move = None
        moves = legal_moves.items()
        # search the best "move" with the highest `alpha` value
        for move, alpha in moves:
            if alpha >= best_alpha:
                best_alpha = alpha
                best_move = move

        end_time = int(round(time.time() * 1000))
        print("response time: {}".format(end_time - start_time))

        return best_move

    def _find(self, depth, grid, curr_player_color):
        """
        Searches in the tree at depth = `depth` till it's not equal to 0. This function is recursive
        :param depth: the current depth of the tree
        :param grid: a grid of the connect four
        :param curr_player_color: the color of the current player
        :return alpha: value calculated with an heuristic. It represent the value of a "move" (column index)
        """
        # enumerate all legal moves from this state
        legal_moves = []
        for i in range(len(grid)):
            if self._is_legal_move(i, grid):
                # simulate the move in column i for curr_player
                tmp_grid = self._simulate_move(grid, i, curr_player_color)
                legal_moves.append(tmp_grid)

        self.visited.append({depth:legal_moves[:]})
        if depth == 0 or len(legal_moves) == 0 or self._game_is_over(grid):
            # return the heuristic value of node
            return self._eval_game(depth, grid, curr_player_color)

        # determine opponent's color
        opp_player_color = self._determine_color()

        alpha = -99999999
        last_alpha = alpha
        for child in legal_moves:
            if child == None:
                print("child == None (search)")
            alpha = max(alpha, -self._find(depth - 1, child, opp_player_color))
            if last_alpha > alpha:
                return last_alpha      
        return alpha

    def _eval_game(self, depth, grid, player_color):
        """
        Evaluate the game with its grid
        :param depth: the depth of the tree
        :param grid: a grid of connect four
        :param player_color: the current player's color
        :return: alpha : value calculated with an heuristic. It represent the value of a "move" (column index)
        """
        if player_color == 'x':
            opp_color = 'o'
        else:
            opp_color = 'x'
        # get scores of human and IA player with theirs streaks
        ia_fours = self._find_streak(grid, player_color, 4)
        ia_threes = self._find_streak(grid, player_color, 3)
        ia_twos = self._find_streak(grid, player_color, 2)
        human_fours = self._find_streak(grid, opp_color, 4)
        human_threes = self._find_streak(grid, opp_color, 3)
        human_twos = self._find_streak(grid, opp_color, 2)
        # calculate and return the alpha
        if human_fours > 0:
            return -100000 - depth
        else:
            X = (ia_fours * 100000 + ia_threes * 100 + ia_twos * 10) - (human_threes * 100 + human_twos * 10) + depth
            #todo: não consegui terminar a implementação
            return X+0.01*math.sqrt(2*math.log())
