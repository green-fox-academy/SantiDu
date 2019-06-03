from collections import namedtuple

Student = namedtuple("Student", "name age gender grades")
John = Student(name="John", age=16, gender="male", grades=[5, 5, 4, 2])
Jane = Student(name="Jane", age=15, gender="female", grades=[4, 3, 4, 4, 5])
Bob = Student(name="Bob", age=17, gender="male", grades=[2, 2, 3, 1])

Students = (John, Jane, Bob)

