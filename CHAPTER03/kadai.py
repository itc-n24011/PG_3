# kadai.py

def aisatsu(name, time):
    if time == 1:
        print(f"{name}さん、おはようございます")
    elif time == 2:
        print(f"{name}さん、こんにちは")
    elif time == 3:
        print(f"{name}さん、こんばんは")
    elif time == 4:
        print(f"{name}さん、おやすみなさい")
    else:
        print("時間帯の入力が正しくありません")

# (1) 名前を入力
name = input("名前を入力してください: ")

# (2) 時間帯を数値で入力
print("時間帯を選んでください")
print("朝…1、昼…2、晩…3、寝る前…4")
time = int(input("番号を入力: "))

# (3) あいさつ表示
aisatsu(name, time)
