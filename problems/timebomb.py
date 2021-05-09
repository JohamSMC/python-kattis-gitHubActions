def main():
    num_list = ["""***
	* *
	* *
	* *
	***""",
                """  *
	*
	*
	*
	*""",
                """***
	*
	***
	*  
	***""", """***
	*
	***
	*
	***""", """* *
	* *
	***
	*
	*""", """***
	*  
	***
	*
	***""", """***
	*  
	***
	* *
	***""", """***
	*
	*
	*
	*""", """***
	* *
	***
	* *
	***""", """***
	* *
	***
	*
	***"""]

    line1 = input()
    line2 = input()
    line3 = input()
    line4 = input()
    line5 = input()

    len_input = len(line1)
    num_numbers = [7, 11, 15, 19, 23, 27, 31]
    #[2, 3, 4, 5, 6, 7, 8]
    if len_input == num_numbers[0]:
        num_digits = 2
    if len_input == num_numbers[1]:
        num_digits = 3
    if len_input == num_numbers[2]:
        num_digits = 4
    if len_input == num_numbers[3]:
        num_digits = 5
    if len_input == num_numbers[4]:
        num_digits = 6
    if len_input == num_numbers[5]:
        num_digits = 7
    if len_input == num_numbers[6]:
        num_digits = 8

    invalid_digit = False
    aux = 0
    aux_output = ""

    while aux < num_digits and invalid_digit == False:
        invalid_digit = True
        if aux == 0:
            temp_num = line1[0:3] + "\n" + line2[0:3] + "\n" + \
                line3[0:3] + "\n" + line4[0:3] + "\n" + line5[0:3]
            for x in range(len(num_list)):
                if num_list[x] == temp_num:
                    invalid_digit = False
                    aux_output += str(x)
        else:
            start_chain = 4+((aux-1)*4)
            end_chain = start_chain+3
            temp_num = line1[start_chain:end_chain] + "\n" + line2[start_chain:end_chain] + "\n" + \
                line3[start_chain:end_chain] + "\n"+line4[start_chain:end_chain] + "\n" + line5[start_chain:end_chain]
            for x in range(len(num_list)):
                if num_list[x] == temp_num:
                    invalid_digit = False
                    aux_output += str(x)

        aux += 1

    if invalid_digit:
        print("BOOM!!")
    else:
        sum_num = 0
        for x in range(len(aux_output)):
            sum_num += int(aux_output[x])
        if int(aux_output) % 2 == 0 and sum_num % 3 == 0:
            print("BEER!!")
        else:
            print("BOOM!!")


if __name__ == '__main__':
    main()
