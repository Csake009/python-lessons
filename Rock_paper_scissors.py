import random
Epiloges = ["rock", "paper", "scissors"]
for i in range(3):
    secret = random.randrange(0,3)
    #print(Epiloges[secret])
    guess =  input("Διλαεξε rock, paper ή scissors: ")
    print(guess, Epiloges[secret])
    if guess == Epiloges[secret]:
        print("Ισοπαλία")

    if guess == "paper":
        if Epiloges[secret] == "rock":
            print("Με κέρδισες")
        elif Epiloges[secret] == "scissors":
            print("Σε κέρδισα")


    if guess == "rock":
        if Epiloges[secret] == "scissors":
            print("Με κέρδισες")
        elif Epiloges[secret] == "paper":
            print("Σε κέρδισα")


    if guess == "scissors":
        if Epiloges[secret] == "paper":
            print("Με κέρδισες")
        elif Epiloges[secret] == "rock":
            print("Σε κέρδισα")