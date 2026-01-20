marks = [45, 67, 89, 34, 56, 98, 21, 74, 65, 87,
         90, 55, 32, 46, 78, 88, 93, 35, 40, 62]  

total_students = len(marks)
highest = max(marks)
lowest = min(marks)
average = sum(marks) / total_students


passed = sum(1 for m in marks if m >= 33)
failed = total_students - passed
pass_percentage = (passed / total_students) * 100


sorted_marks = sorted(marks)


grade_A = sum(1 for m in marks if m >= 90)
grade_B = sum(1 for m in marks if 75 <= m < 90)
grade_C = sum(1 for m in marks if 60 <= m < 75)
grade_D = sum(1 for m in marks if 33 <= m < 60)
grade_F = failed


print("\n=========== STUDENT MARKS REPORT ===========\n")
print("Total Students:", total_students)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", round(average, 2))
print("Passed:", passed)
print("Failed:", failed)
print("Pass Percentage:", str(round(pass_percentage, 2)) + "%")
print("Sorted Marks:", sorted_marks)
print("Grade A:", grade_A, "Students")
print("Grade B:", grade_B, "Students")
print("Grade C:", grade_C, "Students")
print("Grade D:", grade_D, "Students")
print("Grade F:", grade_F, "Students")
print("\n============================================\n")