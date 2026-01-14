import random

capitals = {...}

issue = input("問題集を作成する数を指定してください>>")

#問題集を作成する
for quiz_num in range(issue):
    #問題集を回答集のファイルを作成
    quiz_file = open(f"capitalquiz{quiz_num+1}.txt", "w")
    answer_key_file = open(f"answerkey{quiz_num+1}.txt", "w")
    #問題集の順番をシャッフルする
    prefectures = list(capitals.keys())
    random.shuffle(prefectures)
    #47都道府県をループしてそれぞれ問題集を作成する
    for prefecture in range(len(prefectures)):
        #問題文と解答の選択肢を問題ファイルに出力する

        #答えの選択肢を解答ファイルに出力する