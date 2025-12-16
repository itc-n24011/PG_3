import random

def omikuji(n):
    if n == 1:
        return "大吉"
    elif n in (2, 3):
        return "中吉"
    elif 4 <= n <= 7:
        return "小吉"
    elif n in (8, 9):
        return "吉"
    else:
        return "凶"

def main():
    num = random.randint(1, 10)
    print(f"乱数: {num}")
    print("結果:", omikuji(num))

main()
