import time
from .Player import Player

class MachinePlayerAbstract(Player):
    """ Computer Player controlled by an IA 
    """

    def __init__(self, color):
        """
        Constructor
        :param color: character entered in the grid for example: `o` or `x`
        :return:
        """
        super(MachinePlayerAbstract, self).__init__(color)
        self._type = "IA"
        self._difficulty = 5 #depth

    def get_move(self, grid):
        """
        Returns the best "move" (column index) calculated by IA
        :param grid: the current grid of the game
        :return: the best move found by IA (MinMax algorithm)
        """
        return self._get_best_move(grid)

    def _get_best_move(self, grid):
        pass

    def _find(self, depth, grid, curr_player_color):
        pass

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
        pass

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

    def _determine_color(self):
        if self._color == "x":
            return "o"
        else:
            return "x"

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
