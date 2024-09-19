***
Write a program to check whether the given character is vowel or consonant.
Input format:
The input consist of a character
Output format:
The output consists of a below-given string
“Vowel” / “Consonant” / “Not an alphabet”
Sample Input:
e

Sample Output:
Vowel
3)The newly appointed Vice-Chancellor of Anna University wanted to create an automated grading system for the students to check their grade. When a student enters a mark, the grading system displays the corresponding grade.
Write a program to solve the given problem.
  Marks scored  
  Grade 
100
S
90 - 99
A
80 - 89
B
70 - 79
C
60 - 69
D
50 - 59
E
<50
F

Input format:
The input consists of one integer which corresponds to the marks scored by the student

Output format:
If a student marks greater than 100, print "Invalid Input". Otherwise, print the grade.
Sample Input:
78
Sample Output:C

***
def check_character():
    # Get character input from the user
    char = input().strip()
    
    # Check if the input is a single character
    if len(char) != 1:
        print("Not an alphabet")
        return
    
    # Check if the character is an alphabet
    if char.isalpha():
        # Check if it's a vowel
        if char.lower() in 'aeiou':
            print("Vowel")
        else:
            print("Consonant")
    else:
        print("Not an alphabet")

if __name__ == "__main__":
    check_character()
