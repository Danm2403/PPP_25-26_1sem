

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

# Дополнительно: выведем всех студентов по убыванию успеваемости
print("\nРейтинг студентов:")
for i, (student, avg) in enumerate(reversed(avg_grades), 1):
    print(f"{i}. {student}: {avg:.2f}")

# Ещё дополнительная информация - статистика по группе
print("\n" + "="*50)
all_grades = [grade for student_grades in grades for grade in student_grades]
avg_group = sum(all_grades) / len(all_grades)
print(f"Средний балл по группе: {avg_group:.2f}")
print(f"Всего студентов: {len(students)}")
print(f"Отличников (средний ≥ 4.5): {len([avg for _, avg in avg_grades if avg >= 4.5])}")
print(f"Хорошистов (средний 3.5-4.49): {len([avg for _, avg in avg_grades if 3.5 <= avg < 4.5])}")
print(f"Троечников (средний 2.5-3.49): {len([avg for _, avg in avg_grades if 2.5 <= avg < 3.5])}")
print(f"Неуспевающих (средний < 2.5): {len([avg for _, avg in avg_grades if avg < 2.5])}")
