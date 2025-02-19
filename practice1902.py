
# Розробитисистему управління курсами та оцінками учнів.
# Система повинна включати наступні компоненти:
# 1. Інкапсуляція: Використовувати приватні поля для курсів та студентів, забезпечуючи доступ до даних лише через методи.
#
# 2. Спадкування та поліморфізм: Створити базовий абстрактний клас Course та його підкласи MathCourse і ScienceCourse
# для різних типів курсів.Реалізувати поліморфізм для методів, специфічних для кожного типу курсу.
#
# 3. Абстракція: Застосувати абстрактні класи та методи для приховування деталей реалізації.
#
# 4. Перевантаження операторів: Перевантажити оператори для порівняння оцінок студентів( ==, !=, <, >, <=, >= ),
# а також для агрегування оцінок курсів(оператор +).
#
# 5. Магічні методи: Реалізувати магічні методи для строкового представлення об’єктів, операцій порівняння,
# додавання оцінок та інших операцій.
#
# 6. Читання та запис у файли: Створити функції для збереження та завантаження даних про курси та студентів у текстові файли,
# а також у формати JSON та pickle.
#
# 7. Робота з бібліотеками `datetime` та `collections`: Відслідковувати дати початку та закінчення курсів,
# використовувати структури даних з модуля collections для зберігання оцінок.
#
# 8. Використання функцій `filter`, `sorted`, `map`: Обробляти списки студентів та курсів для фільтрації,
# сортування та перетворення даних.
#
# 9. До системи необхідно додати наступні можливості:
# - Перевірка активності курсу:
#     Реалізувати метод is_active(), який визначає, чи перебуває курс в активному стані
#     (тобто, поточна дата знаходиться між датою початку та закінчення курсу).
# - Генерація звіту по курсу:
#     Реалізувати метод generate_report(), який формує детальний звіт по курсу. Звіт повинен містити:
#         - Назву курсу та його тип.
#         - Статус активності курсу.
#         - Кількість студентів.
#         - Середній бал по курсу.
#         - Студента з найвищою оцінкою та студента з найнижчою оцінкою.
#         - Нагородження студентів:
#             Реалізувати метод award_badges(), який присвоює студентам бейджі залежно від їх оцінок.
#             Наприклад: - Оцінка ≥ 95: «Outstanding» - Оцінка ≥ 90: «Excellent» - Оцінка ≥ 80: «Good» - Інакше: «Needs Improvement»

from abc import ABC, abstractmethod
from datetime import datetime
import json
import pickle

class Student:
    def __init__(self, name: str, grade: float):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.grade == other.grade
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.grade < other.grade
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Student):
            return self.grade <= other.grade
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.grade > other.grade
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.grade >= other.grade
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Student):
            return self.grade != other.grade
        return NotImplemented

    def __str__(self):
        return f"Student(name={self.name}, grade={self.grade})"

    def __repr__(self):
        return self.__str__()

