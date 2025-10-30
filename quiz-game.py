print ("Welcome to BARZZ- The Quiz Game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print ("Let's play :)")
score =0

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print ("That's correct!\n Next question:")
    score += 1

else: 
    print ("That's wrong. Better luck next time.\nCorrect Answer is " \
    "Central Processing Unit.")

answer = input ("What types of jobs exist in Jenkins? ")

if answer == "2":
    print ("That's correct!\n Next question")
    score += 1

else: 
    print ("That's wrong. Better luck next time.\nCorrect Answer is " \
    "2.")

answer = input ("What is GPU? ")

if answer.lower() == "Graphical Processing Unit":
    print ("That's correct!\n Next question")
    score += 1

else: 
    print ("That's wrong. Better luck next time.\nCorrect Answer is " \
    "Graphical processing Unit.")

answer = input ("What is RAM? ")

if answer.lower() == "random access memory":
    print ("That's correct!\n Next question")
    score += 1

else: 
    print ("That's wrong. Better luck next time.\nCorrect Answer is " \
    "Random Access Memory.")

answer = input ("Is an array a data structure? ")

if answer.lower() == "yes":
    print ("That's correct!")
    score += 1

else: 
    print ("That's wrong. Better luck next time.\nCorrect Answer is " \
    "yes.")
    

print ("Thanks for Playing\nYou got: " + str(score) + " questions correct.")
print ("You got " + str((score/5)*100) + "%.")



