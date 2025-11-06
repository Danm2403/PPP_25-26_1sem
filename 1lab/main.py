

if __name__ == "__main__":
    students = ["Зайцев", "Белов", "Громов", "Орлов", "Соколов", 
           "Лебедев", "Воробьёв", "Соловьёв", "Жуков", "Волков"]

# Матрица оценок 10 студентов × 5 предметов
grades = [
    [4, 3, 4, 5, 4],  # Зайцев
    [3, 4, 3, 3, 4],  # Белов
    [5, 5, 4, 5, 5],  # Громов
    [3, 2, 3, 4, 3],  # Орлов
    [4, 4, 3, 4, 4],  # Соколов
    [2, 3, 2, 3, 2],  # Лебедев
    [5, 4, 5, 4, 4],  # Воробьёв
    [3, 3, 3, 3, 4],  # Соловьёв
    [4, 5, 4, 4, 5],  # Жуков
    [2, 2, 2, 3, 2]   # Волков
]

# 1. Средняя оценка каждого студента
print("Средние оценки студентов:")
for i in range(len(students)):
    avg_grade = sum(grades[i]) / len(grades[i])
    print(f"{students[i]}: {avg_grade:.2f}")

print("\n" + "="*50)

# 2. Самая высокая и низкая оценка по каждому предмету
subjects = ["Математика", "Физика", "Химия", "История", "Программирование"]
print("\nЛучшие и худшие оценки по предметам:")
for j in range(len(grades[0])):
    subject_grades = [grades[i][j] for i in range(len(students))]
    max_grade = max(subject_grades)
    min_grade = min(subject_grades)
    print(f"{subjects[j]}: макс = {max_grade}, мин = {min_grade}")

print("\n" + "="*50)

# 3. Студент с лучшими и худшими средними баллами
avg_grades = []
for i in range(len(students)):
    avg = sum(grades[i]) / len(grades[i])
    avg_grades.append((students[i], avg))

# Сортируем по среднему баллу
avg_grades.sort(key=lambda x: x[1])

best_student = avg_grades[-1]  # последний в отсортированном списке
worst_student = avg_grades[0]  # первый в отсортированном списке

print(f"\nЛучший студент: {best_student[0]} со средним баллом {best_student[1]:.2f}")
print(f"Худший студент: {worst_student[0]} со средним баллом {worst_student[1]:.2f}")


