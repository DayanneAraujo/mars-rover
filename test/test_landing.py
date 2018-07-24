import unittest
import src.constants as c
from src.plateau import Plateau
from src.mars_controller import Controller
from src.exceptions.ex_collision import CollisionException
from src.exceptions.ex_invalid_plateau_bounds import InvalidPlateauBounds


class RoverTest(unittest.TestCase):
    def test_landing_without_plateau(self):
        ctrl = Controller(None)

        self.assertRaises(ValueError, ctrl.land_rover, x=1, y=2,
                          heading=c.NORTH, name='rover1')

    def test_landing_outside_x_plateau_dimension(self):
        plateau = Plateau(5, 5)
        ctrl = Controller(plateau)
        self.assertRaises(InvalidPlateauBounds, ctrl.land_rover, x=10, y=2,
                          heading=c.NORTH, name='rover1')

    def test_landing_outside_y_plateau_dimension(self):
        plateau = Plateau(5, 5)
        ctrl = Controller(plateau)
        self.assertRaises(InvalidPlateauBounds, ctrl.land_rover, x=2, y=10,
                          heading=c.NORTH, name='rover1')

    def test_when_rover_lands_with_not_valid_heading(self):
        plateau = Plateau(5, 5)
        ctrl = Controller(plateau)
        self.assertRaises(ValueError, ctrl.land_rover, x=2, y=2,
                          heading='X', name='rover1')

    def test_landing_collision_position(self):
        plateau = Plateau(5, 5)
        ctrl = Controller(plateau)
        ctrl.land_rover(x=2, y=2, heading=c.WEST, name='rover1')
        self.assertRaises(CollisionException, ctrl.land_rover, x=2, y=2,
                          heading=c.WEST, name='rover2')

    def test_when_rover_lands_with_valid_params(self):
        plateau = Plateau(5, 5)
        ctrl = Controller(plateau)
        ctrl.land_rover(x=2, y=2, heading=c.WEST, name='rover1')

        rover = ctrl.dict_rover['rover1']

        self.assertEqual(rover.x_pos, 2)
        self.assertEqual(rover.y_pos, 2)
        self.assertEqual(rover.heading, c.WEST)
