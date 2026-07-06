def main():
    # ここで letters を出力してください
    item_01 = item()
    print(f"{item_01}")

def item():
    word = "development"
    letters = list(word)
    return letters

if __name__ == '__main__':
    main()