from collections import namedtuple

Student = namedtuple("Student", "name age gender grades")
John = Student(name="John", age=16, gender="male", grades=(5, 5, 4, 2))
Jane = Student(name="Jane", age=15, gender="female", grades=(4, 3, 4, 4, 5))
Bob = Student(name="Bob", age=17, gender="male", grades=(2, 2, 3, 1))

Students = (John, Jane, Bob)

####
males = filter(lambda student: student.gender == "male", Students)
print(f"Boys: {', '.join((male.name for male in males))}")

####
startswithJ = filter(lambda student: student.name.startswith("J"), Students)
print(f"Students whose name starts with J: {', '.join((J.name for J in startswithJ))}")

####
females = filter(lambda student: student.gender == "female", Students)
print(f"Girls: {', '.join((female.name for female in females))}")

####
average_above_4 = filter(lambda student: sum(student.grades) / len(student.grades) >= 4, Students)
print(f"Students whose average grade is above 4: {', '.join((s.name for s in average_above_4))}")

####
boys_startswithJ = filter(lambda student: student.name.startswith("J") and student.gender == "male", Students)
print(f"Boys whose name starts with J: {', '.join((theJ.name for theJ in boys_startswithJ))}")

####
girls_average_above_4 = filter(lambda student: sum(student.grades) / len(student.grades) >= 4 and
    student.gender == "female", Students)
print(f"Girls whose average grade is above 4: {', '.join((s.name for s in girls_average_above_4))}")

####
at_least_2_fives = filter(lambda student: sum(map(lambda grade: grade == 5, student.grades)) == 2, Students)
print(f"Those who have at least two fives: {', '.join((s.name for s in at_least_2_fives))}")

####
def avg_above_4and2_fives(grades):
    s = 0
    count = 0
    count5 = 0
    for grade in grades:
        count += 1
        s += grade
        if count5 >= 2:
            continue
        elif grade >= 5:
            count5 += 1
    if s / count >= 4 and count5 >= 2:
        return True

result = (student.name for student in Students if avg_above_4and2_fives(student.grades))
print(f"{next(result)} is the student who have at least two fives and have average grade above 4.")