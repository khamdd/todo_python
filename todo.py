import json
from datetime import datetime

def menu():
    print("1: Create a new task")
    print("2: View all tasks")
    print("3: Edit a task")
    print("4: Delete a task")
    print("q: Exit")
    choice = input("Enter a number: ")
    return choice

class Data:
    def __init__(self, name, detail, dueDate, priority):
        self.name = name
        self.detail = detail
        self.dueDate = dueDate
        self.priority = priority
    def to_dict(self):
        return {
            "name": self.name,
            "detail": self.detail,
            "dueDate": self.dueDate,
            "priority": self.priority
        }
choice = menu()

def write_file(data: Data):
    with open("data.json", "a") as file:
        json.dump(data.to_dict(), file)

def dateValidation(input):
    date_format = '%d/%m/%Y'

    try:
        datetime.strptime(input, date_format)
        return True
    except ValueError:
        return False

try:
    choice = int(choice)
    
except ValueError:
    if(choice == 'q'):
        print("Exiting...")
        exit()
    else:
        print("Invalid choice")
        exit()

if(choice == 1):
    task = input("Enter the task name: ")
    detail = input("Enter the task detail: ")
    dueDate = input("Enter the due date: ")

    while(dateValidation(dueDate) == False):
        print("Invalid date format")
        dueDate = input("Enter the due date: ")

    priority = input("Enter the priority: ")

    data = Data(task, detail, dueDate, priority)

    # Writing to sample.json
    with open("data.json", "a") as file:
        json.dump(data.to_dict(), file)
elif(choice == 2):
    pass
elif(choice == 3):
    pass
elif(choice == 4):
    pass
else:
    print("Invalid choice")