class Course(ABC):
    def __init__(self, name: str, start_date: str, end_date: str):
        format_date = "%d.%m.%Y"
        self.__name = name
        try:
            self.__start_date = datetime.strptime(start_date, format_date)
            self.__end_date = datetime.strptime(end_date, format_date)
        except ValueError:
            raise ValueError(f"Дати повинні бути у форматі {format_date}")
        self.__students = []

    def get_name(self):
        return self.__name

    def add_student(self, student: Student):
        """Додає студента до курсу"""
        if isinstance(student, Student):
            self.__students.append(student)
        else:
            raise TypeError("Очікується об'єкт типу Student")

    def get_students(self):
        """Повертає список студентів"""
        return self.__students

    def __str__(self):
        format_date = "%d.%m.%Y"
        students_str = ", ".join(str(s) for s in self.__students)
        start_date_str = self.__start_date.strftime(format_date)
        end_date_str = self.__end_date.strftime(format_date)
        return f"Course(name={self.__name}, start_date={start_date_str}, end_date={end_date_str}, students={students_str})"

    @abstractmethod
    def _course_type(self):
        """Абстрактний метод, що повертає тип курсу"""
        pass

    def __add__(self, other):
        """Перевантаження оператор '+' для об'єднання курсів"""
        if not isinstance(other, Course):
            return NotImplemented

        format_date = "%d.%m.%Y"
        new_name = f"Combined {self.__name} & {other.__name}"
        new_start_date = min(self.__start_date, other.__start_date).strftime(format_date)
        new_end_date = max(self.__end_date, other.__end_date).strftime(format_date)

        if type(self) == type(other):
            new_course = type(self)(new_name, new_start_date, new_end_date)
        else:
            new_course = CombinedCourse(new_name, new_start_date, new_end_date)

        for student in self.get_students() + other.get_students():
            new_course.add_student(student)

        return new_course

    def save_to_json(self, filename):
        """Зберегає дані курсу у JSON файл"""
        format_date = "%d.%m.%Y"
        data = {
            'name' : self.__name,
            'course_type': self._course_type(),
            'start_date' : self.__start_date.strftime(format_date),
            'end_date' : self.__end_date.strftime(format_date),
            'students' : [{'name': s.name, 'grade': s.grade} for s in self.__students]
        }
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def save_to_pickle(self, filename):
        """Зберегає дані курсу у pickle файл"""
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def load_from_pickle(clc, filename):
        """Завантажує дані курсу з pickle файлу"""
        with open(filename, 'rb') as file:
            course = pickle.load(file)
        return course

    @classmethod
    def load_from_json(cls, filename):
        """Завантажує дані курсу з JSON файлу"""
        with open(filename, 'r') as file:
            data = json.load(file)

        course_type_str = data.get('course_type')
        if course_type_str == "Mathematics":
            course_class = MathCourse
        elif course_type_str == "Science":
            course_class = ScienceCourse
        elif course_type_str == "Combined":
            course_class = CombinedCourse
        else:
            course_class = CombinedCourse

        new_course = course_class(data['name'], data['start_date'], data['end_date'])
        for s in data.get('students', []):
            new_course.add_student(Student(s['name'], s['grade']))

        return new_course

    def filter_student_by_grade(self, min_grade: float):
        return list(filter(lambda s: s.grade >= min_grade, self.__students))

    def sort_students(self):
        return sorted(self.__students, key=lambda s: s.grade)

    def get_student_names(self):
        return list(map(lambda s: s.name, self.__students))

    def is_active(self):
        now = datetime.now()
        return self.__start_date <= now <= self.__end_date

    def generate_report(self):
        students = self.__students
        if not students:
            return f"Курс {self.__name} не має записаних студентів"
        avg_grade = sum(s.grade for s in students)/len(students)
        top_student = max(students, key=lambda s: s.grade)
        low_student = min(students, key=lambda s: s.grade)
        report = f"Звіт курсу: {self.__name}\n"
        report += f"Тип курсу: {self._course_type()}\n"
        report += f"Активний: {'Так' if self.is_active else 'Ні'}\n"
        report += f"Кількість студентів: {len(students)}\n"
        report += f"Середній бал: {avg_grade}\n"
        report += f"Найкращий студент: {top_student.name} ({top_student.grade})\n"
        report += f"Студент з найнижчим балом: {low_student.name} ({low_student.grade})"

        return report

    def award_badges(self):
        badges = {}
        for s in self.get_students():
            if s.grade >= 95:
                badge = "Outstanding"
            elif s.grade >= 90:
                badge = "Excellent"
            elif s.grade >= 80:
                badge = "Good"
            else:
                badge = "Needs Improvement"
            badges[s.name] = badge
        return badges

class MathCourse(Course):
    def _course_type(self):
        return "Mathematics"

class ScienceCourse(Course):
    def _course_type(self):
        return "Science"

class CombinedCourse(Course):
    def _course_type(self):
        return "Combined"








bob = Student("Bob", 75)
alice = Student("Alice", 90)
charlie = Student("Charlie", 85)
dave = Student("Dave", 95)
emma = Student("Emma", 98)

# print(bob)
# print(alice)
# print(bob < alice)
# print(bob > alice)
# print(bob >= alice)
# print(bob <= alice)
# print(bob == alice)
# print(bob != alice)

math_course = MathCourse("Algebra", "15.02.2025", "15.03.2025")
scince_course = ScienceCourse("Biology", "20.02.2025", "20.03.2025")

math_course.add_student(bob)
math_course.add_student(alice)
math_course.add_student(emma)
scince_course.add_student(charlie)
scince_course.add_student(dave)

print("Студенти з оцінкою >=80 в курсі Algebra")
filtered_student = math_course.filter_student_by_grade(80)
for student in filtered_student:
    print(student)


print("\nСортування студентів за оцінкою в курсі Biology")
sorted_students = scince_course.sort_students()
sorted_students.reverse()
for student in sorted_students:
    print(student)

print("\nОтримання Імен студентів")
print(math_course.get_student_names())
print(scince_course.get_student_names())

combined_course = math_course + scince_course
print(f"\n{combined_course}")

badges = combined_course.award_badges()
for name, badge in badges.items():
    print(f"{name} - {badge}")

print(f'\n{combined_course.generate_report()}')


# test_course = Course("test", "05.05.2025", "05.06.2025")
# test_course.add_student(bob)
# test_course.add_student(alice)
# print(test_course)
# test_course.save_to_json("test_course.json")
# test_course.save_to_pickle("test_course.pcl")

# new_course = Course.load_from_pickle("test_course.pcl")
# print(new_course.get_students())
#