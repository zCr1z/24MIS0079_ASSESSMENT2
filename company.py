class Employee:
    def __init__(self, name, department, productivity, attendance, teamwork):
        self.name = name
        self.department = department
        self.productivity = productivity
        self.attendance = attendance
        self.teamwork = teamwork

        # Weighted Score
        self.score = (productivity * 0.5 +attendance * 0.3 +teamwork * 0.2)

        self.rating = self.get_rating()

    def get_rating(self):
        if self.score >= 90:
            return "Excellent"
        elif self.score >= 75:
            return "Good"
        elif self.score >= 60:
            return "Average"
        else:
            return "Poor"


employees = [Employee("Alice", "IT", 95, 90, 85),
    Employee("Bob", "HR", 80, 75, 70),
    Employee("Charlie", "IT", 88, 92, 90),
    Employee("David", "Finance", 60, 65, 70),
    Employee("Eva", "HR", 98, 96, 94),]

print("Employee Details")
for emp in employees:
    print(f"{emp.name} | {emp.department} | Score: {emp.score:.2f} | Rating: {emp.rating}")

# Top 3 Employees
employees.sort(key=lambda x: x.score, reverse=True)

print("\nTop 3 Employees")
for emp in employees[:3]:
    print(f"{emp.name} - {emp.score:.2f}")

# Department-wise Average
dept_scores = {}

for emp in employees:
    if emp.department not in dept_scores:
        dept_scores[emp.department] = []
    dept_scores[emp.department].append(emp.score)

print("\nDepartment-wise Average Scores")
for dept, scores in dept_scores.items():
    print(f"{dept}: {sum(scores)/len(scores):.2f}")
