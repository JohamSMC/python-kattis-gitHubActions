from tokenize import Double
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
		self.assertEqual(str(output).split("'")[1].split("\\n")[0], "Bob")

		output = subprocess.check_output("python problems/twostones.py < inputs/inputtwostones3.txt", shell=True)
		self.assertEqual(str(output).split("'")[1].split("\\n")[0], "Alice")

	def test_r2(self):
		import problems.r2
		output = subprocess.check_output("python problems/r2.py < inputs/inputR2-1.txt", shell=True)
		self.assertEqual(int(str(output).split("'")[1].split("\\n")[0]), 19)

		output = subprocess.check_output("python problems/r2.py < inputs/inputR2-2.txt", shell=True)
		self.assertEqual(int(str(output).split("'")[1].split("\\n")[0]), 2)

	def test_qaly(self):
		import problems.qaly
		output = subprocess.check_output("python problems/qaly.py < inputs/inputQaly1.txt", shell=True)
		self.assertEqual(str(output).split("'")[1].split("\\n")[0], "41.470")

	def test_pot(self):
		import problems.pot
		output = subprocess.check_output("python problems/pot.py < inputs/inputPot1.txt", shell=True)
		self.assertEqual(str(output).split("'")[1].split("\\n")[0], "1953566")

		output = subprocess.check_output("python problems/pot.py < inputs/inputPot2.txt", shell=True)
		self.assertEqual(str(output).split("'")[1].split("\\n")[0], "102")

		output = subprocess.check_output("python problems/pot.py < inputs/inputPot3.txt", shell=True)
		self.assertEqual(str(output).split("'")[1].split("\\n")[0], "10385")

if __name__ == "__main__":
	unittest.main()