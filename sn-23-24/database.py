from random import randint, sample

# Constants
std_nbr = 10  # number of students
DS_nbr = 3  # number of supervised assignments
TP_nbr = 2  # number of practical works
Att_nbr = 3  # number of sessions

# Days of the week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# Attendance ranges
min_att = {
    'Present': range(0, 5),
    'Late': range(5, 11),
    'Very Late': range(11, 21),
    'Absent': range(21, 120)
}

# Attendance coefficients
dic_att = {
    'Present': 1.0,
    'Late': 0.95,
    'Very Late': 0.9,
    'Absent': 0.87
}

# Main database structure
database = {
    'Students': [f'Student_{i}' for i in range(1, std_nbr + 1)],
    'Genders': [sample(['M', 'F'], 1)[0] for step in range(std_nbr)],
    'Groups': [sample(['A', 'B', 'C', 'D'], 1)[0] for x in range(std_nbr)],
    'DS': [[randint(6, 20) for i in range(std_nbr)] for step in range(DS_nbr)],
    'TP': [[sample([randint(6, 12), randint(10, 16), randint(14, 20)], 1)[0]
            for i in range(std_nbr)] for step in range(TP_nbr)],
    'Attendance': {
        sample(days, 1)[0]: [sample([randint(0, 25), randint(0, 25), 0, 5], 1)[0]
                             for i in range(std_nbr)] for i in range(Att_nbr)
    }
}
