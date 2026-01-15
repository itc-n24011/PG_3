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
    for question_num in range(len(prefectures)):
        #正解と誤答を取得する
    correct_answer = capitals[prefectures[question_num]]
    wrong_answers = list(capitals.values())
    del wrong_answers[wrong_answers.index(correct_answer)]
    wrong_answers = random.sample(wrong_answers, 3)
    anwser_options = wrong_answers + [correct_answer]
    random.shuffle(anwser_options)
    #問題文と解答の選択肢を問題ファイルに出力する
    quiz_file.write(f"{question_num + 1}, ")
    quiz_file.write(prefectures[question_num] )
    quiz_file.write("の都道府県庁所在地は？\n")
    for i in range(4):
        quiz_file.write(f' {"ABCD"[i]}, answer_options[i]\n')
    quiz.file.write('\n')

    quiz.file.close()
    answer_key_file.close
        #答えの選択肢を解答ファイルに出力する