#!/usr/bin/env python

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    _min = sorted(students, key=lambda x: x[1])[0][1]
    for _student in sorted(students, key=lambda x: x[1]):
        if _student[1] > _min:
            _sec_min = _student[1]
            break

    print(*[i[0] for i in sorted(list(filter(lambda x: x[1] == _sec_min, students)), key=lambda x: x[0])], sep='\n')
