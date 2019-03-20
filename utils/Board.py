class Board:
    def __init__(self, board_array=[], width=4):
        # 4 by 4 board
        # self.board is the goal board when first initialized
        self.board = self._generate_matrix(width, board_array)
        # self.goal is later used as a comparison to solve the mixed board
        self.goal = [] 
        for i in self.board:
            self.goal.append(tuple(i))
        self.goal = tuple(self.goal)
        # self.empty is the position of empty block TODO
        self.empty = self._locate_blank()

    def _generate_matrix(self, matrix_width, array):
        matrix = []
        count = 0
        aux = []
        for p, i in enumerate(array):
            if count < matrix_width:
                aux.append(i)
                count += 1
                if p+1 == len(array):
                    matrix.append(aux[:])
            else:
                matrix.append(aux[:])
                aux = []
                aux.append(i)
                count = 1
        return matrix

    def _locate_blank(self, matrix=None):
        if not matrix:
            matrix=self.board
            
        for i, row in enumerate(matrix):
            for j, element in enumerate(row):
                if element == 0:
                    return [i,j]

    def convert_to_tuple(self, ar):
        result = []
        for i in ar:
            result.append(tuple(i))
        return tuple(result)

    def convert_to_list(self, tup):
        result = []
        for i in tup:
            result.append(list(i))
        return result

    def move_up(self): # move empty block up
        try:
            if self.empty[0] != 0:
                tmp = self.board[self.empty[0]-1][self.empty[1]]
                self.board[self.empty[0]-1][self.empty[1]] = 0
                self.board[self.empty[0]][self.empty[1]] = tmp
                self.empty = [self.empty[0]-1, self.empty[1]]
        except IndexError:
            pass

    def move_down(self): # move empty block down
        try:
            tmp = self.board[self.empty[0]+1][self.empty[1]]
            self.board[self.empty[0]+1][self.empty[1]] = 0
            self.board[self.empty[0]][self.empty[1]] = tmp
            self.empty = [self.empty[0]+1, self.empty[1]]
        except IndexError:
            pass

    def move_right(self): # move empty block right
        try:
            tmp = self.board[self.empty[0]][self.empty[1]+1]
            self.board[self.empty[0]][self.empty[1]+1] = 0
            self.board[self.empty[0]][self.empty[1]] = tmp
            self.empty = [self.empty[0], self.empty[1]+1]
        except IndexError:
            pass

    def move_left(self): # move empty block left
        try:
            if self.empty[1] != 0:
                tmp = self.board[self.empty[0]][self.empty[1]-1]
                self.board[self.empty[0]][self.empty[1]-1] = 0
                self.board[self.empty[0]][self.empty[1]] = tmp
                self.empty = [self.empty[0], self.empty[1]-1]
        except IndexError:
            pass


    def __repr__(self):
        string = ''
        for row in self.board:
            for num in row:
                if len(str(num)) == 1:
                    string += '   ' + str(num)
                elif len(str(num)) > 1:
                    string += '  ' + str(num)
            string += '\n'
        return string