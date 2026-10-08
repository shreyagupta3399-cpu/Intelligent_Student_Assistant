import random
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

print("==============================================")
print("   AI-BASED INTELLIGENT STUDENT ASSISTANT")
print("==============================================")


# ============================================
# MACHINE LEARNING DATASET
# ============================================

random.seed(42)

X = []
y = []

# Generate synthetic educational data
for i in range(300):

    study_hours = random.randint(1, 8)
    attendance = random.randint(55, 100)
    assignment_score = random.randint(35, 100)
    previous_score = random.randint(35, 95)

    # Academic performance score
    score = (
        0.30 * (study_hours / 8 * 100)
        + 0.25 * attendance
        + 0.20 * assignment_score
        + 0.25 * previous_score
        + random.gauss(0, 6)
    )

    # Performance classes
    if score >= 72:
        performance = 2       # High
    elif score >= 55:
        performance = 1       # Medium
    else:
        performance = 0       # Low

    X.append([
        study_hours,
        attendance,
        assignment_score,
        previous_score
    ])

    y.append(performance)


# ============================================
# TRAINING AND TESTING
# ============================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Decision Tree Machine Learning model
model = DecisionTreeClassifier(
    max_depth=5,
    min_samples_leaf=4,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Test model
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)


print("\n--- MACHINE LEARNING MODEL ---")
print("Algorithm: Decision Tree Classifier")
print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))
print("Model Accuracy:", round(accuracy * 100, 2), "%")

print("\nConfusion Matrix:")
print(cm)


# ============================================
# MARKS CALCULATOR
# ============================================

print("\n--- MARKS CALCULATOR ---")

subject1 = float(
    input("Enter marks in Subject 1 (out of 100): ")
)

subject2 = float(
    input("Enter marks in Subject 2 (out of 100): ")
)

subject3 = float(
    input("Enter marks in Subject 3 (out of 100): ")
)

total = subject1 + subject2 + subject3
percentage = total / 3

print("\nTotal Marks:", total, "/ 300")
print("Percentage:", round(percentage, 2), "%")


# ============================================
# ATTENDANCE CALCULATOR
# ============================================

print("\n--- ATTENDANCE CALCULATOR ---")

total_classes = int(
    input("Enter total classes: ")
)

attended_classes = int(
    input("Enter classes attended: ")
)

if total_classes > 0 and 0 <= attended_classes <= total_classes:

    attendance = (
        attended_classes / total_classes
    ) * 100

    print(
        "Your attendance:",
        round(attendance, 2),
        "%"
    )

    if attendance >= 75:
        print("Your attendance is 75% or above.")
    else:
        print("Your attendance is below 75%.")

else:
    print("Please enter valid class numbers.")
    attendance = 0


# ============================================
# STUDY PLANNER
# ============================================

print("\n--- STUDY PLANNER ---")

study_hours = float(
    input("How many hours can you study daily? ")
)

if study_hours >= 5:

    print(
        "Suggestion: Revise difficult topics "
        "and solve practice questions."
    )

elif study_hours >= 3:

    print(
        "Suggestion: Focus on weak subjects "
        "and revise daily."
    )

elif study_hours > 0:

    print(
        "Suggestion: Make a short timetable "
        "and study consistently."
    )

else:

    print("Please enter a valid number of study hours.")


# ============================================
# AI PERFORMANCE PREDICTION
# ============================================

print("\n--- AI STUDENT PERFORMANCE PREDICTION ---")

assignment_score = float(
    input("Enter your assignment score (0-100): ")
)

previous_score = float(
    input("Enter your previous exam score (0-100): ")
)


student_data = [[
    study_hours,
    attendance,
    assignment_score,
    previous_score
]]


prediction = model.predict(student_data)[0]


if prediction == 0:

    performance = "LOW"

    recommendation = (
        "Increase your study hours, improve "
        "attendance and focus on weak subjects."
    )

elif prediction == 1:

    performance = "MEDIUM"

    recommendation = (
        "Maintain regular study and spend "
        "more time on difficult topics."
    )

else:

    performance = "HIGH"

    recommendation = (
        "Great performance! Maintain your "
        "study routine and practice advanced questions."
    )


print("\nPredicted Performance:", performance)

print(
    "AI Recommendation:",
    recommendation
)


# ============================================
# FINAL MESSAGE
# ============================================

print("\n==============================================")
print(" Thank you for using AI-Based Student Assistant!")
print("==============================================")