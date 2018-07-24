# -*- coding: utf-8 -*-
from src.exceptions.ex_collision import CollisionException
from src.exceptions.ex_invalid_plateau_bounds import InvalidPlateauBounds


class Plateau:
    """
    The plateau is rectangular and divided up into a grid.
    The plateau dimensions are represented by x y co-ordinates.

    Attributes:
        x_max (int): x axis limit.
        y_max (int): y axis limit.
        pos_matrix (list): it is a matrix of booleans representing witch
            positions on plateau are available.
    """
    def __init__(self, x_max, y_max):
        self.x_max = x_max + 1
        self.y_max = y_max + 1
        self.pos_matrix = [[True for x in range(self.x_max)]
                           for y in range(self.y_max)]

    def is_available(self, x, y):
        self.verify_bounds(x, y)
        return self.pos_matrix[x][y]

    def verify_bounds(self, x, y):
        if (x < 0 or y < 0) or (x >= self.x_max or y >= self.y_max):
            raise InvalidPlateauBounds("Invalid plateau bounds.")

    def set_pos_matrix(self, x, y):
        if self.is_available(x, y):
            # Occupy
            self.pos_matrix[x][y] = False
        else:
            raise CollisionException("The land place is not available.")

    def clean_pos_matrix(self, x, y):
        self.pos_matrix[x][y] = True
