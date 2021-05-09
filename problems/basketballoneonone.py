def main():
    input_game = input()
    score_a = 0
    score_b = 0
    win_a = False
    move = 0

    while (move <= (len(input_game)-2)):
        if input_game[move+0] == "A":
            score_a += 1 if input_game[move+1] == "1" else 2
        elif input_game[move+0] == "B":
            score_b += 1 if input_game[move+1] == "1" else 2

        if score_a >= 11 and score_b < 10:
            win_a = True
            break
        elif score_a >= 10 and score_b >= 10:
            if score_a > score_b and (score_a-score_b) >= 2:
                win_a = True
                break

        move += 1

    if win_a:
        print("A")
    else:
        print("B")


if __name__ == '__main__':
    main()
