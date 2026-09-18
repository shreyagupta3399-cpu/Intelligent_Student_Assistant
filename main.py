print("===================================")
print("   INTELLIGENT STUDENT ASSISTANT")
print("===================================")

print("\nWelcome to your Student Assistant!")

# MARKS CALCULATOR
print("\n--- MARKS CALCULATOR ---")

subject1 = float(input("Enter marks in Subject 1 (out of 100): "))
subject2 = float(input("Enter marks in Subject 2 (out of 100): "))
subject3 = float(input("Enter marks in Subject 3 (out of 100): "))

total = subject1 + subject2 + subject3
percentage = total / 3

print("\nTotal Marks:", total, "/ 300")
print("Percentage:", round(percentage, 2), "%")

# ATTENDANCE CALCULATOR
print("\n--- ATTENDANCE CALCULATOR ---")

total_classes = int(input("Enter total classes: "))
attended_classes = int(input("Enter classes attended: "))

if total_classes > 0 and 0 <= attended_classes <= total_classes:
    attendance = (attended_classes / total_classes) * 100
    print("Your attendance:", round(attendance, 2), "%")

    if attendance >= 75:
        print("Your attendance is 75% or above.")
    else:
        print("Your attendance is below 75%.")
else:
    print("Please enter valid class numbers.")

# STUDY PLANNER
print("\n--- STUDY PLANNER ---")

study_hours = float(input("How many hours can you study daily? "))

if study_hours >= 5:
    print("Suggestion: Revise difficult topics and solve practice questions.")
elif study_hours >= 3:
    print("Suggestion: Focus on weak subjects and revise daily.")
elif study_hours > 0:
    print("Suggestion: Make a short timetable and study consistently.")
else:
    print("Please enter a valid number of study hours.")

print("\nThank you for using Student Assistant!")