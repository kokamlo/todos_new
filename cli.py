from func import get_todos , write_todos
import time


now = time.strftime("%Y ,%b %d , %H:%M")
print(now)

while True:
    user_input= input('add , show , edit, complete or exit?\n')
    user_input = user_input.strip()

    if user_input.startswith("add"):
        todo=user_input[4:]
        todos= get_todos()
        todos.append(todo+"\n")
        
        write_todos(todos)

    elif user_input.startswith("show"):
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.strip("\n")  
            row =f"{int(index) +1} -{item}"
            print(row)
    
    elif user_input.startswith("edit"):
        try:
            edit_num = int(user_input[5:])
            edit_num = edit_num -1
            todos = get_todos()        
            new_todo = input("wut u wanna do?")
            todos[edit_num] = new_todo+ "\n"
            
            write_todos( todos)        
        except ValueError:
            print("wrong command!")
            continue
    elif user_input.startswith("complete"):
        try:
            number = int(user_input[9:])
            todos = get_todos()
            done = todos.pop(number-1)

            write_todos( todos)
            print(f"u completed {done} good job !")
        except IndexError:
            print("not in range")
            continue
    elif user_input.startswith("exit"):
        break
        
    else :
        print("worng input")
            
print("bb!")        