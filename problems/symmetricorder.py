from typing import List


def main():
    set_size: int = int(input())
    set_number: int = 1
    while set_size != 0:
        input_data: List[str] = []
        output_data: List[str] = []
        for iteration in range(set_size):
            input_data.append(input())

        # print(input_data)
        output_data = list(filter(lambda x: input_data.index(x) % 2 == 0, input_data))
        output_data += list(filter(lambda x: input_data.index(x) % 2 != 0, input_data))[::-1]

        print("SET "+str(set_number))
        for data in output_data:
            print(data)
        set_size = int(input())
        set_number += 1


if __name__ == '__main__':
    main()
