print("Welcom to our Quiz Game")

answer = input("You want to play ? yes or no ? ")

if answer != "yes":
    quit()

commonOptionList = ["None","all","both"]

questionList = ["html stands for ?",
                "cup stands for ?",
                "css stands for ?",
                "computer is  ",
                "window is "]

optionList = [[["host text make language"],["hide tool made language"],["hyper text markup language"],["head transfer mode line"]],
              [["central processing unit"],["central program unit"],[commonOptionList[2]],[commonOptionList[0]]],
              [["cascading style sheet"],["cat style slide"],["comman styling slide"],[commonOptionList[0]]],
              [["Electronic device"],["machanical device"],["robotic device"],[commonOptionList[1]]],
              [["Operating System"],["System Software"],["software to control hardware"],[commonOptionList[1]]],]

correctAnswerList = [3,1,1,1,4]

answerList = []

for i in range(0,5):
    print((i+1),questionList[i]," \n Option Are.....")
    for j in range(0,4):
        print((j+1),optionList[i][j])
    answer = int(input("Answer : "))
    answerList.append(answer)

total = 0
for i in range(0,5):
    if correctAnswerList[i] == answerList[i] :
        total = total + 1

if total == 5:
    print("All Answer are correct :)")
elif total == 0:
    print("All answer are incorrect ")
else:
    print("You have enter ",total," correct answer")