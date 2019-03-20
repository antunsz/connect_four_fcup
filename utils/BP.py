from collections import deque
from .BaseTree import BaseTree
import timeit
import sys
import math 

class BP(BaseTree):
    """
    Implementação da busca em profundidade
    """
    def _search_solution(self):
        start = self.puzzle.initial_board.convert_to_tuple(self.puzzle.initial_board.board)
        pred = {}
        visited = []
        frontier = deque([])
        frontier.appendleft(start)
        
        depth = 0
        while len(frontier) > 0:
            tmp = frontier.pop()            
            layer = []            
            
            if tmp == self.puzzle.final_board.goal:
                return self._get_result(tmp, start, pred, depth, False)

            if depth < self.limit:
                if tmp not in visited:
                    visited.append(tmp)                
                    tmpboard = self.puzzle.match(tmp)
                    tmpboard.move_up()
                    if self.puzzle.initial_board.convert_to_tuple(tmpboard.board) != tmp:
                        layer.append(self.puzzle.initial_board.convert_to_tuple(tmpboard.board))
                        if not self.puzzle.initial_board.convert_to_tuple(tmpboard.board) in pred:
                            pred[self.puzzle.initial_board.convert_to_tuple(tmpboard.board)]=[tmp, 'up']
                    
                    
                    tmpboard = self.puzzle.match(tmp)
                    tmpboard.move_down()
                    if self.puzzle.initial_board.convert_to_tuple(tmpboard.board) != tmp:
                        layer.append(self.puzzle.initial_board.convert_to_tuple(tmpboard.board))
                        if not self.puzzle.initial_board.convert_to_tuple(tmpboard.board) in pred:
                            pred[self.puzzle.initial_board.convert_to_tuple(tmpboard.board)]=[tmp, 'down']

                            
                    tmpboard = self.puzzle.match(tmp)
                    tmpboard.move_right()
                    if self.puzzle.initial_board.convert_to_tuple(tmpboard.board) != tmp:
                        layer.append(self.puzzle.initial_board.convert_to_tuple(tmpboard.board))
                        if not self.puzzle.initial_board.convert_to_tuple(tmpboard.board) in pred:
                            pred[self.puzzle.initial_board.convert_to_tuple(tmpboard.board)]=[tmp, 'right']

                    
                    tmpboard = self.puzzle.match(tmp)
                    tmpboard.move_left()
                    if self.puzzle.initial_board.convert_to_tuple(tmpboard.board) != tmp:
                        layer.append(self.puzzle.initial_board.convert_to_tuple(tmpboard.board))
                        if not self.puzzle.initial_board.convert_to_tuple(tmpboard.board) in pred:
                            pred[self.puzzle.initial_board.convert_to_tuple(tmpboard.board)]=[tmp, 'left']
                    
                    [frontier.appendleft(node) for node in list(reversed(layer[:]))]
                depth = self._get_depth(start, pred, tmp)
                del tmp
                
        self.pred = pred 

        return False