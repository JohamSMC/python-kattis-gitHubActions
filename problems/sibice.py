import math


def main():
    n, w, h = list(map(int, input().split()))

    for x in range(n):
        a = (w**2)+(h**2)
        entrada = float(input())
        if entrada <= math.sqrt(a):
            print("DA")
        else:
            print("NE")


if __name__ == '__main__':
    main()
