
import csv

# Fictional Student Dataset
students = [
    ["STU001", "Computer Science", 300, 85, 78],
    ["STU002", "Cyber Security", 200, 90, 82],
    ["STU003", "Software Engineering", 300, 75, 69],
    ["STU004", "Computer Science", 100, 95, 88],
    ["STU005", "Information Technology", 200, 80, 74],
    ["STU006", "Cyber Security", 300, 70, 65],
    ["STU007", "Computer Science", 200, 88, 91],
    ["STU008", "Software Engineering", 100, 92, 85],
    ["STU009", "Information Technology", 300, 78, 72],
    ["STU010", "Computer Science", 100, 82, 80],
    ["STU011", "Cyber Security", 200, 86, 77],
    ["STU012", "Software Engineering", 300, 90, 89],
    ["STU013", "Information Technology", 100, 76, 68],
    ["STU014", "Computer Science", 300, 93, 95],
    ["STU015", "Cyber Security", 100, 84, 81]
]

# Create a CSV file
with open("student_dataset.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Student ID",
        "Department",
        "Level",
        "Attendance Percentage",
        "Average Examination Score"
    ])

    writer.writerows(students)

print("Student dataset created successfully!")
