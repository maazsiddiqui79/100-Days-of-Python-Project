import random
print('''

 __   _ _     _ _______ ______  _______  ______     
 | \  | |     | |  |  | |_____] |______ |_____/     
 |  \_| |_____| |  |  | |_____] |______ |    \_     
                                                         
                         ______ _     _ _______ _______ _______ _____ __   _  ______
                         |  ____ |     | |______ |______ |______   |   | \  | |  ____
                         |_____| |_____| |______ ______| ______| __|__ |  \_| |_____|
                         
 ______ _______ _______ _______
 |  ____ |_____| |  |  | |______
 |_____| |     | |  |  | |______
                                                                                                                          

''')
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

user_ip = int(input("Choose Your Diffculty. 1 = 'easy' 2 = 'hard': "))
num = random.randint(1,100)
print(num)

life = 10 if user_ip == 1 else 5
 

        
# game = True
# while game:

print(f"You have {life} attempts remaining to guess the number.")
    
while life != 0:
    user_num_ip = int(input("Guess a Number: "))
    
    if user_num_ip == num-1 or user_num_ip == num+1 :
        print("Too Close!")
    elif user_num_ip < num:
        print("Too Low!")
    elif user_num_ip > num:
        print("Too High!")
    else:
        print("🔥 Bingo! You got the correct number!")
        break
    life -= 1
    print(f"You have {life} attempts remaining to guess the number.")
    if life == 0:
        print("🔴 Game Over! You couldn't guess the right number.")
        break
        
        
