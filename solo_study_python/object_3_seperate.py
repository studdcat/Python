def create_student(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
    }

def student_get_sum(student):
    return student["korean"] + student["math"] + student["english"] + student["science"]

def student_get_average(student):
    return student_get_sum(student) / 4

def student_to_string(student):
    return "{}\t{}\t{}".format(student["name"], student_get_sum(student), student_get_average(student))

students = [
    create_student("윤인성", 87, 98, 88, 95),
    create_student("연하진", 87, 98, 88, 95),
    create_student("구지연", 87, 98, 88, 95)
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    for student in students:
        print(student_to_string(student))