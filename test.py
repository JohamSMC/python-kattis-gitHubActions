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

	def test_skener(self):
		import problems.skener
		output = subprocess.check_output("python problems/skener.py < inputs/inputSkener1.txt", shell=True)
		self.assertEqual(str(output).split("'")[1].split("\\n"), ["..xx..","xx..xx","..xx..",''])

		output = subprocess.check_output("python problems/skener.py < inputs/inputSkener2.txt", shell=True)
		self.assertEqual(str(output).split("'")[1].split("\\n"), [".x.",".x.","x.x","x.x",".x.",".x.",''])

	def test_herman(self):
		import problems.herman
		output = subprocess.check_output("python problems/herman.py < inputs/input1Herman.txt", shell=True)
		self.assertEqual(str(output).split("'")[1].split("\\n"), ["3.141593","2.000000",''])

		output = subprocess.check_output("python problems/herman.py < inputs/input2Herman.txt", shell=True)
		self.assertEqual(str(output).split("'")[1].split("\\n"), ["1385.442360","882.000000",''])

		output = subprocess.check_output("python problems/herman.py < inputs/input3Herman.txt", shell=True)
		self.assertEqual(str(output).split("'")[1].split("\\n"), ["5541.769441","3528.000000",''])

	def test_kejima08(self):
		import problems.kemija08
		output = subprocess.check_output("python problems/kemija08.py < inputs/inputKejima08-1.txt", shell=True)
		self.assertEqual(str(output).split("'")[1].split("\\n"), ["zelena paprika",''])

		output = subprocess.check_output("python problems/kemija08.py < inputs/inputKejima08-2.txt", shell=True)
		self.assertEqual(str(output).split("'")[1].split("\\n"), ["bas je dosadna ova kemija",''])

	def test_aaah(self):
		import problems.aaah
		output = subprocess.check_output("python problems/aaah.py < inputs/inputAaah1.txt", shell=True)
		self.assertEqual(str(output).split("'")[1].split("\\n"), ["no",''])

		output = subprocess.check_output("python problems/aaah.py < inputs/inputAaah2.txt", shell=True)
		self.assertEqual(str(output).split("'")[1].split("\\n"), ["go",''])

	def test_abc(self):
		import problems.abc
		output = subprocess.check_output("python problems/abc.py < inputs/inputAbc1.txt", shell=True)
		self.assertEqual(str(output).split("'")[1].split("\\n"), ["1","3","5",''])

		output = subprocess.check_output("python problems/abc.py < inputs/inputAbc2.txt", shell=True)
		self.assertEqual(str(output).split("'")[1].split("\\n"), ["6","2","4",''])

	def test_aboveaverage(self):
		import problems.aboveaverage
		output = subprocess.check_output("python problems/aboveaverage.py < inputs/inputAboveaverage1.txt", shell=True)
		self.assertEqual(str(output).split("'")[1].split("\\n"), ["40.000%","57.143%","33.333%",'66.667%','55.556%',''])

	def test_apaxiaaans(self):
		import problems.apaxiaaans
		output = subprocess.check_output("python problems/apaxiaaans.py < inputs/inputApaxiaaans1.txt", shell=True)
		self.assertEqual(str(output).split("'")[1].split("\\n"), ["robert",''])

		output = subprocess.check_output("python problems/apaxiaaans.py < inputs/inputApaxiaaans2.txt", shell=True)
		self.assertEqual(str(output).split("'")[1].split("\\n"), ["robert",''])

		output = subprocess.check_output("python problems/apaxiaaans.py < inputs/inputApaxiaaans3.txt", shell=True)
		self.assertEqual(str(output).split("'")[1].split("\\n"), ["robertapalaxios",''])

	def test_areal(self):
		import problems.areal
		output = subprocess.check_output("python problems/areal.py < inputs/inputAreal1.txt", shell=True)
		self.assertEqual(str(output).split("'")[1].split("\\n"), ["16.00000000",''])

		output = subprocess.check_output("python problems/areal.py < inputs/inputAreal2.txt", shell=True)
		self.assertEqual(str(output).split("'")[1].split("\\n"), ["8.94427191",''])

if __name__ == "__main__":
	unittest.main()