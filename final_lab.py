***
 There are 3 labs in the CSE department. The labs are L1, L2, and L3 with a seating capacity of x, y, and z respectively. A single lab needs to be allocated to a class of 'n' students. The labs need to be utilized to the maximum i.e the number of systems used should not be minimal. Which lab needs to be allocated to this class?
Input format:
Input consists of 4 integers
The first input denotes 'x'
The second input denotes 'y'
The third input denotes 'z'
The fourth input denotes 'n'
Output format:
Print the lab which is suitable for  'n' number of students
Refer the Sample output for formatting
Sample Input:
30
40
20
25
Sample Output:
L1

***
def find_best_lab(x, y, z, n):
    # Initialize variables to keep track of the best lab and maximum utilization
    best_lab = None
    max_utilization = -1

    # Check each lab and its capacity
    for lab, capacity in zip(["L1", "L2", "L3"], [x, y, z]):
        if capacity >= n:
            utilization = capacity - n
            if utilization > max_utilization:
                max_utilization = utilization
                best_lab = lab

    return best_lab

# Input reading
capacity_L1 = int(input().strip())
capacity_L2 = int(input().strip())
capacity_L3 = int(input().strip())
num_students = int(input().strip())

# Determine the best lab for allocation
suitable_lab = find_best_lab(capacity_L1, capacity_L2, capacity_L3, num_students)

# Output result
print(suitable_lab)
