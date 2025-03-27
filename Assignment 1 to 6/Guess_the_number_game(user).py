import random

no_of_rounds = 3
current_round = 0
score = 0

while True:
    current_round += 1
    if current_round > no_of_rounds:
     print("Game over")
     break

    print("-----------High-Low Game------------")
    print("____________________________________")


    my_random_number = random.randint(1,100)
    computer_generated_random_number = random.randint(1,100)

    print("my_random_number",my_random_number)


    high_low_choice = input("What do you think your number is higher or lower than computer's ? high/low ?")  

    print(high_low_choice)

    isuserhigherthancomputer = True if my_random_number > computer_generated_random_number else False
    isuserchoicecorrect = True if (high_low_choice == "high" and isuserhigherthancomputer) or (high_low_choice == "low" and not isuserhigherthancomputer) else False


    print("computer_generated_random_number",computer_generated_random_number)

    if isuserchoicecorrect:
       score += 1
       print("You are right")

    else:
       print("You are wrong") 

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")         

print("Your final score is : ", score)   

print("====================================")  