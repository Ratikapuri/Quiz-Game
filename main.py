print("WELCOME TO MY COMPUTER QUIZ!")

playing = input("Do you want to Play? ")
print(playing)
if playing.lower() != "yes":
    quit()

print("Okay! Let's Play :) ")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score +=1
else:
    print('Incorrect! ')

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect! ')

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect! ')

answer = input("What does PSU stand for? ")
if answer.lower() == "Power Supply":
    print('Correct!')
    score += 1
else:
    print('Incorrect! ')

print("You got " + str(score) + "questions Correct!")
print("You got " + str((score/4)*100) +  "%.")
