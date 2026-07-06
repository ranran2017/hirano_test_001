# ここにインポート文を書いてください
import random
import string

def main():
    # 英大文字 + 英小文字 + 数字 + 記号
    chars = string.ascii_letters + string.digits + string.punctuation

    # 8文字のランダムなパスワードを生成
    password = ''.join(random.choice(chars) for _ in range(8))

    print("生成されたパスワード:", password)

if __name__ == "__main__":
    main()