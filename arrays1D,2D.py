Arrays 1D ,2D problems and solutions 
Arrays 1D - Insertion of New Product IDs
A retail company stores all its product IDs in a list (1D array).
When a new product is added to the inventory, the company needs to insert its Product ID into the existing list at a specified position.

solution :
n = int(input()) # no of student id's 5
l= list(map(int,input().split())) # student id's 101 105 110 120 130 
new_ele = int(input()) #107

l.append(new_ele) # 101 105 120 130 107

l.sort() # 101 105 107 110 120 130 

print(*l) # 101 105 107 110 120 130 



2.Arrays 1D - Data Recovery - Reversing the Sensor Log
A research laboratory collects sensor readings continuously and stores them in a system log (a 1D array).
Due to a system crash, the data log got jumbled, and the recovery team found that the readings are stored in reverse order.

solution :
n = int(input())
readings = list(map(int, input().split()))

# Reverse the array
readings.reverse()

# Print the reversed readings
print(' '.join(map(str, readings)))



3.Arrays 2D - Merging Attendance Records
A school maintains attendance records for students in different classes.
Each class has its own record showing whether students were present (1) or absent (0) on a given day.
The school management wants to combine (merge) the attendance data of two classes to analyze the overall presence of students.

solution :
# Read dimensions
classes, days = map(int, input().split())

# Read first week's matrix
matrix1 = []
for i in range(classes):
    row = list(map(int, input().split()))
    matrix1.append(row)

# Read second week's matrix
matrix2 = []
for i in range(classes):
    row = list(map(int, input().split()))
    matrix2.append(row)

# Add matrices element-wise and print result
for i in range(classes):
    result_row = []
    for j in range(days):
        sum_value = matrix1[i][j] + matrix2[i][j]
        result_row.append(str(sum_value))
    print(' '.join(result_row) + ' ')



4.Arrays 2D - Power Grid Monitoring - Computing Diagonal Load Balances
An electric power station monitors the load distribution across its regional grid.
The grid is represented as a square matrix, where each element denotes the power load (in megawatts) at a specific junction.

solution : 
n = int(input())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

primary_sum = 0
secondary_sum = 0

for i in range(n):
    primary_sum += matrix[i][i]
    secondary_sum += matrix[i][n - 1 - i]

print(primary_sum, secondary_sum)




5.Arrays 2D - Security Camera Image Processing System
A security company uses multiple CCTV cameras to monitor activity in restricted areas.
Each camera captures a grayscale image, which is represented as a 2D matrix, where every element denotes the pixel intensity 
(ranging from 0 to 255).

solution : 
n = int(input())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Step 1: Flip each row horizontally (reverse)
for i in range(n):
    matrix[i].reverse()

# Step 2: Invert each pixel (0 -> 1, 1 -> 0)
for i in range(n):
    for j in range(n):
        matrix[i][j] = 1 - matrix[i][j]

# Print the result
for i in range(n):
    print(' '.join(map(str, matrix[i])) + ' ')




