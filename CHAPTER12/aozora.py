#青空文庫からタグを省いて出力　※一部エラーあり
from urllib import request
from bs4 import BeautifulSoup
import re

url=["", "https://www.aozora.gr.jp/cards/000148/files/752_14964.html",
     "https://www.aozora.gr.jp/cards/000879/files/95_15247.html",
     "https://www.aozora.gr.jp/cards/000081/files/473_42318.html",
     "https://www.aozora.gr.jp/cards/000129/files/45244_22341.html",
     "https://www.aozora.gr.jp/cards/001030/files/4803_14204.html",
]

print("[[[ 青空文庫より ]]]")
print("1. 夏目漱石")
print("2. 芥川龍之介")
print("3. 宮沢賢治")
print("4. 森鴎外")
print("5. 堀辰雄")

book=int(input("誰の作品にしますか(1-5)>>"))
