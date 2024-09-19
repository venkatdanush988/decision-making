***
There are 3 labs in the CSE department(L1, L2, and L3) with a seating capacity of x, y, and z respectively. Find the lab which has minimal seating capacity.  
Input format:
Input consists of 3 integers
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
Output format:
Print the minimal seating lab capacity
Refer the Sample output for formatting
Sample Input:
30
40
20
Sample Output:
L3

***
def find_min_lab(a, b, c):
    # Find the minimum seating capacity
    if a <= b and a <= c:
        return "L1"
    elif b <= a and b <= c:
        return "L2"
    else:
        return "L3"

# Input reading
capacity_L1 = int(input().strip())
capacity_L2 = int(input().strip())
capacity_L3 = int(input().strip())

# Determine the lab with minimal seating capacity
min_lab = find_min_lab(capacity_L1, capacity_L2, capacity_L3)

# Output result
print(min_lab)
