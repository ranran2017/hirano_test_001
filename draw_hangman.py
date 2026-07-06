def draw_hangman(tries):
		# ここにコードを書いてください
        if tries == 0:
             print("-----")
             print("|   |")
             print("    |")
             print("    |")
             print("    |")
             print("    |")
             print("--------")

        if tries == 1:
             print("-----")
             print(" |   |")
             print(" O   |")
             print("     |")
             print("     |")
             print("     |")
             print("--------")

        if tries == 2:
             print("-----")
             print(" |   |")
             print(" O   |")
             print(" |   |")
             print("     |")
             print("     |")
             print("--------")

        if tries == 3:
             print("-----")
             print(" |   |")
             print(" O   |")
             print("/|   |")
             print("     |")
             print("     |")
             print("--------")

        if tries == 4:
             print("-----")
             print(" |   |")
             print(" O   |")
             print("/|\  |")
             print("     |")
             print("     |")
             print("--------")

        if tries == 5:
             print("-----")
             print(" |   |")
             print(" O   |")
             print("/|\  |")
             print("/    |")
             print("     |")
             print("--------")

        if tries == 6:
             print("-----")
             print("GAME |")
             print("OVER |")
             print("     |")
             print("_|￣|○ |")
             print("--------")



             

def main():
    # ここにコードを書いてください
    for i in range(7):
        draw_hangman(i)

if __name__ == '__main__':
    main()