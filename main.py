from stack import Stack
from Queue import Queue
from function import *
exit_program = False
def main():
    global exit_program
    while not exit_program:
        print("\n--- Main Menu ---")
        print("1- Character Analysis")
        print("2- Word Analysis")
        print("3- Stack Operations")
        print("4- Queue Operations")
        print("5- Exit")
        text = input("Enter a text: ")
        operation = input("Choose a task: ")

        if operation == "1":
            Character_Analysis(text)
        elif operation == "2":
            Word_Analysis(text)
        elif operation == "3":
            Stack_Operations(text)
        elif operation == "4":
            Queue_Operations(text)
        elif operation == "5":
            exit_program = True
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
