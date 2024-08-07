print("Welcome to the console QUIZ...")

playing = input("Do you want to play? ")

if playing.lower() == "yes":

    print("Okay! Let's play")
    
    answer = input("What does CPU stand for? ")
    if answer == "central processing unit":
        print("Correct!")
    else:
        print("Incorrect! The correct answer is Central Processing Unit.")
    
    answer = input("What does GPU stand for? ")
    if answer == "graphics processing unit":
        print("Correct!")
    else:
        print("Incorrect! The correct answer is Graphics Processing Unit.")
    
    answer = input("What does RAM stand for? ")
    if answer == "random access memory":
        print("Correct!")
    else:
        print("Incorrect! The correct answer is Random Access Memory.")

else:
    quit()