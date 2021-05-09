def main():
    output = 0
    for x in range(int(input())):
        aux = input()
        output += int(aux[0:-1])**(int(aux[-1]))

    print(output)


if __name__ == '__main__':
    main()
