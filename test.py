import unittest
import os
import subprocess

class TestCarrots(unittest.TestCase):    
    
    def test_hello(self):
    	import problems.hello
    	output = subprocess.check_output("python problems/hello.py", shell=True)
    	self.assertEqual(str(output).split("'")[1].split("\\n")[0], "Hello World!")

    def test_carrots(self):
        import problems.carrots
        output = subprocess.check_output("python problems/carrots.py < inputs/inputCarrots1.txt", shell=True)
        self.assertEqual(int(str(output).split("'")[1].split("\\n")[0]), 1)
        output = subprocess.check_output("python problems/carrots.py < inputs/inputCarrots2.txt", shell=True)
        self.assertEqual(int(str(output).split("'")[1].split("\\n")[0]), 5)

    def test_twostones(self):
    	import problems.twostones
    	output = subprocess.check_output("python problems/twostones.py < inputs/inputtwostones1.txt", shell=True)
    	self.assertEqual(str(output).split("'")[1].split("\\n")[0], "Alice")
    	output = subprocess.check_output("python problems/twostones.py < inputs/inputtwostones2.txt", shell=True)
    	self.assertEqual(str(output).split("'")[1].split("\\n")[0],"Bob")
    	output = subprocess.check_output("python problems/twostones.py < inputs/inputtwostones3.txt", shell=True)
    	self.assertEqual(str(output).split("'")[1].split("\\n")[0],"Alice")    	
    	
if __name__ == "__main__":
    unittest.main()