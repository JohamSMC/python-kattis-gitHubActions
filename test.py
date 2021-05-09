import subprocess
import unittest


class TestExercises(unittest.TestCase):

    def test_hello(self):
        output = subprocess.check_output("python problems/hello.py", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "Hello World!")

    def test_carrots(self):
        output = subprocess.check_output(
            "python problems/carrots.py < inputs/inputCarrots1.txt", shell=True)
        self.assertEqual(int(str(output).split("'")[1].split("\\n")[0]), 1)

        output = subprocess.check_output(
            "python problems/carrots.py < inputs/inputCarrots2.txt", shell=True)
        self.assertEqual(int(str(output).split("'")[1].split("\\n")[0]), 5)

    def test_twostones(self):
        output = subprocess.check_output(
            "python problems/twostones.py < inputs/inputtwostones1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "Alice")

        output = subprocess.check_output(
            "python problems/twostones.py < inputs/inputtwostones2.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "Bob")

        output = subprocess.check_output(
            "python problems/twostones.py < inputs/inputtwostones3.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "Alice")

    def test_r2(self):
        output = subprocess.check_output("python problems/r2.py < inputs/inputR2-1.txt", shell=True)
        self.assertEqual(int(str(output).split("'")[1].split("\\n")[0]), 19)

        output = subprocess.check_output("python problems/r2.py < inputs/inputR2-2.txt", shell=True)
        self.assertEqual(int(str(output).split("'")[1].split("\\n")[0]), 2)

    def test_qaly(self):
        output = subprocess.check_output(
            "python problems/qaly.py < inputs/inputQaly1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "41.470")

    def test_pot(self):
        output = subprocess.check_output(
            "python problems/pot.py < inputs/inputPot1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "1953566")

        output = subprocess.check_output(
            "python problems/pot.py < inputs/inputPot2.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "102")

        output = subprocess.check_output(
            "python problems/pot.py < inputs/inputPot3.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "10385")

    def test_skener(self):
        output = subprocess.check_output(
            "python problems/skener.py < inputs/inputSkener1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), ["..xx..", "xx..xx", "..xx..", ''])

        output = subprocess.check_output(
            "python problems/skener.py < inputs/inputSkener2.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), [
                         ".x.", ".x.", "x.x", "x.x", ".x.", ".x.", ''])

    def test_herman(self):
        output = subprocess.check_output(
            "python problems/herman.py < inputs/input1Herman.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), ["3.141593", "2.000000", ''])

        output = subprocess.check_output(
            "python problems/herman.py < inputs/input2Herman.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), ["1385.442360", "882.000000", ''])

        output = subprocess.check_output(
            "python problems/herman.py < inputs/input3Herman.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), ["5541.769441", "3528.000000", ''])

    def test_kejima08(self):
        output = subprocess.check_output(
            "python problems/kemija08.py < inputs/inputKejima08-1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), ["zelena paprika", ''])

        output = subprocess.check_output(
            "python problems/kemija08.py < inputs/inputKejima08-2.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), ["bas je dosadna ova kemija", ''])

    def test_aaah(self):
        output = subprocess.check_output(
            "python problems/aaah.py < inputs/inputAaah1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), ["no", ''])

        output = subprocess.check_output(
            "python problems/aaah.py < inputs/inputAaah2.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), ["go", ''])

    def test_abc(self):
        output = subprocess.check_output(
            "python problems/abc.py < inputs/inputAbc1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), ["1", "3", "5", ''])

        output = subprocess.check_output(
            "python problems/abc.py < inputs/inputAbc2.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), ["6", "2", "4", ''])

    def test_aboveaverage(self):
        output = subprocess.check_output(
            "python problems/aboveaverage.py < inputs/inputAboveaverage1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), [
                         "40.000%", "57.143%", "33.333%", '66.667%', '55.556%', ''])

    def test_apaxiaaans(self):
        output = subprocess.check_output(
            "python problems/apaxiaaans.py < inputs/inputApaxiaaans1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), ["robert", ''])

        output = subprocess.check_output(
            "python problems/apaxiaaans.py < inputs/inputApaxiaaans2.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), ["robert", ''])

        output = subprocess.check_output(
            "python problems/apaxiaaans.py < inputs/inputApaxiaaans3.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), ["robertapalaxios", ''])

    def test_areal(self):
        output = subprocess.check_output(
            "python problems/areal.py < inputs/inputAreal1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), ["16.00000000", ''])

        output = subprocess.check_output(
            "python problems/areal.py < inputs/inputAreal2.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), ["8.94427191", ''])

    def test_arithmetic(self):
        output = subprocess.check_output(
            "python problems/arithmetic.py < inputs/inputArithmetic1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), ["924", ''])

        output = subprocess.check_output(
            "python problems/arithmetic.py < inputs/inputArithmetic2.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), ["10", ''])

        output = subprocess.check_output(
            "python problems/arithmetic.py < inputs/inputArithmetic3.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), ["689", ''])

        output = subprocess.check_output(
            "python problems/arithmetic.py < inputs/inputArithmetic4.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), ["FAC688053977", ''])

    def test_armystrengtheasy(self):
        output = subprocess.check_output(
            "python problems/armystrengtheasy.py < inputs/inputArmystrengtheasy1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), ["Godzilla", "MechaGodzilla", ''])

    def test_autori(self):
        output = subprocess.check_output(
            "python problems/autori.py < inputs/inputAutori1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), ["KMP"])

        output = subprocess.check_output(
            "python problems/autori.py < inputs/inputAutori2.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), ["MS"])

        output = subprocess.check_output(
            "python problems/autori.py < inputs/inputAutori3.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), ["PP"])

    def test_basketballoneonone(self):
        output = subprocess.check_output(
            "python problems/basketballoneonone.py < inputs/inputBasketballoneonone1.txt",
            shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), ["A", ''])

        output = subprocess.check_output(
            "python problems/basketballoneonone.py < inputs/inputBasketballoneonone2.txt",
            shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), ["A", ''])

    def test_bijele(self):
        output = subprocess.check_output(
            "python problems/bijele.py < inputs/inputBijele1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "1 0 0 0 0 1")

        output = subprocess.check_output(
            "python problems/bijele.py < inputs/inputBijele2.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "-1 0 0 1 0 7")

    def test_cokolada(self):
        output = subprocess.check_output(
            "python problems/cokolada.py < inputs/inputCokolada1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "8 2")

        output = subprocess.check_output(
            "python problems/cokolada.py < inputs/inputCokolada2.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "8 3")

        output = subprocess.check_output(
            "python problems/cokolada.py < inputs/inputCokolada3.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "8 3")

    def test_cold(self):
        output = subprocess.check_output(
            "python problems/cold.py < inputs/inputCold1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "1")

        output = subprocess.check_output(
            "python problems/cold.py < inputs/inputCold2.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "5")

    def test_faktor(self):
        output = subprocess.check_output(
            "python problems/faktor.py < inputs/inputFaktor1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "875")

        output = subprocess.check_output(
            "python problems/faktor.py < inputs/inputFaktor2.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "100")

        output = subprocess.check_output(
            "python problems/faktor.py < inputs/inputFaktor3.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "91")

    def test_filip(self):
        output = subprocess.check_output(
            "python problems/filip.py < inputs/inputFilip1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "437")

        output = subprocess.check_output(
            "python problems/filip.py < inputs/inputFilip2.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "132")

        output = subprocess.check_output(
            "python problems/filip.py < inputs/inputFilip3.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "938")

    def test_hissingmicrophone(self):
        output = subprocess.check_output(
            "python problems/hissingmicrophone.py < inputs/inputHissingmicrophone1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "hiss")

        output = subprocess.check_output(
            "python problems/hissingmicrophone.py < inputs/inputHissingmicrophone2.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "no hiss")

        output = subprocess.check_output(
            "python problems/hissingmicrophone.py < inputs/inputHissingmicrophone3.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "hiss")

    def test_lastfactorialdigit(self):
        output = subprocess.check_output(
            "python problems/lastfactorialdigit.py < inputs/inputLastfactorialdigit1.txt",
            shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), ["1", "2", "6", ''])

        output = subprocess.check_output(
            "python problems/lastfactorialdigit.py < inputs/inputLastfactorialdigit2.txt",
            shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), ["0", "2", ''])

    def test_oddities(self):
        output = subprocess.check_output(
            "python problems/oddities.py < inputs/inputOddities1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), [
                         "10 is even", "9 is odd", "-5 is odd", ''])

    def test_oddmanout(self):
        output = subprocess.check_output(
            "python problems/oddmanout.py < inputs/inputOddmanout1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), [
                         "Case #1: 1", "Case #2: 7", "Case #3: 5", ''])

    def test_pet(self):
        output = subprocess.check_output(
            "python problems/pet.py < inputs/inputPet1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "4 19")

        output = subprocess.check_output(
            "python problems/pet.py < inputs/inputPet2.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "2 17")

    def test_putovanje(self):
        output = subprocess.check_output(
            "python problems/putovanje.py < inputs/inputPutovanje1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "4")

        output = subprocess.check_output(
            "python problems/putovanje.py < inputs/inputPutovanje2.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "3")

        output = subprocess.check_output(
            "python problems/putovanje.py < inputs/inputPutovanje3.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "3")

    def test_quadrant(self):
        output = subprocess.check_output(
            "python problems/quadrant.py < inputs/inputQuadrant1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "1")

        output = subprocess.check_output(
            "python problems/quadrant.py < inputs/inputQuadrant2.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "4")

    def test_reversebinary(self):
        output = subprocess.check_output(
            "python problems/reversebinary.py < inputs/inputReversebinary1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "11")

        output = subprocess.check_output(
            "python problems/reversebinary.py < inputs/inputReversebinary2.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "61")

    def test_reverserot(self):
        output = subprocess.check_output(
            "python problems/reverserot.py < inputs/inputReverserot1.txt", shell=True)
        self.assertEqual(
            str(output).split("'")[1].split("\\n"),
            ["EDCB", "CHUHKWBR.", "UPEA", "ROAD", "PWRAYF_LWNHAXWH.RHPWRAJAX_HMWJHPWRAORQ.",
             "FGVTGXPQEAGDAQVAIPKTVU", "REVERSE_ROT", ''])

    def test_sibice(self):
        output = subprocess.check_output(
            "python problems/sibice.py < inputs/inputSibice1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), ["DA", "DA", "DA", "NE", "NE", ''])

        output = subprocess.check_output(
            "python problems/sibice.py < inputs/inputSibice2.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), ["NE", "DA", ''])

    def test_simon(self):
        output = subprocess.check_output(
            "python problems/simon.py < inputs/inputSimon1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), [
                         "write a program", "", "", "get balloons", ''])

    def test_simonsays(self):
        output = subprocess.check_output(
            "python problems/simonsays.py < inputs/inputSimonsays1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), ["smile.", ''])

        output = subprocess.check_output(
            "python problems/simonsays.py < inputs/inputSimonsays2.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), [
                         "raise your right hand.", "raise your left hand.", ''])

        output = subprocess.check_output(
            "python problems/simonsays.py < inputs/inputSimonsays3.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), ["raise your left hand.", ''])

    def test_spavanac(self):
        output = subprocess.check_output(
            "python problems/spavanac.py < inputs/inputSpavanac1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "9 25")

        output = subprocess.check_output(
            "python problems/spavanac.py < inputs/inputSpavanac2.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "23 45")

        output = subprocess.check_output(
            "python problems/spavanac.py < inputs/inputSpavanac3.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "22 55")

    def test_speedlimit(self):
        output = subprocess.check_output(
            "python problems/speedlimit.py < inputs/inputSpeedlimit1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), [
                         "170 miles", "180 miles", "90 miles", ''])

    def test_t9spelling(self):
        output = subprocess.check_output(
            "python problems/t9spelling.py < inputs/inputT9spelling1.txt", shell=True)
        self.assertEqual(
            str(output).split("'")[1].split("\\n"),
            ["Case #1: 44 444", "Case #2: 999337777", "Case #3: 333666 6660 022 2777",
             "Case #4: 4433555 555666096667775553", ''])

    def test_tarifa(self):
        output = subprocess.check_output(
            "python problems/tarifa.py < inputs/inputTarifa1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "28")

        output = subprocess.check_output(
            "python problems/tarifa.py < inputs/inputTarifa2.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "16")

        output = subprocess.check_output(
            "python problems/tarifa.py < inputs/inputTarifa3.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "15")

    def test_timebomb(self):
        output = subprocess.check_output(
            "python problems/timebomb.py < inputs/inputTimebomb2.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "BOOM!!")

        output = subprocess.check_output(
            "python problems/timebomb.py < inputs/inputTimebomb3.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "BOOM!!")

    def test_timeloop(self):
        output = subprocess.check_output(
            "python problems/timeloop.py < inputs/inputTimeloop1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n"), [
                         "1 Abracadabra", "2 Abracadabra", "3 Abracadabra",
                         "4 Abracadabra", "5 Abracadabra", ''])

        output = subprocess.check_output(
            "python problems/timeloop.py < inputs/inputTimeloop2.txt", shell=True)
        self.assertEqual(
            str(output).split("'")[1].split("\\n"),
            ["1 Abracadabra", "2 Abracadabra", "3 Abracadabra", "4 Abracadabra", "5 Abracadabra",
             "6 Abracadabra", "7 Abracadabra", "8 Abracadabra", "9 Abracadabra", "10 Abracadabra",
             ''])

    def test_tri(self):
        output = subprocess.check_output(
            "python problems/tri.py < inputs/inputTri1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "5+3=8")

        output = subprocess.check_output(
            "python problems/tri.py < inputs/inputTri2.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "5=15/3")

    def test_trik(self):
        output = subprocess.check_output(
            "python problems/trik.py < inputs/inputTrik1.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "3")

        output = subprocess.check_output(
            "python problems/trik.py < inputs/inputTrik2.txt", shell=True)
        self.assertEqual(str(output).split("'")[1].split("\\n")[0], "1")

    def test_symmetricorder(self):
        output = subprocess.check_output(
            "python problems/symmetricorder.py < inputs/inputSymmetricorder1.txt", shell=True)
        self.assertEqual(
            str(output).split("'")[1].split("\\n"),
            ["SET 1", "Bo", "Jean", "Claude", "Marybeth", "William", "Kevin", "Pat", "SET 2", "Jim",
             'Zoe', "Frederick", "Annabelle", "Joey", "Ben", "SET 3", "John", "Fran", "Cece",
             "Stan", "Bill", ''])


if __name__ == "__main__":
    unittest.main()
