# Welcome message
print("Welcome to the console QUIZ...")

# Ask the user if they want to play
playing = input("Do you want to play? ")

if playing.lower() == "yes":

    print("Okay! Let's play")

    # Create a variable that tracks the score
    score = 0

    # Ask the user multiple questions and update their score accordingly
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

    # Print the final score
    print("You got " + str(score) + " questions correct.")
else:
    print("Goodbye!")
    quit()
