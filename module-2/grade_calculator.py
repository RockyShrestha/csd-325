# grade_calculator.py
# Rakesh Shrestha - CSD-325 Module 2.2

def calculate_average(grades):
    """Calculate the average of a list of grades."""
    if len(grades) == 0:
        return 0
    total = sum(grades)
    average = total / len(grades)
    return average


def get_letter_grade(average):
    """Return a letter grade based on the numeric average."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def display_results(name, grades):
    """Display the student's name, grades, average, and letter grade."""
    average = calculate_average(grades)
    letter = get_letter_grade(average)
    print(f"Student: {name}")
    print(f"Grades: {grades}")
    print(f"Average: {average:.2f}")
    print(f"Letter Grade: {letter}")


def main():
    students = [
        ("Alice Johnson", [92, 88, 95, 91]),
        ("Bob Martinez", [75, 68, 82, 79]),
        ("Carol Smith", [55, 60, 58, 62]),
    ]

    for name, grades in students:
        display_results(name, grades)
        print("-" * 30)


if __name__ == "__main__":
    main()
