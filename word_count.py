def main():
    # ここにコードを書いてください
    guess = input("単語を入力して下さい")
    print(f"単語数: {tango_count(guess)}")


def tango_count(a):
    list_a = list(a)
    return len(list_a)


if __name__ == '__main__':
    main()