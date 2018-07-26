import unittest
from src.plateau import Plateau
from src.exceptions.ex_plateau import PlateauException
from src.mars_controller import Controller

class PlateauTest(unittest.TestCase):
    def test_overwrite_plateau(self):
        plateau = Plateau(5, 5)
        ctrl = Controller(plateau)

        self.assertRaises(PlateauException, ctrl.set_plateau, x=5, y=5)

    def test_creating_valid_plateau(self):
        ctrl = Controller(None)
        ctrl.set_plateau(5, 5)

        self.assertEquals(ctrl.plateau.x_max, 5)
        self.assertEquals(ctrl.plateau.y_max, 5)

