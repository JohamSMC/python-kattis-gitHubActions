def main():
    r, c, zr, zc = input().split(" ")
    rows = []
    for row in range(int(r)):
        row_input = list(input())
        row = list(map(lambda column: str(column) * int(zc), row_input))
        rows.append(''.join(map(str, row)))

    rows_output = []
    for row in rows:
        for index in range(int(zr)):
            rows_output.append(row)

    print('\n'.join(map(str, rows_output)))


if __name__ == '__main__':
    main()
