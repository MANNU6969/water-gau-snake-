import random
'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice (snake/water/gun): ")
youDict = {"s":1, "w":-1, "g":0}
reverseDict = {1:"s", -1:"w", 0:"g"}
you = youDict[youstr]

# ny now we have 2 numbers (variables ), you and computer!
print(f"you choose {reverseDict[you]}\ncomputer choose {reverseDict[computer]}")

# if(computer == you):
#     print("It's a tie!")
# else:
#     if((computer - you) == -1 or (computer - you) == 2):
#         print("You loose")
#     else:
#         print("You win")
# this is a new code which is shorter than this lil harder in read 

if(computer == you):
    print("It's a tie!")
    
else:
    if(computer ==-1 and you ==1):
        print("You win!")
    elif(computer == -1 and you == 0): 
        print("You lose!")
    elif(computer == 1 and you == -1):   
        print("You win!")
    elif(computer == 1 and you == 0):
        print("You win!")
    elif(computer == 0 and you == -1): 
        print("You lose!")
    elif(computer == 0 and you == 1):   
        print("You win!")

    else:
        print("someting went wrong")

# import random

# def determine_winner(player, computer):
#     # Outcome mapping: (player, computer) -> result
#     outcomes = {
#         (1, -1): "You win!",  # Snake beats Water
#         (-1, 1): "You lose!", # Water loses to Snake
#         (1, 0): "You win!",   # Snake beats Gun
#         (0, 1): "You lose!",  # Gun loses to Snake
#         (-1, 0): "You lose!", # Water loses to Gun
#         (0, -1): "You win!"   # Gun beats Water
#     }
#     if player == computer:
#         return "It's a tie!"
#     return outcomes.get((player, computer), "Something went wrong!")

# def main():
#     choices = {"s": 1, "w": -1, "g": 0}
#     reverse_choices = {1: "snake", -1: "water", 0: "gun"}

#     # Get computer's choice
#     computer = random.choice([-1, 0, 1])

#     # Get user's choice
#     youstr = input("Enter your choice (s for snake, w for water, g for gun): ").lower()
#     if youstr not in choices:
#         print("Invalid choice! Please enter 's', 'w', or 'g'.")
#         return

#     you = choices[youstr]

#     # Display choices
#     print(f"You chose {reverse_choices[you]}")
#     print(f"Computer chose {reverse_choices[computer]}")

#     # Determine and display the result
#     result = determine_winner(you, computer)
#     print(result)

# if __name__ == "__main__":
#     main()