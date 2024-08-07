print("Welcome to the console QUIZ...")

playing = input("Do you want to play? ")

if playing.lower() == "yes":

    print("Okay! Let's play")
    
    score = 0

    answer = input("What does CPU stand for? ")
    if answer == "central processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer is Central Processing Unit.")
    
    answer = input("What does GPU stand for? ")
    if answer == "graphics processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer is Graphics Processing Unit.")
    
    answer = input("What does RAM stand for? ")
    if answer == "random access memory":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer is Random Access Memory.")

    print("You got " + str(score) + " questions correct.")
else:
    print("Goodbye!")
    quit()
