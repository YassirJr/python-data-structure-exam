from q1 import extract_students_list
from q2 import calc_final_note

if __name__ == '__main__':
    students_list = extract_students_list()
    for group, students in students_list.items():
        print(f'Group {group}:')
        for student in students:
            print(f'{student}: {calc_final_note(student)}')
        print()
