# ここにインポート文を書いてください
import csv

def main():
    # ここにコードを書いてください
    with open('data.csv', 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            print(*line)


if __name__ == '__main__':
    main()