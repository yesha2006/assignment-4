# Assignment 4 – Files, Exceptions, and Errors in Python

#Task 1: Read a File and Handle Errors

#Problem Statement: 
Write a Python program that opens and reads a text file named `sample.txt`, prints its content line by line, and handles the error if the file does not exist.

#Solution: 
1. Use a `try-except` block to handle potential file errors.  
2. Inside the `try` block, open `sample.txt` in read mode using the `with` statement.  
3. Read the file line by line and display each line using a loop.  
4. If the file does not exist, the `except` block prints a friendly error message.  

#sample output:-
File content:
heyy!!how are you??
I learn python.
I just like to learn new skills


# Task 2: Write and Append Data to a File

Problem Statement:
Write a Python program that takes user input and writes it to a file named `output.txt`, appends additional data to the same file, and reads & displays the final content.

#Solution:
1. Take input from the user.  
2. Open `output.txt` in write mode using `with` and write the input.  
3. Open the file in append mode and add extra content.  
4. Open the file in read mode and display all the content.  
5. Using the `with` statement ensures files are automatically closed after operations.

#sample output:-
Final content of output.txt:
I am IT student.I Just like coding.
Learning file handling in Python.


