import queue 
from .BaseTree import BaseTree

class BL(BaseTree):
    """
    Implementação da Busca em Largura
    """
    def _search_solution(self):
        
        start = self.puzzle.initial_board.convert_to_tuple(self.puzzle.initial_board.board)
        pred = {}
        visited = []
        frontier = queue.Queue()
        frontier.put(start)
        
        while frontier.qsize() > 0:
            tmp = frontier.get()

            if tmp == self.puzzle.final_board.goal:
                return self._get_result(tmp, start, pred, 0,  True)

            if tmp not in visited:
                visited.append(tmp)
                tmpboard = self.puzzle.match(tmp)
                tmpboard.move_up()
                if self.puzzle.initial_board.convert_to_tuple(tmpboard.board) != tmp:
                    frontier.put(self.puzzle.initial_board.convert_to_tuple(tmpboard.board))
                    if not self.puzzle.initial_board.convert_to_tuple(tmpboard.board) in pred:
                        pred[self.puzzle.initial_board.convert_to_tuple(tmpboard.board)]=[tmp, 'up']

                
                tmpboard = self.puzzle.match(tmp)
                tmpboard.move_down()
                if self.puzzle.initial_board.convert_to_tuple(tmpboard.board) != tmp:
                    frontier.put(self.puzzle.initial_board.convert_to_tuple(tmpboard.board))
                    if not self.puzzle.initial_board.convert_to_tuple(tmpboard.board) in pred:
                        pred[self.puzzle.initial_board.convert_to_tuple(tmpboard.board)]=[tmp, 'down']

                        
                tmpboard = self.puzzle.match(tmp)
                tmpboard.move_right()
                if self.puzzle.initial_board.convert_to_tuple(tmpboard.board) != tmp:
                    frontier.put(self.puzzle.initial_board.convert_to_tuple(tmpboard.board))
                    if not self.puzzle.initial_board.convert_to_tuple(tmpboard.board) in pred:
                        pred[self.puzzle.initial_board.convert_to_tuple(tmpboard.board)]=[tmp, 'right']

                
                tmpboard = self.puzzle.match(tmp)
                tmpboard.move_left()
                if self.puzzle.initial_board.convert_to_tuple(tmpboard.board) != tmp:
                    frontier.put(self.puzzle.initial_board.convert_to_tuple(tmpboard.board))
                    if not self.puzzle.initial_board.convert_to_tuple(tmpboard.board) in pred:
                        pred[self.puzzle.initial_board.convert_to_tuple(tmpboard.board)]=[tmp, 'left']
            else:
                del tmp    
        self.pred = pred    
        
        raise Exception('There is no solution.')