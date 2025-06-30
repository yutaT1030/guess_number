import random

def generate_number():
    return random.randint(100, 999)

def main():
    answer = generate_number()
    max_attempts = 10
    attempts = 0

    print("★ 数字当てゲーム開始（3桁の数字を当てよう）")
    print(f"ヒント：{max_attempts}回以内に当ててください。")

    while attempts < max_attempts:
        guess = input(f"{attempts+1}回目の予想：")
        
        if not guess.isdigit() or len(guess) != 3:
            print("⚠ 3桁の数字を入力してください。")
            continue

        guess = int(guess)
        attempts += 1

        if guess == answer:
            print(f" 正解！おめでとうございます（{attempts}回目）")
            break
        elif guess < answer:
            print(" 不正解！もっと大きな数です。")
        else:
            print(" 不正解！もっと小さな数です。")

    else:
        print(f" 残念！正解は {answer} でした。")

if __name__ == "__main__":
    main()