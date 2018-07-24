import unittest
import src.constants as c
from src.plateau import Plateau
from src.mars_controller import Controller
from src.exceptions.ex_rover import InvalidRover
from src.exceptions.ex_collision import CollisionException

class RoverTest(unittest.TestCase):
    def test_instruction_without_plateau(self):
        ctrl = Controller(None)
        self.assertRaises(InvalidRover, ctrl.instructions,
                          rover_name='rover1', instructions_str='MMRMMRMRRM')

    def test_instruction_without_rover_landed(self):
        plateau = Plateau(5, 5)
        ctrl = Controller(plateau)

        self.assertRaises(InvalidRover, ctrl.instructions,
                          rover_name='rover1', instructions_str='MMRMMRMRRM')

    def test_invalid_instructions(self):
        plateau = Plateau(5, 5)
        ctrl = Controller(plateau)
        ctrl.land_rover(x=2, y=2, heading=c.WEST, name='rover1')

        self.assertRaises(ValueError, ctrl.instructions,
                          rover_name='rover1', instructions_str='XYRMMRMRRM')

    def test_instruction_causing_collision(self):
        plateau = Plateau(5, 5)
        ctrl = Controller(plateau)
        ctrl.land_rover(x=2, y=2, heading=c.WEST, name='rover1')

        ctrl.land_rover(x=3, y=2, heading=c.WEST, name='rover2')

        self.assertRaises(CollisionException, ctrl.instructions,
                          rover_name='rover2', instructions_str='M')


    def test_valid_instruction(self):
        plateau = Plateau(5, 5)
        ctrl = Controller(plateau)

        ctrl.land_rover(x=3, y=3, heading=c.EAST, name='rover1')
        ctrl.instructions('rover1', 'MMRMMRMRRM')
        rover1 = ctrl.dict_rover['rover1']

        ctrl.land_rover(x=1, y=2, heading=c.NORTH, name='rover2')
        ctrl.instructions('rover2', 'LMLMLMLMM')
        rover2 = ctrl.dict_rover['rover2']


        self.assertEquals(rover1.x_pos, 5)
        self.assertEquals(rover1.y_pos, 1)
        self.assertEquals(rover1.heading, c.EAST)

        self.assertEquals(rover2.x_pos, 1)
        self.assertEquals(rover2.y_pos, 3)
        self.assertEquals(rover2.heading, c.NORTH)
