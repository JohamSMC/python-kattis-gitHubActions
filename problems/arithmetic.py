def main():
    decimal = int(input(), 8)
    hexadecimal = hex(decimal)
    hexa_string = str(hexadecimal)
    result = hexa_string.replace("0x", "")
    print(result.upper())


if __name__ == '__main__':
    main()
