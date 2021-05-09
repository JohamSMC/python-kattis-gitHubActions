def main():
    numbers_part = list(map(int, input().split()))

    print(missing_files(numbers_part[0], 1)+" "+missing_files(numbers_part[1], 1)
          + " "+missing_files(numbers_part[2], 2)+" "+missing_files(numbers_part[3], 2)
          + " "+missing_files(numbers_part[4], 2)+" "+missing_files(numbers_part[5], 8))


def missing_files(num_part, valid_set):
    if num_part == valid_set:
        return "0"
    else:
        return str(valid_set-num_part)


if __name__ == '__main__':
    main()
