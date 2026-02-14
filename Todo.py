to_do = []
print("=== Welcome to the TO-DO LIST ===")


print("=== MAIN MENU ===")
print("1. Add New Task")
print("2. Remove Task")
print("3. Edit Task")
print("4. Mark task as completed")
print("5. Exist")

while True:
    x = int(input("Enter your choice (1-5): "))

    def add(to_do):
        thing = input("What would you like to add? ")
        to_do.append(thing)
        print("Successfully added")
        print(to_do)
    def remove(to_do):
        thing_to_remove = input("What would you like to remove? ")
        to_do.remove(thing_to_remove)
        print("successfully removed")
        print(to_do)
    def edit(to_do):
        num = int(input("what task number would you like to edit"))
        new_task = input("add new task")
        past_task = to_do.pop(num - 1)
        to_do.insert(num - 1, new_task)
        print("task edited")
        print(to_do)
    def complete(to_do):
        complete_task = input("Enter the value you want to complete: ")   
        to_do.remove(complete_task)
        print("Task completed")
        print(to_do)
        


    if x == 1:
        add(to_do)
    elif x == 2:
        remove(to_do)
    elif x == 3:
        edit(to_do)
    elif x == 4:
        complete(to_do)
    elif x == 5:
        break
     
