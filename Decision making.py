Decision-Making Problems
1.Decision Making - Rock, Paper, Scissors
Simulate the classic Rock-Paper-Scissors game using user inputs. Determine who wins using nested if–else statements.

solution : 
M = input()

if M == "rock":
    print("Paper")
elif M == "paper":
    print("Scissors")
elif M == "scissors":
    print("Rock")





2.Decision Making – Car Rental Charges for a Travel Agency
Calculate the total rental cost based on the type of car (e.g., sedan/SUV) and number of days, applying discount slabs.

solution :
import math

R1 = int(input())
N = int(input())
R2 = int(input())
X = int(input())

# Convert minutes to hours (round up using ceiling)
total_hours = math.ceil(X / 60)

# Calculate cost
if total_hours <= N:
    # All hours charged at R1 rate
    total_cost = total_hours * R1
else:
    # First N hours at R1, remaining at R2
    cost_first_n_hours = N * R1
    remaining_hours = total_hours - N
    cost_remaining_hours = remaining_hours * R2
    total_cost = cost_first_n_hours + cost_remaining_hours

print(total_cost)




3.Decision Making – Choosing the Tallest Skyscraper
Given heights of several skyscrapers, use if–else to find and print the tallest one.
Concepts: Nested comparison, max logic without using built-in max().

solution :
heights = list(map(int, input().split()))
print(max(heights))




4.Decision Making – Calculating Daily Profit or Loss Percentage
Accept cost price and selling price, then calculate whether there is profit, loss, or no change, along with percentage.
Concepts: Mathematical conditions, percentage formula inside if–else.

solution :
invested = int(input())
earned = int(input())

if invested < 0 or earned < 0:
    print("Invalid Input")
elif earned > invested:
    profit = earned - invested
    profit_percentage = int((profit / invested) * 100)
    print(f"Profit - {profit_percentage}%")
elif earned < invested:
    loss = invested - earned
    loss_percentage = int((loss / invested) * 100)
    print(f"Loss - {loss_percentage}%")
else:
    print("No Profit, No Loss")




5.Decision Making – Movie Ticket Price Calculator
Determine movie ticket price based on age and time slot (matinee or evening), using multiple if–elif–else cases.
Concepts: Multiple branching logic, nested condition handling.

solution :
age = int(input())
show_time = float(input())

if show_time == 13.30:
    # Matinee show - special price for everyone
    price = 2.00
elif age > 13:
    # Adult price for non-matinee shows
    price = 5.00
else:
    # Child price for non-matinee shows
    price = 3.00

print(f"${price:.2f}")
