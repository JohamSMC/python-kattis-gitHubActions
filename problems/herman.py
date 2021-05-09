import math


def main():
    radius = int(input())
    print("{:.6f}".format(radius * radius * math.pi))
    print("{:.6f}".format(radius * radius * 2))


if __name__ == '__main__':
    main()
