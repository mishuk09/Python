# 1. Write a Program to create an empty valid class by name Students, with no properties.


class Students:


# 2. Write a Program to create a class by name Students, and initialize attributes like name, age, and grade while creating an object.'''


class Students:

    student_id = 'V10'
    student_name = 'MAHADI HASAN MISHUK'
    student_GPA = 5.00

    def display():
        print(
            f'Student id: {Students().student_id}\nStudent Name: {Students().student_name} \n Student GPA:{Students().student_GPA}')


print("Output")
Students.display()


