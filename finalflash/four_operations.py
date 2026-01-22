seisu1 = int(input("１つ目の整数を入力してください>>"))
seisu2 = int(input("２つ目の整数を入力してください>>"))


print("和:", seisu1 + seisu2)
print("差:", seisu1 - seisu2)
print("積:", seisu1 * seisu2)

if seisu2 != 0:
    print("商:", seisu1 // seisu2)
    print("剰余:", seisu1 % seisu2)