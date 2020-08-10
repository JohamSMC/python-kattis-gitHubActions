import unittest
import os
import subprocess
from problems import *

class TestCarrots(unittest.TestCase):    
    def test_carrots(self):
        output = subprocess.check_output("python problems/carrots.py < inputs/inputCarrots1.txt", shell=True)
        self.assertEqual(int(str(output).split("'")[1].split("\\n")[0]), 1)
        output = subprocess.check_output("python problems/carrots.py < inputs/inputCarrots2.txt", shell=True)
        self.assertEqual(int(str(output).split("'")[1].split("\\n")[0]), 5)
if __name__ == "__main__":
    unittest.main()