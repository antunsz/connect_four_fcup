import os
import random


class Game:
    def __init__(self, player1, player2, width=7, height=6, board_array=[]):
        self._width = width
        self._height = height
        self._player_avatars = ["x", "o"]
        
        self._grid = None
        self._round = 1
        self._finished = False
        self._winner = None
        self._current_player = None
        self._players = [None, None]
        self._players[0] = player1(self._player_avatars[0])
        self._players[1] = player2(self._player_avatars[1])

        for i in range(2):
            print("\t{} joga com {}".format(self._players[i]._type, self._player_avatars[i]))
        print('*'*10)
        input('\tPrecione ENTER para iniciar o jogo')
        print('*'*10)

        self.start_new()        
        # display players's status
        
    def start_game(self):
        """ Start a game
        """
        while not self._finished:
            self._next_move()

    def start_new(self):
        """ Start a new game
        """
        #clear screen
        os.system(['clear', 'cls'][os.name == 'nt'])
        # reset game status
        self._round = 1
        self._finished = False
        self._winner = None
        # choose the first player randomly
        self._current_player = self._players[random.randint(0, 1)]
        # clear grid with white spaces
        self._grid = []
        for i in range(self._height):
            self._grid.append([])
            for j in range(self._width):
                self._grid[i].append(' ')

        # start a new game
        self.start_game()

    def _switch_player(self):
        """ Switch the current player
        """
        if self._current_player == self._players[0]:
            self._current_player = self._players[1]
        else:
            self._current_player = self._players[0]

    def _next_move(self):
        """ Handle the next move
        """
        # get the "move" (column) that the player played
        self._print_state()
        column = self._current_player.get_move(self._grid)
        # search the available line in the selected column
        for i in range(self._height - 1, -1, -1):
            if self._grid[i][column] == ' ':
                # set the color in the grid
                self._grid[i][column] = self._current_player._color
                self._check_status()
                self._print_state()
                # swith player
                self._switch_player()
                # increment the round
                self._round += 1
                return

        # column selected is full
        print("Esta coluna está cheia. Selecione outra coluna.")
        return

    def _check_status(self):
        """ Check and update the status of the game
        """
        if self._is_full():
            self._finished = True
        elif self._are_someone_won():
            self._finished = True
            self._winner = self._current_player

    def _is_full(self):
        """
        Check if the grid is full
        :return: Boolean
        """
        # the number of round can't be superior to the number of case of the grid
        return self._round > self._height * self._width

    def _are_someone_won(self):
        """
        Check if there is a connect four in the grid
        :return: Boolean
        """
        # for each box of the grid
        for i in range(self._height - 1, -1, -1):
            for j in range(self._width):
                if self._grid[i][j] != ' ':
                    # check for vertical connect four
                    if self._find_vertical_four(i, j):
                        return True

                    # check for horizontal connect four
                    if self._find_horizontal_four(i, j):
                        return True

                    # check for diagonal connect four
                    if self._find_diagonal_four(i, j):
                        return True

        return False

    def _find_vertical_four(self, row, col):
        """
        Check for vertical connect four starting at index [row][col] of the grid
        :param row: row of the grid
        :param col: column of the grid
        :return: Boolean
        """
        consecutive_count = 0

        if row + 3 < self._height:
            for i in range(4):
                if self._grid[row][col] == self._grid[row + i][col]:
                    consecutive_count += 1
                else:
                    break
            # define the winner
            if consecutive_count == 4:
                if self._players[0]._color == self._grid[row][col]:
                    self._winner = self._players[0]
                else:
                    self._winner = self._players[1]
                return True
        return False

    def _find_horizontal_four(self, row, col):
        """
        Check for horizontal connect four starting at index [row][col] of the grid
        :param row: row of the grid
        :param col: column of the grid
        :return: Boolean
        """
        consecutive_count = 0

        if col + 3 < self._width:
            for i in range(4):
                if self._grid[row][col] == self._grid[row][col + i]:
                    consecutive_count += 1
                else:
                    break

            # define the winner
            if consecutive_count == 4:
                if self._players[0]._color == self._grid[row][col]:
                    self._winner = self._players[0]
                else:
                    self._winner = self._players[1]
                return True

        return False

    def _find_diagonal_four(self, row, col):
        """
        Check for diagonal connect four starting at index [row][col] of the grid
        :param row: row of the grid
        :param col: column of the grid
        :return: Boolean
        """
        consecutive_count = 0
        # check positive slope
        if row + 3 < self._height and col + 3 < self._width:
            for i in range(4):
                if self._grid[row][col] == self._grid[row + i][col + i]:
                    consecutive_count += 1
                else:
                    break

            # define the winner
            if consecutive_count == 4:
                if self._players[0]._color == self._grid[row][col]:
                    self._winner = self._players[0]
                else:
                    self._winner = self._players[1]
                return True

        consecutive_count = 0
        # check negative slope
        if row - 3 >= 0 and col + 3 < self._width:
            for i in range(4):
                if self._grid[row][col] == self._grid[row - i][col + i]:
                    consecutive_count += 1
                else:
                    break

            # define the winner
            if consecutive_count == 4:
                if self._players[0]._color == self._grid[row][col]:
                    self._winner = self._players[0]
                else:
                    self._winner = self._players[1]
                return True

        return False

    def _print_state(self):
            """ Print state of the game (round, grid, winner)
            """
            # cross-platform clear screen
            os.system(['clear', 'cls'][os.name == 'nt'])
            board = ''
            # print the round
            board = " Round: " + str(self._round)
            board += "\n"
            # print the grid
            for i in range(self._height):
                for j in range(self._width):
                    board += "| " + str(self._grid[i][j])
                board += "|\n"
            board += "\t\n"
            # print the bottom of the grid with columns index
            for k in range(self._width):
                board += "  _"
            board += "\n"
            for k in range(self._width):
                board += "  %d" % (k + 1)
            board += "\n"
            print(board)
            # print final message when the game is finished
            if self._finished:
                print("Game Over!")
                if self._winner != None:
                    print(str(self._winner._type) + " venceu!")
                else:
                    print("Game is a draw")