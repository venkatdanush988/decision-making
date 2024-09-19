***
There are 3 labs in the CSE department are L1, L2, and L3 with a seating capacity of x, y, and z respectively. One of the 3 labs has been allocated for ACE training. Out of the available labs, find the lab which has minimal seating capacity.
Input format:
Input consists of 3 integers and a string
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
The fourth input denotes the lab which is allocated for ACE training
Output format:
Print the minimal seating capacity lab amongst the available labs.
Refer the Sample output for formatting
Sample Input:
30
40
20
L3
Sample Output:
L1


***
def find_min_lab(a, b, c, allocated_lab):
    # Create a dictionary to hold lab capacities
    lab_capacities = {
        "L1": a,
        "L2": b,
        "L3": c
    }

    # Remove the allocated lab from consideration
    if allocated_lab in lab_capacities:
        del lab_capacities[allocated_lab]

    # Find the lab with the minimal capacity from the remaining labs
    min_lab = min(lab_capacities, key=lab_capacities.get)
    return min_lab

# Input reading
capacity_L1 = int(input().strip())
capacity_L2 = int(input().strip())
capacity_L3 = int(input().strip())
allocated_lab = input().strip()

# Determine the lab with minimal seating capacity
min_lab = find_min_lab(capacity_L1, capacity_L2, capacity_L3, allocated_lab)

# Output result
print(min_lab)
