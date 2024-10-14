# student_records.py

from typing import List, Tuple

class Student:
    """Represents a student with a name and a grade."""
    def __init__(self, name: str, grade: float):
        self.name = name
        self.grade = grade

    def __repr__(self):
        return f"{self.name}: {self.grade}"


def bubble_sort(students: List[Student], key=lambda x: x.name) -> List[Student]:
    """Sorts students using Bubble Sort."""
    n = len(students)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if key(students[j]) > key(students[j + 1]):
                students[j], students[j + 1] = students[j + 1], students[j]
    return students


def merge_sort(students: List[Student], key=lambda x: x.grade) -> List[Student]:
    """Sorts students using Merge Sort."""
    if len(students) <= 1:
        return students

    mid = len(students) // 2
    left = merge_sort(students[:mid], key)
    right = merge_sort(students[mid:], key)

    return merge(left, right, key)


def merge(left: List[Student], right: List[Student], key) -> List[Student]:
    """Merges two sorted lists."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def binary_search(students: List[Student], target_name: str) -> int:
    """Searches for a student by name using Binary Search."""
    low, high = 0, len(students) - 1

    while low <= high:
        mid = (low + high) // 2
        if students[mid].name == target_name:
            return mid
        elif students[mid].name < target_name:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def class_average(students: List[Student]) -> float:
    """Calculates the average grade of the class."""
    if not students:
        return 0.0
    return sum(student.grade for student in students) / len(students)


def top_student(students: List[Student]) -> Student:
    """Identifies the student with the highest grade."""
    return max(students, key=lambda student: student.grade)


def factorial(n: int) -> int:
    """Calculates factorial of n using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int, memo={0: 0, 1: 1}) -> int:
    """Calculates Fibonacci using dynamic programming."""
    if n in memo:
        return memo[n]
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


def main():
    # Sample list of students
    students = [
        Student("Alice", 85.5),
        Student("Bob", 92.0),
        Student("Charlie", 78.0),
        Student("David", 88.5),
        Student("Eve", 91.0),
    ]

    print("Original Student List:")
    print(students)

    print("\nSorted by Name (Bubble Sort):")
    sorted_by_name = bubble_sort(students[:], key=lambda x: x.name)
    print(sorted_by_name)

    print("\nSorted by Grade (Merge Sort):")
    sorted_by_grade = merge_sort(students[:], key=lambda x: x.grade)
    print(sorted_by_grade)

    print("\nSearching for 'Charlie' using Binary Search:")
    index = binary_search(sorted_by_name, "Charlie")
    if index != -1:
        print(f"Found: {sorted_by_name[index]}")
    else:
        print("Student not found.")

    print(f"\nClass Average Grade: {class_average(students):.2f}")

    print(f"\nTop Student: {top_student(students)}")

    print("\nFactorial of 5:")
    print(factorial(5))

    print("\nFibonacci of 10:")
    print(fibonacci(10))


if __name__ == "__main__":
    main()
