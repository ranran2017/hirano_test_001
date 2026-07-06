def count_letters(s):
    box = {}

    for letter in s:
        if letter in box:
            box[letter] += 1
        else:
            box[letter] = 1

    print(", ".join(f"'{k}': {v}" for k, v in box.items()))


def main():
    guess = input("単語を入力して下さい: ")
    count_letters(guess)


if __name__ == '__main__':
    main()