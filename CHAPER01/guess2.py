import random

score = 5
loop = 10
print("0で終了。1〜10を当てよう！")

while loop > 0:
    secret = random.randint(1, 10)
    print(f"\n残り{loop}回 / スコア{score}")

    for _ in range(10):
        guess = int(input("数を入力: "))

        if guess == 0:
            print(f"\n終了！最終スコア: {score}")
            exit()

        if guess == secret:
            print("あたり！ +10点")
            score += 10
            loop -= 1
            break
        else:
            print("はずれ -1点")
            score -= 1

    else:
        print(f"正解は {secret}")

    if loop == 0:
        print("\nパーフェクト達成！ +100点")
        score += 100

print(f"\nゲーム終了！最終スコア: {score}")
