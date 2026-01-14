import pathlib
import os

pname=input("調べるディレクトリ名を絶対パスで指定してください>>")

p=pathlib.Path(pname)
#入力されたパスが存在しているかチェックしてから表示
if p.is_dir() == True:
    olist = os.listdir(pname)
    for fo in olist:
        print(fo)
else:
    print(f"{pname}というパスはありません")