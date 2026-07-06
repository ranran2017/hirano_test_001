# ここにインポート文を書いてください
import random

# ここに名詞、動詞、形容詞のリストを定義してください
nouns = ["猫", "犬", "車", "木", "家"]
verbs = ["走る", "飛ぶ", "食べる", "見る", "座る"]
adjectives = ["速い", "高い", "美しい", "小さい", "大きい"]

def main():
    # ここにコードを書いてください
    nouns_selected = random.choice(nouns)
    verbs_selected = random.choice(verbs)
    adjectives_selected = random.choice(adjectives)

    print(f"{adjectives_selected}{nouns_selected}が{verbs_selected}")


if __name__ == '__main__':
    main()