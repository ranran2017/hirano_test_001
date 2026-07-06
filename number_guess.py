import random


def main():
    # ここにコードを書いてください
    random_number = random.randint(1, 50)
    clear_flg = 0

    clear_flg = test(random_number)

    if clear_flg == 1:
        print("正解です！")

def test(a):
    think_value = 0
    while think_value != a:
        think_value = int(input("隠された整数を当てて下さい: "))
        if think_value > a:
            print("もっと小さい数です")
        elif think_value < a:
            print("もっと大きい数です")
        elif think_value == a:
            return 1
            break


if __name__ == '__main__':
    main()