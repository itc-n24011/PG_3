import requests, os, bs4
url="https://xkcd.com"
os.makedirs("xkcd", exist_ok=True)
while not url.endswith('#'):
    #ページをダウンロードする
    #コミック画像のURLを見つける
    #画像を./xkcdに保存する
    #「Prev」ボタンのURLを取得する

print("完了")