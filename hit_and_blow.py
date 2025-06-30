import random

def generate_answer():
    # 0～9の数字から重複なしで3つ選ぶ（リスト）
    digits = random.sample(range(10), 3)
    return [str(d) for d in digits]  # 文字列に変換して返す

def calculate_hit_blow(answer, guess):
    hit = sum([a == g for a, g in zip(answer, guess)])
    blow = sum([g in answer for g in guess]) - hit
    return hit, blow

def main():
    answer = generate_answer()
    max_attempts = 10
    attempts = 0

    print(" ヒット＆ブロー ゲーム開始！")
    print("3桁の異なる数字を当ててください。")
    print(f"ヒント：最大{max_attempts}回まで。")

    while attempts < max_attempts:
        guess = input(f"{attempts+1}回目の予想（3桁）: ")

        if len(guess) != 3 or not guess.isdigit() or len(set(guess)) != 3:
            print("⚠ 入力は重複なしの3桁の数字にしてください。")
            continue

        guess_list = list(guess)
        hit, blow = calculate_hit_blow(answer, guess_list)
        attempts += 1

        print(f" ヒット: {hit} / ブロー: {blow}")

        if hit == 3:
            print(f" 正解！{attempts}回でクリアしました！")
            break
    else:
        print(f" ゲームオーバー！正解は {''.join(answer)} でした。")

if __name__ == "__main__":
    main()