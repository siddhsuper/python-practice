# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()

# 🚨 Don't change the code above 👆

# Write your code below this row 👇
high_score = 0
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    if(high_score < student_scores[n]):
        high_score = student_scores[n]
print(student_scores)
print(f"The highest score in the class is: {high_score}")
