def main():
    # ここにコードを書いてください
    text_01 = input()
    reverse_text = reverse(text_01)
    print(f"{reverse_text}")

def reverse(a):
    return a[::-1]

if __name__ == '__main__':
    main()