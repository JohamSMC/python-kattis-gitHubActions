def main():
    n = int(input())

    while n != -1:
        times = []
        miles = 0

        for x in range(n):
            inputs = list(map(int, input().split()))
            speed = inputs[0]
            times.append(inputs[1])

            if x == 0:
                miles += (speed*times[x])
            else:
                miles += (speed*(times[x]-times[(x-1)]))
        print(miles, "miles")
        n = int(input())


if __name__ == '__main__':
    main()
