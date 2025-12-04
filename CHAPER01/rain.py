print("雨は降っていますか？")
a=input()
if a == "yes":
    print("傘は持っていますか？")
    b=input()
    if b == "yes":
        print("出かける")
    elif b == "no":
        print("雨が止むまで待つ？")
        c=input()
        if c == "yes":
            print("ずっと待っとけ")
        elif c == "no":
            print("じゃあ走れ")
        else:
            print("yseかnoで答えてください")
    else:
        print("yseかnoで答えてください")
elif a == "no":
    print("諦める")
else:
    print("yseかnoで答えてください")