import math
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
total_heights = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    total_heights += student_heights[n]
# 🚨 Don't change the code above 👆
print(
    f"Average Student Height is : {math.ceil(total_heights/len(student_heights))}")

# Write your code below this row 👇
