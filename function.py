from stack import Stack
from Queue import Queue
def Stack_Operations(text):
    stack = Stack()
    while True:
        print("\n--- Stack Operations ---")
        print("1- Push each character of the input string onto the stack")
        print("2- Pop characters from the stack to create the reversed string")
        print("3- Exit from Stack Operations")
        op = input("Enter number of operation: ")

        if op == "1":
            # Push each character of the input string onto the stack
            for char in text:
                stack.push(char)
            print("Characters pushed onto the stack.")
            print(stack.items)
        elif op == "2":
            # Pop characters from the stack to create the reversed string
            reversed_string = ""
            while not stack.is_empty():
                reversed_string += stack.pop()
            print("\nReversed String:")
            print(reversed_string)
        elif op == "3":
            # Exit from Stack Operations
            break
        else:
            print("Invalid option. Please try again.")


def Queue_Operations(text):
    queue = Queue()
    while True:
        print("\n--- Queue Operations ---")
        print("1- Enqueue each word from the input string into the queue")
        print("2- Dequeue words from the queue and print them in FIFO order")
        print("3- Exit from Queue Operations")
        op = input("Enter number of operation: ")

        if op == "1":
            # Split the input into words and enqueue each word into the queue
            words = text.split()
            for word in words:
                queue.enqueue(word)
            print("Words enqueued into the queue.")
        elif op == "2":
            # Dequeue words from the queue and print them in FIFO order
            print("\nWords in FIFO Order:")
            while not queue.is_empty():
                print(queue.dequeue())
        elif op == "3":
            # Exit from Queue Operations
            break
        else:
            print("Invalid option. Please try again.")


def Character_Analysis(text):
    while True:
        print("\n--- Character Analysis ---")
        print("1- Store the input string in an array of characters")
        print("2- Display the frequency of each character")
        print("3- Exit from Character Analysis operation")
        op = input("Enter number of operation: ")

        if op == "1":
            # Store the input string in an array of characters
            char_array = list(text)
            print("Array of characters:", char_array)
        elif op == "2":
            # Determine and display the frequency of each character
            char_frequency = {}
            for char in text:
                char_frequency[char] = char_frequency.get(char, 0) + 1
            print("\nCharacter Frequency Analysis:")
            for char, count in char_frequency.items():
                print(f"'{char}': {count}")
        elif op == "3":
            # Exit from Character Analysis operation
            break
        else:
            print("Invalid option. Please try again.")


def Word_Analysis(text):
    while True:
        print("\n--- Word Analysis ---")
        print("1- Split the input string into individual words")
        print("2- Store unique words in a set")
        print("3- Determine and display the frequency of each word")
        print("4- Search for a specific word in the text")
        print("5- Replace a specific word with another word in the text")
        print("6- Exit from Word Analysis operation")
        op = input("Enter number of operation: ")

        if op == "1":
            # Split the input string into individual words
            words = text.split()
            print("Words:", words)
        elif op == "2":
            # Store unique words in a set
            words = text.split()
            unique_words = set(words)
            print("Unique Words:", unique_words)
        elif op == "3":
            # Determine and display the frequency of each word
            words = text.split()
            word_frequency = {}
            for word in words:
                word_frequency[word] = word_frequency.get(word, 0) + 1
            print("\nWord Frequency Analysis:")
            for word, count in word_frequency.items():
                print(f"'{word}': {count}")
        elif op == "4":
            # Search for a specific word in the text
            search_word = input("Enter the word to search: ")
            words = text.split()
            if search_word in words:
                print(f"'{search_word}' found in the text.")
            else:
                print(f"'{search_word}' not found in the text.")
        elif op == "5":
            # Replace a specific word with another word in the text
            words = text.split()
            original_word = input("Enter the word to replace: ")
            replace_word = input("Enter the new word: ")
            replaced_text = " ".join([replace_word if word == original_word else word for word in words])
            print("Text after replacement:", replaced_text)
        elif op == "6":
            # Exit from Word Analysis operation
            break
        else:
            print("Invalid option. Please try again.")