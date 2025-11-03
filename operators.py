Operators problmes and solutions 

1.Operators - Fencing and Carpet Calculation for a Fighting Ground
The Fencing and Carpet Calculation for a Fighting Ground program is designed to calculate the perimeter and area of a rectangular
fighting arena using arithmetic operators. The user provides the length and width of the ground as input, and the program outputs:
The total length of fencing required (perimeter).
The amount of carpet or mat area needed to cover the ground (area)

solution :
length = int(input())
breadth = int(input())

# Calculate perimeter (length of rope for fence)
perimeter = 2 * (length + breadth)

# Calculate area (carpet area)
area = length * breadth

# Display results
print(f"The required length is {perimeter} m")
print(f"The required area of carpet is {area} sqm")



2.Operators - Fitness App
The Fitness App program uses operators to perform essential health and fitness calculations based on user input. The app can 
compute values such as Body Mass Index (BMI), calories burned, or dailystep goals depending on the data entered by the user.

solution :
N = int(input())
seconds = N * 60
print(seconds)



3.Operators - Leena's Business Loan
The Leena’s Business Loan program helps calculate the total repayment amount and monthly installment (EMI) for a business loan using 
arithmetic operators. The user inputs the loan amount, interest rate, and loan duration (in years), 
and the program computes how much Leena needs to repay in total.

solution :
principal = float(input())
rate = float(input())
years = float(input())

# Calculate simple interest
interest = (principal * rate * years) / 100

# Calculate total amount (principal + interest)
total_amount = principal + interest

# Calculate discount (2% of interest)
discount = 0.02 * interest

# Calculate final settlement amount after discount
final_settlement = total_amount - discount

# Print results formatted to 2 decimal places
print(f"Interest: {interest:.2f}")
print(f"Total Amount: {total_amount:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Final Settlement Amount: {final_settlement:.2f}")



4.Operators - Opening the Enchanted Door
The Opening the Enchanted Door program is a magical-themed project that uses arithmetic and logical operators to determine whether a secret door
can be unlocked. The user enters a set of mystery numbers or keys, and the program performs mathematical and logical operations
to check if the correct unlocking condition is met.

solution :
number = input()

# Extract first and last digits
first_digit = int(number[0])
last_digit = int(number[-1])

# Calculate sum
result = first_digit + last_digit

print(result)



5.Operators - Profit Calculation for The Herald Newspaper
The Profit Calculation for The Herald Newspaper program is designed to compute the daily or monthly profit earned by the newspaper company
using arithmetic operators. The user provides inputs such as cost price per copy, selling price per copy, and number of copies sold. The program then calculates 
the total profit or loss and displays the result clearly.

solution :
a = int(input())
b = int(input())
c = int(input())

# Calculate total revenue
total_revenue = a * b

# Calculate total cost (printing cost + fixed overhead)
total_cost = (a * c) + 100

# Calculate profit
profit = total_revenue - total_cost

print(profit)







