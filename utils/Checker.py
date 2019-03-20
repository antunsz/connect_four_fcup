class Checker:
    """
    Classe que verifica a resolubilidade do problema.
    Se ambos configuração inicial e configuração final são solucionáveis,
    então é possível chegar na configuração final apartir da configuração inicial.
    """
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def _check_grid_position(self, config):
        linha = 1
        count = 1
        for i, value in enumerate(config):
            if count == self.puzzle.matrix_width:
                linha += 1
                count = 0
            if 0 in config[i:i+self.puzzle.matrix_width]:
                break
            count += 1
        if linha % 2 == 0:
            return True
        else:
            return False

    def _solubility_rules(self, config):
        rule = "par"
        if len(config) %2 == 0:
            if self._check_grid_position(config):
                rule = "par"
            else:
                rule = "impar"
                    
        if rule == "par":
            return False if self.puzzle.points % 2 == 0 else True
        if rule =="impar":
            return True if self.puzzle.points % 2 == 0 else False        


    def there_is_no_solution(self):
        self._update_points(self.puzzle.initial_config)
        check_1 = self._solubility_rules(self.puzzle.initial_config)
        self._update_points(self.puzzle.final_config)
        check_2 = self._solubility_rules(self.puzzle.final_config)
        return check_1 and check_2

    def _update_points(self, config):
        self.puzzle.points = 0
        for i, value in enumerate(config):
            if config[i] == 0:
                self.puzzle.points += 0
            else:
                self.puzzle.points += len([x for x in config[i:] if x < value and x != 0])
                #print("Position={} |Pontos = {} | inversões = {}".format(i, self.puzzle.points, len([i for i in self.puzzle.initial_config[value:] if i > value])))
