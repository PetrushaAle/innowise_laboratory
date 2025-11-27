from typing import List, Dict, Optional


def find_student(students: List[Dict], name: str) -> Optional[Dict]:
    """Найти студента по имени (регистронезависимо). Возвращает словарь или None."""
    name_lower = name.strip().lower()
    for s in students:
        if s.get("name", "").strip().lower() == name_lower:
            return s
    return None


def add_student(students: List[Dict]) -> None:
    name = input("Enter student name: ").strip()
    if not name:
        print("Имя не может быть пустым.")
        return
    if find_student(students, name) is not None:
        print(f"Студент '{name}' уже существует.")
        return
    students.append({"name": name, "grades": []})
    print(f"Студент '{name}' добавлен.")


def enter_grades(students: List[Dict]) -> None:
    name = input("Enter student name: ").strip()
    if not name:
        print("Имя не может быть пустым.")
        return
    student = find_student(students, name)
    if student is None:
        print(f"Студент '{name}' не найден.")
        return

    print("Enter a grade (or 'done' to finish):")
    while True:
        raw = input().strip()
        if raw.lower() == "done":
            print("Ввод оценок завершён.")
            break
        try:
            grade = int(raw)
            if grade < 0 or grade > 100:
                print("Оценка должна быть в диапазоне 0-100. Попробуйте снова.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")
            continue
        student["grades"].append(grade)
        print(f"Оценка {grade} добавлена для {student['name']}.")


def average(grades: List[int]) -> float:
    """Вычисляет среднее списка оценок. Предполагается grades не пустой."""
    return sum(grades) / len(grades)


def generate_report(students: List[Dict]) -> None:
    print("--- Student Report ---")
    if not students:
        print("Нет студентов для отчёта.")
        return

    averages = []
    for s in students:
        try:
            if not s.get("grades"):
                print(f"{s['name']}'s average grade is N/A.")
            else:
                avg = average(s["grades"])
                averages.append(avg)
                print(f"{s['name']}'s average grade is {avg:.1f}.")
        except ZeroDivisionError:
            print(f"{s['name']}'s average grade is N/A.")

    if averages:
        max_avg = max(averages)
        min_avg = min(averages)
        overall_avg = sum(averages) / len(averages)
        print("---")
        print(f"Max Average: {max_avg:.1f}")
        print(f"Min Average: {min_avg:.1f}")
        print(f"Overall Average: {overall_avg:.1f}")
    else:
        print("Нет доступных средних для расчёта (нет оценок у студентов).")


def find_top_student(students: List[Dict]) -> None:
    if not students:
        print("Нет студентов в системе.")
        return

    def student_avg(s: Dict) -> Optional[float]:
        grades = s.get("grades", [])
        if not grades:
            return None
        return average(grades)

    students_with_avg = [s for s in students if student_avg(s) is not None]

    if not students_with_avg:
        print("Нет студентов с оценками для поиска топ-студента.")
        return

    top = max(students_with_avg, key=lambda s: student_avg(s) or 0)
    top_avg = student_avg(top)
    print(f"Top student: {top['name']} with average {top_avg:.1f}.")


def print_menu() -> None:
    print()
    print("--- Student Grade Analyzer ---")
    print("1. Add a new student")
    print("2. Enter grades for a student")
    print("3. Generate report")
    print("4. Find top student")
    print("5. Exit")
    print()


def main() -> None:
    students: List[Dict] = []

    while True:
        try:
            print_menu()
            choice_raw = input("Enter your choice: ").strip()
            if not choice_raw:
                print("Пожалуйста, введите номер опции.")
                continue
            try:
                choice = int(choice_raw)
            except ValueError:
                print("Неверный ввод. Введите номер опции (1-5).")
                continue

            if choice == 1:
                add_student(students)
            elif choice == 2:
                enter_grades(students)
            elif choice == 3:
                generate_report(students)
            elif choice == 4:
                find_top_student(students)
            elif choice == 5:
                print("Exiting program.")
                break
            else:
                print("Неверный выбор. Пожалуйста, выберите опцию 1-5.")
        except KeyboardInterrupt:
            print("\nInterrupted. Exiting program.")
            break
        except Exception as e:
            print(f"Произошла ошибка: {e}. Попробуйте снова.")


if __name__ == "__main__":
    main()
