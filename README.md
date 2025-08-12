# Project: The Text Processor

**Course:** Data Structures  
**Department:** Data Science and AI  
**Deanship:** Engineering and Intelligent Systems  
**Institution:** University College of Applied Sciences (UCAS)

---

## 🎯 Project Objective

This project explores the practical application of fundamental data structures to solve common text processing problems. The program performs a series of analytical operations on a user-provided text string, utilizing arrays, dictionaries, sets, stacks, queues, and optionally, linked lists.

---

## ✨ Features

The program implements the following functionalities based on user input:

#### 1. Character Analysis
- Stores the input string in a character array (Python list).
- Calculates and displays the frequency of each character using a **Dictionary**.

#### 2. Word Analysis
- Splits the text into individual words, handling punctuation and converting to lowercase for accurate analysis.
- Stores all unique words in a **Set**.
- Calculates and displays the frequency of each word using a **Dictionary**.

#### 3. Stack Operations
- Implements a **Stack** data structure.
- Reverses the input string by pushing each character onto the stack and then popping them off to construct the reversed version.

#### 4. Queue Operations
- Implements a **Queue** data structure.
- Processes words in a "First-In, First-Out" (FIFO) order by enqueuing each word and then dequeuing them for display.

#### 5. Linked List (Optional)
- Implements a simple **Linked List**.
- Stores words in their original order and demonstrates list traversal to display them sequentially.

---

## 🛠️ Data Structures Implemented

- **Array (Python List):** To store the initial characters and words of the string.
- **Dictionary:** For efficient key-value storage of character and word frequencies (O(1) average time complexity for access).
- **Set:** To store unique words and demonstrate efficient membership testing and removal of duplicates.
- **Stack (LIFO):** To reverse the string by leveraging its Last-In, First-Out property.
- **Queue (FIFO):** To process words in their original order by leveraging its First-In, First-Out property.
- **Linked List (Optional):** To demonstrate dynamic memory allocation and node-based data storage and traversal.

---

## 🚀 How to Run the Project

1.  **Prerequisites:** Ensure you have Python (version 3.6 or newer) installed on your system.
2.  **Download/Clone:** Download or clone this repository to your local machine.
3.  **Navigate to Directory:** Open your terminal or command prompt and navigate to the project folder.
    ```sh
    cd path/to/the-text-processor
    ```
4.  **Execute the Script:** Run the program using the following command:
    ```sh
    python main.py
    ```
5.  **Provide Input:** The program will prompt you to enter a string. Type your text and press Enter to see the analysis.

---

## 📋 Sample Output

Below is an example of the program's output for the input string: `Hello world, hello UCAS!`

```
Enter a string of text: Hello world, hello UCAS!

========================================
    Character Frequency Analysis
========================================
'H': 1
'e': 2
'l': 4
'o': 3
' ': 3
'w': 1
'r': 1
'd': 1
',': 1
'U': 1
'C': 1
'A': 1
'S': 1
'!': 1

========================================
      Word Frequency Analysis
========================================
'hello': 2
'world': 1
'ucas': 1

========================================
     Reversed String (using Stack)
========================================
!SACU olleh ,dlrow olleH

========================================
  FIFO Word Order (using Queue)
========================================
hello
world
hello
ucas

========================================
  Linked List Traversal (Optional)
========================================
hello -> world -> hello -> ucas -> None
```

---

## 📁 Project Structure

```
text-processor/
├── main.py          # The main Python script containing all the logic
└── README.md        # This documentation file
```


---

##  deliverables

- **Python Code:** A single Python file (`main.py`) containing the implementation of all described functionalities.
- **Brief Report (Optional):** A document detailing design choices, implementation details, and any challenges encountered during the project.

---

## 🏆 Bonus Points

This section is for any additional features implemented beyond the core requirements.
- *[Describe any bonus features you implemented here, e.g., adding a word count feature, implementing a search/replace function, or allowing the user to choose which analysis to run.]*

---

