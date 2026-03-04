import unittest
from calculator import calculator

class TestOperations(unittest.TestCase):

    def test_sum(self):
        calculation = calculator (2,2)
        self.assertEqual(calculation.get_sum(), 4, "The answer is not 4!!")

    def test_substraction(self):
        calculation = calculator (4,2)
        self.assertEqual(calculation.get_substraction(), 2,"The answer is not 2!!")

    def test_product(self):
        calculation = calculator (2,2)
        self.assertEqual(calculation.get_product(), 4,"The answer is not 4!!")   

    def test_qotient(self):
        calculation = calculator (4,2)
        self.assertEqual(calculation.get_qotient(), 2,"The answer is not 2!!")   

if __name__ == "__main__":

    unittest.main()