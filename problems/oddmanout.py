def main():
    number_cases = int(input())
    for case in range(number_cases):
        input()
        invitation_codes = list(input().split(" "))
        aux_invitation_codes = " ".join(invitation_codes)+" "
        for i in range((len(invitation_codes)//2)+1):
            if aux_invitation_codes.count(invitation_codes[i]+" ") == 1:
                print("Case #", (case+1), ": ", invitation_codes[i], sep="")
                break
            if aux_invitation_codes.count(invitation_codes[len(invitation_codes)-(i+1)]+" ") == 1:
                print(
                    "Case #", (case + 1),
                    ": ", invitation_codes[len(invitation_codes) - (i + 1)],
                    sep="")


if __name__ == '__main__':
    main()
