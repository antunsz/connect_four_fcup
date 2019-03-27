import time
from .Player import Player

class MachinePlayer(Player):
    """ Computer Player controlled by an IA (MinMax algorithm)
    """
    _DIFFICULTY = 5

    def __init__(self, color):
        """
        Constructor
        :param color: character entered in the grid for example: `o` or `x`
        :return:
        """
        super(MachinePlayer, self).__init__(color)
        self._type = "IA"

    def get_move(self, grid):
        """
        Returns the best "move" (column index) calculated by IA
        :param grid: the current grid of the game
        :return: the best move found by IA (MinMax algorithm)
        """
        return self._get_best_move(grid)

    def _get_best_move(self, grid):
        """
        Search and return the best "move" (column index)
        :param grid: the grid of the connect four
        :return best_move: the best "move" (column index)
        """
        # start time
        start_time = int(round(time.time() * 1000))
        # determine opponent's color
        if self._color == "x":
            human_color = "o"
        else:
            human_color = "x"

        # enumerate all legal moves
        # will map legal move states to their alpha values
        legal_moves = {}
        # check if the move is legal for each column
        
        for col in range(len(grid)):
            if self._is_legal_move(col, grid):
                # simulate the move in column `col` for the current player
                tmp_grid = self._simulate_move(grid, col, self._color)
                legal_moves[col] = -self._find(self._DIFFICULTY - 1, tmp_grid, human_color)

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

        if depth == 0 or len(legal_moves) == 0 or self._game_is_over(grid):
            # return the heuristic value of node
            return self._eval_game(depth, grid, curr_player_color)

        # determine opponent's color
        if curr_player_color == 'x':
            opp_player_color = 'o'
        else:
            opp_player_color = 'x'

        alpha = -99999999
        for child in legal_moves:
            if child == None:
                print("child == None (search)")
            alpha = max(alpha, -self._find(depth - 1, child, opp_player_color))
        return alpha

    def _is_legal_move(self, column, grid):
        """ Boolean function to check if a move (column) is a legal move
        """
        for i in range(len(grid) - 1, -1, -1):
            if grid[i][column] == ' ':
                # once we find the first empty, we know it's a legal move
                return True

        # if we get here, the column is full
        return False

    def _game_is_over(self, grid):
        if self._find_streak(grid, 'x', 4) > 0:
            return True
        elif self._find_streak(grid, 'o', 4) > 0:
            return True
        else:
            return False

    def _simulate_move(self, grid, column, color):
        """
        Simulate a "move" in the grid `grid` by the current player with its color `color.
        :param grid: a grid of connect four
        :param column: column index
        :param color: color of a player
        :return tmp_grid: the new grid with the "move" just added
        """
        tmp_grid = [x[:] for x in grid]
        for i in range(len(grid) - 1, -1, -1):
            if tmp_grid[i][column] == ' ':
                tmp_grid[i][column] = color
                return tmp_grid

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
            return (ia_fours * 100000 + ia_threes * 100 + ia_twos * 10) - (human_threes * 100 + human_twos * 10) + depth

    def _find_streak(self, grid, color, streak):
        """
        Search streaks of a color in the grid
        :param grid: a grid of connect four
        :param color: color of a player
        :param streak: number of consecutive "color"
        :return count: number of streaks founded
        """
        count = 0
        # for each box in the grid...
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # ...that is of the color we're looking for...
                if grid[i][j] == color:
                    # check if a vertical streak starts at index [i][j] of the grid game
                    count += self._find_vertical_streak(i, j, grid, streak)

                    # check if a horizontal streak starts at index [i][j] of the grid game
                    count += self._find_horizontal_streak(i, j, grid, streak)

                    # check if a diagonal streak starts at index [i][j] of the grid game
                    count += self._find_diagonal_streak(i, j, grid, streak)
        # return the sum of streaks of length 'streak'

        return count

    def _find_vertical_streak(self, row, col, grid, streak):
        """
        Search vertical streak starting at index [row][col] in the grid
        :param row: row the grid
        :param col: column of the grid
        :param grid: a grid of connect four
        :param streak: number of "color" consecutive
        :return: 0: no streak found, 1: streak founded
        """
        consecutive_count = 0
        if row + streak - 1 < len(grid):
            for i in range(streak):
                if grid[row][col] == grid[row + i][col]:
                    consecutive_count += 1
                else:
                    break

        if consecutive_count == streak:
            return 1
        else:
            return 0

    def _find_horizontal_streak(self, row, col, grid, streak):
        """
        Search horizontal streak starting at index [row][col] in the grid
        :param row: row the grid
        :param col: column of the grid
        :param grid: a grid of connect four
        :param streak: number of "color" consecutive
        :return: 0: no streak found, 1: streak founded
        """
        consecutive_count = 0
        if col + streak - 1 < len(grid):
            for i in range(streak):
                if grid[row][col] == grid[row][col + i]:
                    consecutive_count += 1
                else:
                    break

        if consecutive_count == streak:
            return 1
        else:
            return 0

    def _find_diagonal_streak(self, row, col, grid, streak):
        """
        Search diagonal streak starting at index [row][col] in the grid
        It check positive and negative slope
        :param row: row the grid
        :param col: column of the grid
        :param grid: a grid of connect four
        :param streak: number of "color" consecutive
        :return total: number of streaks founded
        """
        total = 0
        # check for diagonals with positive slope
        consecutive_count = 0
        if row + streak - 1 < len(grid) and col + streak - 1 < len(grid[0]):
            for i in range(streak):
                if grid[row][col] == grid[row + i][col + i]:
                    consecutive_count += 1
                else:
                    break

        if consecutive_count == streak:
            total += 1

        # check for diagonals with negative slope
        consecutive_count = 0
        if row - streak + 1 >= 0 and col + streak - 1 < len(grid):
            for i in range(streak):
                if grid[row][col] == grid[row - i][col + i]:
                    consecutive_count += 1
                else:
                    break

        if consecutive_count == streak:
            total += 1

        return total
