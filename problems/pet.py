def main():
    cont = 0
    lis_num = []
    for x in range(5):
        aux = list(map(int, input().split()))
        lis_num.insert(cont, sum(aux))
        cont += 1

    print(lis_num.index(max(lis_num))+1, max(lis_num))


if __name__ == '__main__':
    main()
