
import random
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


paper ="""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""


scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""






# rock,paper,scissor logic


while True:
    print("\nWHAT DO YOU WANT TO CHOOSE")
    user_ip= int(input("Type 1. ROCK\t2. PAPER\t3.SCISSORS\t4.EXIT:\t"))
    computer_ip=random.randint(1,3)
    if user_ip == 1:
        print("You Choose:")
        print(rock)
    elif user_ip == 2:
        print("You Choose:")
        print(paper)
    elif user_ip == 3:
        print("You Choose:")
        print(scissor)
    elif user_ip == 4:
        print("Good Bye  👋")
        exit()
    else:
        print("invalid ip")
        continue
        
        
    print("Computer Choose:")
    if computer_ip == 1:
        print(rock)
    elif computer_ip == 2:
        print(paper)
    else:
        print(scissor)
        
        

    if user_ip == computer_ip:
            print("DRAW 🤝")
            
    elif (user_ip ==1 and computer_ip == 3) or (user_ip ==2 and computer_ip == 1) or (user_ip ==3 and computer_ip == 2):
        print("You Win 🏆".upper())
        
    else:
        print("You loose  😞".upper())
    
    
