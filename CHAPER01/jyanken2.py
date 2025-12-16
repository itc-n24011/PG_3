import random

hands = ["g", "c", "p"]  # g=グー, c=チョキ, p=パー
hand_name = {"g": "グー", "c": "チョキ", "p": "パー"}

print("じゃんけん10回勝負！")
print("g=グー, c=チョキ, p=パー, 0=終了\n")

player_score = 0
cpu_score = 0

rounds = 10

for i in range(1, rounds + 1):
    print(f"\n【第{i}回】")
    cpu = random.choice(hands)

    # --- 入力受付 ---
    while True:
        player = input("あなたの手を入力: ")
        if player in ["g", "c", "p", "0"]:
            break
        print("入力が違います。g/c/p/0 のいずれかを入力してください。")

    # --- ゲーム終了処理 ---
    if player == "0":
        print("\nゲーム終了を選択！あなたのポイント −1点")
        player_score -= 1
        break

    # --- 手の表示 ---
    print(f"コンピュータ: {hand_name[cpu]}")
    print(f"あなた: {hand_name[player]}")

    # --- 勝敗判定 ---
    if cpu == player:
        print("→ あいこ！ポイントなし")
    elif (player == "g" and cpu == "c") or \
         (player == "c" and cpu == "p") or \
         (player == "p" and cpu == "g"):
        print("→ あなたの勝ち！ +1点")
        player_score += 1
    else:
        print("→ コンピュータの勝ち！ +1点")
        cpu_score += 1

# --- 結果発表 ---
print("\n==========================")
print("        最終結果")
print("==========================")
print(f"あなたの得点: {player_score}")
print(f"コンピュータの得点: {cpu_score}")

if player_score > cpu_score:
    print("→ あなたの勝ち！")
elif player_score < cpu_score:
    print("→ コンピュータの勝ち！")
else:
    print("→ 引き分け！")
