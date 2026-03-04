import unittest
from calculator import calculator

class TestOperations(unittest.TestCase):

    def setUp(self):
        self.myCalc = calculator(8,2)

    def test_sum(self):
     
        self.assertEqual(self.myCalc.get_sum(), 10, "The answer is not 4!!")

    def test_substraction(self):
       
        self.assertEqual(self.myCalc.get_substraction(), 6,"The answer is wrong!!")

    def test_product(self):
       
        self.assertEqual(self.myCalc.get_product(), 16,"The answer is wrong!!")

    def test_qotient(self):
       
        self.assertEqual(self.myCalc.get_qotient(), 4,"The answer is wrong!!")   

if __name__ == "__main__":

    unittest.main()