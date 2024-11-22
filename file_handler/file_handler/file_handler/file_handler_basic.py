def grades(mark):
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


def reader(file_path):
    # initialize final result's variable
    weighted_mark = 0    
    with open(file_path) as file:
        for line in file:
            # destruct text line into single variables, split line on every comma.                        
            name, subject, grade, weight  = line.split(',')
            # split name variable on space to separate first from second nam. '_' character indicates that this variable will not be used.
            name, _ = name.split(' ')
            # calculate weighted mark from formula ( grade times weight in percentages (that's why is divided by 100.) ) and values trasformed from string to numbers.
            weighted_mark += ((int(grade) * (float(weight) / 100)))
        # function return f-string (formatted string literal) built from singles variables and grades function which returns grade calculated from marks.              
    return f'{name}, {weighted_mark}, {grades(weighted_mark)}'
      
def writer(file_path, value):
    with open(file_path, 'w') as file:
        file.write(value)

def read_and_write(r_file, w_file):
    writer(w_file, (reader(r_file)))

read_and_write('./data.txt', './student.txt')

