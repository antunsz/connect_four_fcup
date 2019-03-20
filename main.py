from utils.Checker import Checker
from utils.Puzzle import Puzzle
from utils.BL import BL
from utils.BP import BP
from utils.BIP import BIP
from utils.AStar import AStar
from utils.Greedy import Greedy
import copy

#estado de partida onde existe uma solução
initial_config = [1,2,3,4,5,6,8,12,13,9,0,7,14,11,10,15]

#estado de partida onde não existe solução
initial_config2 = [1,2,3,4,13,68,12,5,9,0,7,14,11,10,15]

#estado teste
init_config_t1 = [1,2,3,4,5,6,7,8,9,10,11,0,13,14,15,12]
final_config_t1 = [9, 5, 12, 7, 14, 13, 0, 8, 1, 3, 2, 4, 6, 10, 15, 11]


#estado final
final_config =   [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]

#objeto puzzle
puzzle = Puzzle(4, initial_config, final_config)

#objecto que checará se o puzzle possui solução ou não
checker = Checker(puzzle)

#método que inicial o jogo
def init_game():
    if checker.there_is_no_solution():
        print("Sem solução")
    else:
        print("-"*10+"Busca em Largura"+"-"*10)
        bl = BL(copy.deepcopy(puzzle))
        bl.search_solution()
        bl.show_solution()
        bl.solve()
        bl.show_time()
        bl.show_size()
        bl.show_depth()

        print("-"*10+"Busca em Profundidade"+"-"*10)
        bp = BP(copy.deepcopy(puzzle))
        bp.search_solution()
        bp.show_solution()
        bp.solve()
        bp.show_time()      
        bp.show_size()
        bp.show_depth()

        print("-"*10+"Busca Iterativa em Profundidade"+"-"*10)
        bip = BIP(copy.deepcopy(puzzle), limit=15000)
        bip.search_solution()
        bip.show_solution()
        bip.solve()
        bip.show_time()
        bip.show_size()
        bip.show_depth()

        print("-"*10+"Busca Informada Greedy - Heurística: Peças fora de Lugar"+"-"*10)
        gd = Greedy(copy.deepcopy(puzzle), heuristic="NPFL")
        gd.search_solution()
        gd.show_solution()
        gd.solve()
        gd.show_time()
        gd.show_size()
        gd.show_depth()

        print("-"*10+"Busca Informada Greedy - Heurística: Manhatam Distance"+"-"*10)
        gd = Greedy(copy.deepcopy(puzzle), heuristic="Manhatam")
        gd.search_solution()
        gd.show_solution()
        gd.solve()
        gd.show_time()
        gd.show_size()
        gd.show_depth()

        print("-"*10+"Busca Informada A* - Heurística: Peças fora de Lugar"+"-"*10)
        astar = AStar(copy.deepcopy(puzzle), heuristic="NPFL")
        astar.search_solution()
        astar.show_solution()
        astar.solve()
        astar.show_time()
        astar.show_size()
        astar.show_depth()

        print("-"*10+"Busca Informada A* - Heurística: Manhatam Distance"+"-"*10)
        astar = AStar(copy.deepcopy(puzzle), heuristic="Manhatam")
        astar.search_solution()
        astar.show_solution()
        astar.solve()
        astar.show_time()
        astar.show_size()
        astar.show_depth()

        

if __name__ == "__main__":
    assert len(initial_config) == len(final_config), "Os tabuleiros devem possuir o mesmo tamanho."
    
    init_game()
