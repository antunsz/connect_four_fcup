import queue 
import timeit
import sys

class BaseTree:    
    """
    Classe com os métodos básicos para a implementação das buscas.
    """
    def __init__(self, puzzle, limit=1000000, heuristic = None):
        self.puzzle = puzzle        #objeto tipo puzzle
        self.pred = None            #onde ficam salvos os nós expandidos
        self.frontier = None        #onde ficam os nós à serem visitados
        self.solution = None        #onde fica salva a solução encontrada na busca
        self.time = None            #tempo de execução da busca
        self.limit = limit          #limite de profundidade, por padrão será 1000000
        self.depth = 0              #profundidade na qual foi encontrada a solução
        self.heuristic = heuristic  #heurística selecionada

    def search_solution(self):
        """
        Método que executa a busca e conta o tempo de execução
        """
        self.time = timeit.timeit(self._search_solution, number=1)

    def _search_solution(self):
        """
        Método à ser implementado nas classes que herdam BaseTree
        """
        pass

    def show_solution(self):
        """
        Mostra os passos para a solução
        """
        print("Solução ótima:",self.solution)

    def show_time(self):
        """
        Mostra o tempo gasto para encontrar a solução
        """
        print("Tempo: "+ str(self.time) + " s" )

    def show_size(self):
        """
        Mostra o tamanho em bytes  do conjunto de nós utilizados até encontrar a solução
        """
        print("Espaço: "+str(self._get_size(self.pred))+ " bytes")

    def show_depth(self):
        """
        Mostra a profundidade atingida até encontrar a solução
        """
        print("Profundidade: "+str(self.depth)+ " camadas")

    def solve(self):
        """
        Resolve o tabuleiro, passo à passo, imprimindo na tela cada jogada
        """
        if not self.solution:
            print("A busca ainda não foi executada. hint: utilize o método .search_solution()")
        else:
            tmp_board = self.puzzle.initial_board
            print("---Resolução passo à passo---")
            for step in self.solution:
                print("Movimento do espaço em branco:", step)
                self._control_board(tmp_board, step)
                print(tmp_board)

    def _get_depth(self, start, pred, tmp):
        """
        Retorna em qual profundidade se está, apartir do nó recebido
        """
        path = []
        while tmp != start:
            path.append(pred[tmp][1])
            tmp = pred[tmp][0]
        return len(path)

    def _get_size(self, obj, seen=None):
        """
        Retorna o tamanho do objeto recebido
        """
        size = sys.getsizeof(obj)
        if seen is None:
            seen = set()
        obj_id = id(obj)
        if obj_id in seen:
            return 0
        seen.add(obj_id)
        if isinstance(obj, dict):
            size += sum([self._get_size(v, seen) for v in obj.values()])
            size += sum([self._get_size(k, seen) for k in obj.keys()])
        elif hasattr(obj, '__dict__'):
            size += self._get_size(obj.__dict__, seen)
        elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
            size += sum([self._get_size(i, seen) for i in obj])
        return size

    def _get_heuristic(self):
        """
        Retorna método selecionado para heurística
        """
        if self.heuristic == "NPFL":
            return self._get_NPFL
        elif self.heuristic == "Manhatam":
            return self._get_manhatam_distance
    
    def _get_NPFL(self, tmpboard):
        """
        Calcula a quantidade de peças fora do lugar
        """
        return self._number_out_of_place(self.puzzle.initial_board.convert_to_list(tmpboard.board),
                                        self.puzzle.initial_board.convert_to_list(self.puzzle.final_board.goal))

    def _get_manhatam_distance(self, tmpboard):
        """
        Calcula a manhatam distance do estado recebido
        """
        return self._manhattan_distance(self.puzzle.initial_board.convert_to_list(tmpboard.board),
                                        self.puzzle.initial_board.convert_to_list(self.puzzle.final_board.goal))

    def _number_out_of_place(self, current_config, final_config):
        return len([i for i, value in enumerate(current_config) if value != final_config[i]])

    def _manhattan_distance(self, current_config, final_config):
        list_1 = [x for i in current_config for x in i]
        list_2 = [x for i in final_config for x in i]
        return sum([abs(value - list_2[i]) for i, value in enumerate(list_1)])

    def _get_result(self, tmp, start, pred, depth, is_BL=True):
        """
        Retorna o conjunto de passos desde a raiz até chegar no nó recebido
        """
        path = []
        while tmp != start:
            path.append(pred[tmp][1])
            tmp = pred[tmp][0]
        self.solution = path[::-1]
        if is_BL:
            self.depth = len(path[::-1])
        else:
            self.depth = depth
        self.pred = pred
        return path[::-1]

    def _control_board(self, board, step):
        """
        Simula as jogadas no tabuleiro
        """
        if step == 'up':
            board.move_up()
        elif step == 'down':
            board.move_down()
        elif step == 'left':
            board.move_left()
        elif step == 'right':
            board.move_right()
        else:
            print("Passo não reconhecido.")    

