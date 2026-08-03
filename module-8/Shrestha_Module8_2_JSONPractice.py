"""
===============================================================================
Course:         CSD325-T301 Advanced Python
Assignment:     Module 8.2 - JSON Practice
Author:         Rakesh Shrestha
Date:           08/02/2026
Description:    Loads student data from student.json, prints the original
                list, appends a new student record, prints the updated
                list, then writes the updated list back to student.json.
===============================================================================
"""

import json

# Path to the JSON file used for this assignment
JSON_FILE = "student.json"


def print_students(student_list):
    """
    Loop through the list of student dictionaries and print each
    record in the format: LastName, FirstName : ID = #### , Email = ...
    """
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : "
              f"ID = {student['Student_ID']} , Email = {student['Email']}")


def main():
    # Step 1: Load the JSON file into a Python list using json.load()
    with open(JSON_FILE, "r") as infile:
        students = json.load(infile)

    # Step 2: Print the original student list
    print("Original Student List:")
    print_students(students)

    # Step 3: Append a new student record to the list
    new_student = {
        "F_Name": "Rakesh",
        "L_Name": "Shrestha",
        "Student_ID": 70921,
        "Email": "rshrestha@bellevue.edu"
    }
    students.append(new_student)

    # Step 4: Print the updated student list
    print("\nUpdated Student List:")
    print_students(students)

    # Step 5: Write the updated list back out to the JSON file using json.dump()
    with open(JSON_FILE, "w") as outfile:
        json.dump(students, outfile, indent=4)

    print("\nstudent.json has been updated with the new record.")


if __name__ == "__main__":
    main()
