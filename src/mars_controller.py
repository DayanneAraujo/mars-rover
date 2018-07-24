import re
import constants as c
from plateau import Plateau
from rover import Rover
from src.exceptions.ex_collision import CollisionException
from src.exceptions.ex_rover import InvalidRover


class Controller:
    def __init__(self, plateau):
        self.plateau = plateau
        self.dict_rover = {}
        self.instructions_pattern = re.compile("[lrm]+", re.IGNORECASE)

    def set_plateau(self, x, y):
        """
        Setting plateau dimensions.
        :param x: (int) x dimension on plateau grid.
        :param y: (int) y dimension on plateau grid
        :return: plateau object
        """
        self.plateau = Plateau(x_max=x, y_max=y)

    def is_rover_on_plateau(self, x, y):
        """
        Verifies if the rover position is on plateau grid.
        :param x: (int) y axis coordinate on plateau grid
        :param y: (int) y axis coordinate on plateau grid
        :return: bool
        """
        if self.plateau:
            is_x_on_plateau = (x >= 0) and (x <= self.plateau.x_max)
            is_y_on_plateau = (y >= 0) and (y <= self.plateau.y_max)

            return is_x_on_plateau and is_y_on_plateau
        return False

    def is_coordinate_available(self, x_move, y_move):
        """
        Verifies if a position on plateau is available

        :param x_move: (int) x axis coordinate on plateau grid
        :param y_move: (int) y axis coordinate on plateau grid
        :return: bool
        """
        return self.plateau.is_available(x_move, y_move)

    def land_rover(self, x, y, heading, name):
        """
        Land rover on a position on plateau.
        Conditions:
            1) The rover can not land out of plateau grid.

            2) The rover can not land on a position that
            there is other rover positioned (collision).

        :param x: (int) x axis coordinate on plateau grid
        :param y: (int) y axis coordinate on plateau grid
        :param name: (str) rover identifier name ex: rover1
        :return:
        """
        rover = Rover()

        try:
            if self.plateau:
                rover.land(x_pos=x, y_pos=y, heading=heading)

                self.plateau.set_pos_matrix(x, y)
                self.dict_rover[name] = rover
            else:
                raise ValueError('Plateau is required before landing')
        except (CollisionException, ValueError) as ex:
            rover.x_pos = None
            rover.y_pos = None

            raise ex

    def is_instructions_str_valid(self, instructions_str):
        """
        Verifies if instruction match the expected regex pattern
        :param instructions_str: (str)
        :return: Bool
        """
        return self.instructions_pattern.match(instructions_str) is not None

    def move_rover_action(self, instructions_str, rover_obj):
        """
        Execute the move action
        :param instructions_str:
        :param rover_obj:
        :return:
        """
        x_init, y_init = rover_obj.x_pos, rover_obj.y_pos
        try:
            instructions = instructions_str.lower()
            for instruction in instructions:
                if (instruction == c.LEFT) or (instruction == c.RIGHT):
                    rover_obj.spin(instruction)
                elif instruction == c.MOVE:
                    self.plateau.clean_pos_matrix(rover_obj.x_pos,
                                                  rover_obj.y_pos)
                    rover_obj.move()

                    self.plateau.set_pos_matrix(rover_obj.x_pos,
                                                rover_obj.y_pos)
                else:
                    raise ValueError('Invalid instruction: {}'
                                     .format(instruction))
        except (CollisionException, ValueError) as ex:
            self.plateau.set_pos_matrix(x_init, y_init)
            rover_obj.x_pos = x_init
            rover_obj.y_pos = y_init

            raise ex

    def instructions(self, rover_name, instructions_str):
        """
        Execute the instructions on rover.
        :param rover_name: (str) rover identifier name ex: 'rover1'
        :param instructions_str: (str) right, left, move ex: 'MMRMMRMRRM'

        :return:
        """
        try:
            rover_obj = self.dict_rover[rover_name]
        except KeyError:
            raise InvalidRover("Please make sure that {} "
                               "is landed on plateau".format(rover_name))

        try:
            if rover_obj and rover_obj.is_landed() and \
                    self.is_rover_on_plateau(rover_obj.x_pos,
                                             rover_obj.y_pos):

                if self.is_instructions_str_valid(instructions_str):
                    self.move_rover_action(instructions_str, rover_obj)

                else:
                    raise ValueError('Invalid instruction')

            else:
                raise InvalidRover("Please make sure that {} "
                         "is landed".format(rover_name))

        except (ValueError, InvalidRover, CollisionException) as ex:
            raise ex
