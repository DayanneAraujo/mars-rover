# -*- coding: utf-8 -*-
import constants as c
from exceptions.ex_rover import InvalidRover


class Rover:
    """
    The rover attributes to render its position.

        Attributes:
            x_pos (int):  Hover position on plateau grid: X axis.
            y_pos (int): Hover position on plateau grid: Y axis.
            heading (str): One of the four cardinal compass represented by
            the initial letter. ex: n,s,e,w.
    """
    def __init__(self):
        self.x_pos = None
        self.y_pos = None
        self.heading = None

    def land(self, x_pos, y_pos, heading):
        """
        :param x_pos: (int)  Hover position on plateau grid: X axis.
        :param y_pos: (int) Hover position on plateau grid: Y axis.
        :param heading: (char) One of the four cardinal compass represented
            by the initial letter. ex: n,s,e,w.
        :return:
        """
        self.x_pos = x_pos
        self.y_pos = y_pos

        # Validating if heading is valid (n,s,e,w)
        if heading.lower() in c.HEADINGS:
            self.heading = heading.lower()
        else:
            raise ValueError("Heading should be a value like: N, S, E or W. "
                             "{} is not valid".format(heading))

    def is_landed(self):
        """
        Verifies if all variables are not None, so we can say that the
        rover is landed.
        :return: Boolean
        """
        is_x_valid = self.x_pos is not None
        is_y_valid = self.y_pos is not None
        is_heading_valid = self.heading is not None

        return is_x_valid and is_y_valid and is_heading_valid

    def spin(self, direction):
        """
        Rotating a rover right will follow the cardinal compass flow:
        North, East, South, West.

        Rotating left, will rotate backwards the same flow .

        The flow is designed and controlled using the initial letter of each
        cardinal compass point:  ex: cardinal_flow = 'nesw'

        :param direction: (char) describes the rotation direction ex: 'r'.
        :return:
        """
        idx_flow_min = 0
        idx_flow_max = 3
        if self.is_landed():
            index = c.CARDINAL_FLOW.index(self.heading)

            if direction == c.RIGHT:
                # Handling the cardinal_flow edge index
                if index == idx_flow_max:
                    self.heading = c.NORTH

                # Shift right the position based on cardinal_flow
                else:
                    self.heading = c.CARDINAL_FLOW[index+1]

            elif direction == c.LEFT:
                # Handling the cardinal_flow edge index
                if index == idx_flow_min:
                    self.heading = c.WEST

                # Shift left the position based on cardinal_flow
                else:
                    self.heading = c.CARDINAL_FLOW[index-1]
            else:
                raise ValueError("Rotation direction not allowed: {}. "
                      "Please try using: r or l".format(direction))
        else:
            raise InvalidRover("The Rover must be landed to spin")

    def move(self):
        """
        Depending on rover heading, it will move differently along the grid
        :return:
        """
        if self.is_landed():
            move_cord = c.MOVEMENTS[self.heading]

            self.x_pos = self.x_pos + move_cord[0]
            self.y_pos = self.y_pos + move_cord[1]


        else:
            raise ValueError("The Rover must be landed on plateau")