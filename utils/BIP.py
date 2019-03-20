from collections import deque 
import copy
from .BP import BP
from .BaseTree import BaseTree

class BIP(BaseTree):
    """
    Implementação de Busca Iterativa em Profundidade
    """
    def _search_solution(self):
        for i in range(1,self.limit):
            print("Buscando até a profundidade:", i, end="\r")
            result, bp = self._do_BP(i)
            if result:
                print()
                self.pred = bp.pred
                self.solution = result
                self.depth = bp.depth
                break

    def _do_BP(self, limit):
        bp = BP(copy.copy(self.puzzle), limit=limit)
        return bp._search_solution(), bp
       
