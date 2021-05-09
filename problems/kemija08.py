def main():
    input_hain = input().lower()

    input_hain = input_hain.replace('apa', 'a')
    input_hain = input_hain.replace('epe', 'e')
    input_hain = input_hain.replace('ipi', 'i')
    input_hain = input_hain.replace('opo', 'o')
    input_hain = input_hain.replace('upu', 'u')

    print(input_hain)


if __name__ == '__main__':
    main()
