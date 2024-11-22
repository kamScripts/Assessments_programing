""" This is what this program does """


def grades(mark):
    """Grades"""
    grade = ''
    if mark >= 70:
        grade = 'Distinction'
    elif mark >= 60:
        grade = 'Merit'
    elif mark >= 50:
        grade = 'Pass'
    else:
        grade = 'Fail'
    return grade


# calculate weighted mark fo a subject
def count_mark(g, w, wm):
    """Calculate weighted mark"""
    weighted_mark = float(wm)
    weighted_mark += ((int(g) * (float(w) / 100)))
    return weighted_mark
def reader_multiple_student(file_path):
    """read students grades from text file"""
    students = []
    check_name = ''
    with open(file_path, 'r', encoding='UTF-8') as file:
        for line in file:
            name, subject, grade, weight = line.rstrip('\n').split(',')
            if name != check_name:
                # if student not on the list, add dict and calculate weighted mark.
                students.append({
                    'student_name':name, 
                    f'{subject}' : (grade,weight), 
                    'weighted_mark': int(grade) * (float(weight) / 100) 
                })
                check_name = name
            else:
                for student in students:
                    #student on the list, so update dict with new subjects
                    # and calculate weighted mark based on previous score
                    if student.get('student_name') == name:
                        student.update(
                                       {f'{subject}': (grade, weight),
                                        'weighted_mark': count_mark(grade, weight, student.get('weighted_mark'))})
    return students

def write_many_files(input_path):
    """Write student final grade into file named with student's full name"""
    students = reader_multiple_student(input_path)
    for student in students:
        name = student.get('student_name')
        student_path = name.replace(' ', '_')
        first_name, _ = name.split(' ')
        with open(f'{student_path}.txt', 'w', encoding='UTF-8') as file:
            file.write(f'{first_name}, {student.get("weighted_mark")}, {grades(student.get("weighted_mark"))}')
write_many_files('data.txt')
    