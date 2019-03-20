from collections import deque 
from .BaseTree import BaseTree

class AStar(BaseTree):
    """
    Implementação da busca A*
    """
    def _search_solution(self):
        start = self.puzzle.initial_board.convert_to_tuple(self.puzzle.initial_board.board)
        pred = {}
        visited = []
        frontier = deque([])
        frontier.appendleft(start)
        depth = 0
        heuristic = self._get_heuristic()
        #enquanto ainda existirem nós para serem visitados
        while len(frontier) > 0:
            tmp = frontier.pop()            
            layer = []
            score_sum = []            
            #se a variável tmp for igual à configuração final
            if tmp == self.puzzle.final_board.goal:
                return self._get_result(tmp, start, pred, depth, False)

            if depth < self.limit:
                if tmp not in visited:
                    visited.append(tmp)                
                    tmpboard = self.puzzle.match(tmp)
                    tmpboard.move_up()
                    if self.puzzle.initial_board.convert_to_tuple(tmpboard.board) != tmp:
                        score = heuristic(tmpboard)
                        try:
                            score += score_sum[0]
                            score_sum[0] += 1
                        except:
                            score += 1
                            score_sum.append(1)
                        score_sum[0] = score    
                        layer.append((score, self.puzzle.initial_board.convert_to_tuple(tmpboard.board)))
                        if not self.puzzle.initial_board.convert_to_tuple(tmpboard.board) in pred:
                            pred[self.puzzle.initial_board.convert_to_tuple(tmpboard.board)]=[tmp, 'up']
                    
                    
                    tmpboard = self.puzzle.match(tmp)
                    tmpboard.move_down()
                    if self.puzzle.initial_board.convert_to_tuple(tmpboard.board) != tmp:
                        score = heuristic(tmpboard)
                        try:
                            score += score_sum[1]
                            score_sum[1] += 1
                        except:
                            score += 1
                            score_sum.append(1)
                        layer.append((score, self.puzzle.initial_board.convert_to_tuple(tmpboard.board)))
                        if not self.puzzle.initial_board.convert_to_tuple(tmpboard.board) in pred:
                            pred[self.puzzle.initial_board.convert_to_tuple(tmpboard.board)]=[tmp, 'down']

                            
                    tmpboard = self.puzzle.match(tmp)
                    tmpboard.move_right()
                    if self.puzzle.initial_board.convert_to_tuple(tmpboard.board) != tmp:
                        score = heuristic(tmpboard)
                        try:
                            score += score_sum[2]
                            score_sum[2] += 1
                        except:
                            score += 1
                            score_sum.append(1)
                        layer.append((score, self.puzzle.initial_board.convert_to_tuple(tmpboard.board)))
                        if not self.puzzle.initial_board.convert_to_tuple(tmpboard.board) in pred:
                            pred[self.puzzle.initial_board.convert_to_tuple(tmpboard.board)]=[tmp, 'right']

                    
                    tmpboard = self.puzzle.match(tmp)
                    tmpboard.move_left()
                    if self.puzzle.initial_board.convert_to_tuple(tmpboard.board) != tmp:
                        score = heuristic(tmpboard)
                        try:
                            score += score_sum[3]
                            score_sum[3] += 1
                        except:
                            score += 1
                            score_sum.append(1)
                        layer.append((score, self.puzzle.initial_board.convert_to_tuple(tmpboard.board)))
                        if not self.puzzle.initial_board.convert_to_tuple(tmpboard.board) in pred:
                            pred[self.puzzle.initial_board.convert_to_tuple(tmpboard.board)]=[tmp, 'left']
                        
                    [frontier.appendleft(element[1]) for element in sorted(layer[:], key=lambda x: x[0]) ]
                
                depth = self._get_depth(start, pred, tmp)
                del tmp
                
        self.pred = pred 

        return False
