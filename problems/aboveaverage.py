def main():
    number_times = int(input())

    for element in range(number_times):
        aux_numbs = input().split(" ")
        aux_numbs.reverse()

        aux_numbs.pop()

        average_students = average(aux_numbs)
        num_students = 0
        for x in range(len(aux_numbs)):
            if int(aux_numbs[x]) > average_students:
                num_students += 1

        porcentaje_students = (num_students*100)/len(aux_numbs)
        """print(round(porcentaje_students,3))	"""
        print("{0:.3f}".format(porcentaje_students), "%", sep="")


def average(numbs):
    sum = 0.0
    for i in range(len(numbs)):
        sum = sum+int(numbs[i])

    return sum/len(numbs)


if __name__ == '__main__':
    main()
