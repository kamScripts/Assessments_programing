mark = int(input('What is student\'s mark ?'))
grade = ''
if mark >=70 and mark <= 100:
    grade = 'A'
elif mark >= 60 and mark <= 69:
    grade = 'B'
elif mark >= 50 and mark <= 59:
    grade = 'C'
elif mark >= 40 and mark <= 49:
    grade = 'D'
elif mark >= 30 and mark <= 39:
    grade = 'E'
elif mark >= 20 and mark <= 29:
    grade = 'F'

print(f'Student received grade {grade}.')
