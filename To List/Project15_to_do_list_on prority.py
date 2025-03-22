from os import system

todo_list = []
todo_list_priority = {}

def add_task ():
    user_task = input("Enter your Task: ")
    user_task_priority = int(input("Enter your Priority [1 = High , 2 = Medium , 3 = Low]: "))
    if user_task_priority == 1:
        todo_list_priority.update({user_task : "High"})
    elif user_task_priority == 2:
        todo_list_priority.update({user_task : "Medium"})
    elif user_task_priority == 3:
        todo_list_priority.update({user_task : "Low"})
    print("TASK ADDED SUCCESSFULLY !")
    todo_list.append(user_task)
    # system("cls")
    
def view_task ():
    print("Tasks :")
    if not todo_list:
        print("NO TASKS.")
    else:
        priorities = ["High", "Medium", "Low"]
        x=0
        for p in priorities:
            for k,v in todo_list_priority.items():
                if v == p:
                    x+=1
                    print(x, "- [" ,v ,"] " , k )
                
            
        
        # system("cls")
def remove_task ():
    
    print("Enter '0' for back")
    priorities = ["High", "Medium", "Low"]
    x=0
    for p in priorities:
        for k,v in todo_list_priority.items():
            if v == p:
                x+=1
                print(x, "- [" ,v ,"] " , k )
    user_del = int(input("Which Task do you want to delete: "))
    # print(todo_list[user_del-1])
    if user_del == 0:
        pass
    if user_del > len(todo_list):
        print("INVALID INPUT")
        pass
        
    else:
        todo_list_priority.pop(todo_list[user_del-1])
        print("TASK REMOVED SUCCESSFULLY")
        
    
    # system("cls")
    
        

print("TO DO".center(25,"-"))
while True:
    
    print (" _______________________ ")
    print ("*                       *")
    print ("|    1. Add Task        |")
    print ("|    2. View Task       |")
    print ("|    3. Remove Task     |")
    print ("|    4. Exit            |")
    print ("*_______________________*\n")


    user_choice = int(input("Enter your choice: "))
    
    if user_choice == 1:
        system("cls")
        add_task()
    elif user_choice == 2:
        system("cls")
        view_task()
    elif user_choice == 3:
        system("cls")
        remove_task()
    elif user_choice == 4:
        exit()
    
        




