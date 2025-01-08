from utils import students, groups, dss, tps, attendances
from database import min_att, dic_att


def get_attendance_percentage(student):
    student_index = students.index(student)
    student_attendances = [attendance[student_index] for attendance in attendances.values()]
    attendance_percentage = sum(student_attendances) / len(student_attendances)
    return attendance_percentage


def get_min_attendance_by_attendance_percentage(percentage):
    for key, value in min_att.items():
        if int(percentage) in value:
            return key


def get_dict_act_by_min_act(min_act):
    return dic_att[min_act]


def get_ds_avg(student):
    student_index = students.index(student)
    student_dss = [ds[student_index] for ds in dss]
    return sum(student_dss) / len(student_dss)


def get_max_tp(student):
    return max([tp[students.index(student)] for tp in tps])


def calc_final_note(student):
    return (float((get_ds_avg(student) * 0.6 + get_max_tp(student) * 0.4) * get_dict_act_by_min_act(
        get_min_attendance_by_attendance_percentage(
            get_attendance_percentage(student))))
            .__round__(2))

