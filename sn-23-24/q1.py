from utils import students, groups

print(students)
print(groups)

def extract_students_list():
    return {
        group : [student for student, student_group in zip(students, groups) if student_group == group] for group in set(groups)
    }


