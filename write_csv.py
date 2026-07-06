import csv

def main():
    name = input("名前を教えて下さい: ")
    age = input("年齢を教えて下さい: ")
    city = input("住んでいる都市を教えて下さい: ")

    with open('output.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, age, city])   # ← リストで渡す

    with open('output.csv', 'r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(",".join(row))

if __name__ == '__main__':
    main()