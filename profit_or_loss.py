***

4) A fruit seller buys a dozen of banana at Rs.X. He sells 1 banana at Rs.Y. Write a program to determine the profit or loss in Rs. for the fruitseller.
Input format:
Input consists of 2 floating point numbers
The first input corresponds to the total cost(X)
The second input corresponds to the sold cost(Y)
Output format:
Print "Profit or Loss" with Rupees.
Sample Input:
60
4
Sample Output:
Loss : Rs.12.00
***
# Function to calculate profit or loss
def calculate_profit_or_loss(total_cost, sold_price_per_banana):
    # Cost per banana
    cost_per_banana = total_cost / 12
    # Selling price for a dozen bananas
    total_selling_price = sold_price_per_banana * 12
    
    # Calculate profit or loss
    profit_or_loss = total_selling_price - total_cost
    
    return profit_or_loss

# Input reading
total_cost = float(input())
sold_price_per_banana = float(input())

# Calculate profit or loss
result = calculate_profit_or_loss(total_cost, sold_price_per_banana)

# Output result
if result > 0:
    print(f"Profit : Rs.{result:.2f}")
elif result < 0:
    print(f"Loss : Rs.{abs(result):.2f}")
else:
    print("No Profit No Loss")
