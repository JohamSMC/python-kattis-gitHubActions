def main():
    n, c = list(map(int, input().split(" ")))
    fruit_weight = list(map(int, input().split(" ")))
    output = 0
    aux_output = []

    for i in range(len(fruit_weight)-1):
        if len(fruit_weight)-i <= output:
            break
        aux_output = []
        for j in range(i, len(fruit_weight)):
            if sum(aux_output) == c:
                break
            if (fruit_weight[j]+sum(aux_output) <= c):
                aux_output.append(fruit_weight[j])
            # print("J =",j,end = "\t")
        if len(aux_output) > output:
            output = len(aux_output)
    print(output)


if __name__ == '__main__':
    main()
