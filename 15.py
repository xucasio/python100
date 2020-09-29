# 题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示；
# 分析：输入成绩，判断是否为数字，是数字则判定属于哪个等级，若不是数字怎根据代码设定返回重新输入成绩或者直接退出程序；
print('输入成绩查看登记，输入"q"则退出')
while True:
    score = input('输入你的成绩:')

    if score.isdigit():

        score_rank = int(score) // 10

        if score_rank >= 9:
            print('A')
        elif score_rank >= 6 and score_rank < 9:
            print('B')
        else:
            print('C')
    elif score == 'q':
        break
    else:
        print('输入错误，请重新输入！')