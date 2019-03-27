from abc import ABCMeta, abstractmethod

class Player:
    """ Abstract Player class
    """
    __metaclass__ = ABCMeta

    _type = None
    _color = None

    def __init__(self, color):
        self._color = color

    @abstractmethod
    def get_move(self, grid):
        pass
