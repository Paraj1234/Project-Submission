"""
Project:

* School Database

- Student (student_id, name, age, sex, class, section, python_marks, database_marks, math_marks, statistics_marks)
- Teacher (teacher_id, name, age, sex, class_teacher, teacher_salary)
- Principal (principal_id, name, age, sex, teacher_id)
- Admin (admin_id, name, email, password)

Input for admin_name, admin_email, admin_password, if the inputs match the data stored in the table,
give the admin the option to alter any table (create, read, update, delete)
"""

import mysql.connector

db = mysql.connector.connect(
    host='enter host',  # Replace these values for your MySQL server values
    user='enter user',
    passwd='enter password'
)

cursor = db.cursor()
cursor.execute('CREATE DATABASE school')  # Make this a comment after executing the program once

db = mysql.connector.connect(
    host='enter host',  # Replace these values for your MySQL server values
    user='enter user',
    passwd='enter password',
    database='school'
)

my_cursor = db.cursor(buffered=True)

student = 'CREATE TABLE student (student_id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), ' \
          'age smallint UNSIGNED, sex VARCHAR(20), class smallint, section VARCHAR(1), python_marks smallint, ' \
          'database_marks smallint, math_marks smallint, statistics_marks smallint)'

teacher = 'CREATE TABLE teacher (teacher_id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50),' \
          'age smallint UNSIGNED, sex VARCHAR(20), class_teacher smallint, teacher_salary int)'

principal = 'CREATE TABLE principal (principal_id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50),' \
            'age smallint UNSIGNED, sex VARCHAR(20), teacher_id int)'

admin = 'CREATE TABLE admin (admin_id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50),' \
        'email VARCHAR(50), password VARCHAR(50))'

my_cursor.execute(student)  # make this a comment after executing the program once
my_cursor.execute(teacher)  # make this a comment after executing the program once
my_cursor.execute(principal)  # make this a comment after executing the program once
my_cursor.execute(admin)  # make this a comment after executing the program once

count, login__ = 0, 0

my_cursor.execute('SELECT * FROM admin')
for i in my_cursor:
    count += 1


def new_admin():
    if input('If you want to create a new admin press 1: ') == '1':
        name = input('Type in an username: ')
        email = input('Type in an email id: ')
        password = input('Type in a password: ')

        my_cursor.execute('INSERT INTO admin (name, email, password) VALUES (%s, %s, %s)', (name, email, password))
        db.commit()

        global count
        count += 1


new_admin()


def login(num):
    global login__

    if num == 1:
        login_ = (input('If you want to login and alter something press 1: '))
    else:
        login_ = '1'

    if login_ == '1':
        if num == 0:
            print('you entered something incorrectly, please try again \n')

        name = input('name: ')
        email = input('email: ')
        password = input('password: ')

        my_cursor.execute('SELECT * FROM admin')

        for j in my_cursor:
            if name == j[1]:
                if email == j[2]:
                    if password == j[3]:
                        print('successful login!')
                        login__ = 1
                        return 1

        login(0)


def alter_student():
    alter_thing = input('If you want to create, press 1\n'
                        'If you want to read, press 2\n'
                        'If you want to update, press 3\n'
                        'If you want to delete press 4\n\n')

    if alter_thing == '1':
        sex, age, class_, section, python_marks, database_marks, statistics_marks, math_marks = \
            0, '', '-1', 1, '-1', '-1', '-1', '-1'

        name = input('Enter the name: ')
        while not age.isdigit():
            age = input('Enter the age: ')
        while sex not in ['boy', 'girl']:
            sex = input('Enter the gender (boy/ girl)')
        while not class_.isdigit() or int(class_) < 1 or int(class_) > 12:
            class_ = input('Enter the class: ')
        while section not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                              'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
            section = input('Enter the section as a single alphabet in capitals: ')
        while not python_marks.isdigit() or int(python_marks) > 100 or int(python_marks) < 0:
            python_marks = input('Enter the Python Marks between 0 to 100: ')
        while not database_marks.isdigit() or int(database_marks) > 100 or int(database_marks) < 0:
            database_marks = input('Enter the Database Marks between 0 to 100: ')
        while not math_marks.isdigit() or int(math_marks) > 100 or int(math_marks) < 0:
            math_marks = input('Enter the Math Marks between 0 to 100: ')
        while not statistics_marks.isdigit() or int(statistics_marks) > 100 or int(statistics_marks) < 0:
            statistics_marks = input('Enter the Statistics Marks between 0 to 100: ')

        my_cursor.execute('INSERT INTO student (name, age, sex, class, section, python_marks, database_marks, '
                          'math_marks, statistics_marks) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                          (name, age, sex, class_, section, python_marks, database_marks, math_marks, statistics_marks))
        db.commit()

    elif alter_thing == '2':
        my_cursor.execute('SELECT * FROM student')
        for j in my_cursor:
            print(j)

    elif alter_thing == '3':
        count_student = []
        my_cursor.execute('SELECT * FROM student;')
        for j in my_cursor:
            count_student.append(str(j[0]))

        student_id = '-1'
        while not student_id.isdigit() or int(student_id) not in count_student:
            student_id = input("Enter the id of the student you want to alter, "
                               "you will be prompted again if the id isn't present in the database: ")

        update = 'yes'
        while update == 'yes':
            column = ''
            while column not in ['name', 'age', 'sex', 'class', 'section', 'python marks', 'database marks',
                                 'math marks', 'statistics marks']:
                column = input("Enter the name of the column you want to alter\n"
                               "options: 'name', 'age', 'sex', 'class', 'section', 'python marks', "
                               "'database marks', 'math marks', 'statistics marks'\n\n")

            if column == 'name':
                name = input('Enter the name: ')
                my_cursor.execute(f"UPDATE student SET name='{name}' WHERE student_id={student_id}")
                db.commit()

            if column == 'age':
                age = ''
                while not age.isdigit():
                    age = input('Enter the age: ')
                my_cursor.execute(f"UPDATE student SET age='{age}' WHERE student_id={student_id}")
                db.commit()

            if column == 'sex':
                sex = ''
                while sex not in ['boy', 'girl']:
                    sex = input('Enter the gender (boy/ girl)')
                my_cursor.execute(f"UPDATE student SET sex='{sex}' WHERE student_id={student_id}")
                db.commit()

            if column == 'class':
                class_ = '-1'
                while not class_.isdigit() or int(class_) < 1 or int(class_) > 12:
                    class_ = input('Enter the class: ')
                my_cursor.execute(f"UPDATE student SET class='{class_}' WHERE student_id={student_id}")
                db.commit()

            if column == 'section':
                section = 1
                while section not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                                      'Q', 'R',
                                      'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
                    section = input('Enter the section as a single alphabet in capitals: ')
                my_cursor.execute(f"UPDATE student SET section='{section}' WHERE student_id={student_id}")
                db.commit()

            if column == 'python marks':
                python_marks = ''
                while not python_marks.isdigit() or int(python_marks) > 100 or int(python_marks) < 0:
                    python_marks = input('Enter the Python Marks between 0 to 100: ')
                my_cursor.execute(f"UPDATE student SET python_marks='{python_marks}' WHERE student_id={student_id}")
                db.commit()

            if column == 'database marks':
                database_marks = ''
                while not database_marks.isdigit() or int(database_marks) > 100 or int(database_marks) < 0:
                    database_marks = input('Enter the Database Marks between 0 to 100: ')
                my_cursor.execute(f"UPDATE student SET database_marks='{database_marks}' WHERE student_id={student_id}")
                db.commit()

            if column == 'math marks':
                math_marks = ''
                while not math_marks.isdigit() or int(math_marks) > 100 or int(math_marks) < 0:
                    math_marks = input('Enter the Math Marks between 0 to 100: ')
                my_cursor.execute(f"UPDATE student SET math_marks='{math_marks}' WHERE student_id={student_id}")
                db.commit()

            if column == 'statistics marks':
                statistics_marks = ''
                while not statistics_marks.isdigit() or int(statistics_marks) > 100 or int(statistics_marks) < 0:
                    statistics_marks = input('Enter the Statistics Marks between 0 to 100: ')
                my_cursor.execute(f"UPDATE student SET statistics_marks='{statistics_marks}' "
                                  f"WHERE student_id={student_id}")
                db.commit()

            update = input('If you wish to alter something else for the same id enter yes: ')

    elif alter_thing == '4':
        count_student = []
        my_cursor.execute('SELECT * FROM student;')
        for j in my_cursor:
            count_student.append(str(j[0]))

        print('Enter the student id of the row you want to delete')

        student_id = '-1'
        while not student_id.isdigit() or student_id not in count_student:
            student_id = input("Enter the id of the student you want to alter, "
                               "you will be prompted again if the id isn't present in the database: ")

        my_cursor.execute(f'DELETE FROM student WHERE student_id = {student_id}')
        db.commit()


def alter_teacher():
    alter_thing = input('If you want to create, press 1\n'
                        'If you want to read, press 2\n'
                        'If you want to update, press 3\n'
                        'If you want to delete press 4\n\n')

    if alter_thing == '1':
        sex, age, class_teacher, section, python_marks, database_marks, statistics_marks, math_marks, teacher_salary = \
         0, '', '-1', 1, '-1', '-1', '-1', '-1', '-1'

        name = input('Enter the name: ')
        while not age.isdigit():
            age = input('Enter the age: ')
        while sex not in ['boy', 'girl']:
            sex = input('Enter the gender (boy/ girl)')
        while not class_teacher.isdigit() or int(class_teacher) < 1 or int(class_teacher) > 12:
            class_teacher = input('Enter the class teacher: ')
        while not teacher_salary.isdigit() or int(teacher_salary) < 1:
            teacher_salary = input('Enter the salary: ')

        my_cursor.execute('INSERT INTO teacher (name, age, sex, class_teacher, salary) VALUES (%s, %s, %s, %s, %s)',
                          (name, age, sex, class_teacher, teacher_salary))
        db.commit()

    elif alter_thing == '2':
        my_cursor.execute('SELECT * FROM teacher')
        for j in my_cursor:
            print(j)

    elif alter_thing == '3':
        count_teacher = []
        my_cursor.execute('SELECT * FROM teacher')
        for j in my_cursor:
            count_teacher.append(str(j[0]))

        teacher_id = '-1'
        while not teacher_id.isdigit() or int(teacher_id) not in count_teacher:
            teacher_id = input("Enter the id of the teacher you want to alter, "
                               "you will be prompted again if the id isn't present in the database: ")

        update = 'yes'
        while update == 'yes':
            column = ''
            while column not in ['name', 'age', 'sex', 'class teacher', 'salary']:
                column = input("Enter the name of the column you want to alter\n"
                               "options: 'name', 'age', 'sex', 'class teacher', 'salary'\n\n")

            if column == 'name':
                name = input('Enter the name: ')
                my_cursor.execute(f"UPDATE teacher SET name='{name}' WHERE teacher_id={teacher_id}")
                db.commit()

            if column == 'age':
                age = ''
                while not age.isdigit():
                    age = input('Enter the age: ')
                my_cursor.execute(f"UPDATE teacher SET age='{age}' WHERE teacher_id={teacher_id}")
                db.commit()

            if column == 'sex':
                sex = ''
                while sex not in ['boy', 'girl']:
                    sex = input('Enter the gender (boy/ girl)')
                my_cursor.execute(f"UPDATE teacher SET sex='{sex}' WHERE teacher_id={teacher_id}")
                db.commit()

            if column == 'class teacher':
                class_teacher = '-1'
                while not class_teacher.isdigit() or int(class_teacher) < 1 or int(class_teacher) > 12:
                    class_teacher = input('Enter the class teacher: ')
                my_cursor.execute(f"UPDATE teacher SET class='{class_teacher}' WHERE teacher_id={teacher_id}")
                db.commit()

            if column == 'salary':
                teacher_salary = '-1'
                while not teacher_salary.isdigit() or int(teacher_salary) < 1:
                    teacher_salary = input('Enter the salary: ')
                my_cursor.execute(f"UPDATE teacher SET salary='{teacher_salary}' WHERE teacher_id={teacher_id}")
                db.commit()

            update = input('If you wish to update something else, enter yes: ')

    elif alter_thing == '4':
        count_teacher = []
        my_cursor.execute('SELECT * FROM teacher;')
        for j in my_cursor:
            count_teacher.append(str(j[0]))

        print('Enter the teacher id of the row you want to delete')

        teacher_id = '-1'
        while not teacher_id.isdigit() or teacher_id not in count_teacher:
            teacher_id = input("Enter the id of the teacher you want to alter, "
                               "you will be prompted again if the id isn't present in the database: ")

        my_cursor.execute(f'DELETE FROM teacher WHERE teacher_id = {teacher_id}')
        db.commit()


def alter_principal():
    alter_thing = input('If you want to create, press 1\n'
                        'If you want to read, press 2\n'
                        'If you want to update, press 3\n'
                        'If you want to delete press 4\n\n')

    if alter_thing == '1':
        sex, age, class_teacher, section, python_marks, database_marks, statistics_marks, math_marks, teacher_salary = \
            0, '', '-1', 1, '-1', '-1', '-1', '-1', '-1'

        name = input('Enter the name: ')
        while not age.isdigit():
            age = input('Enter the age: ')
        while sex not in ['boy', 'girl']:
            sex = input('Enter the gender (boy/ girl)')
        list_of_id = []

        my_cursor.execute('SELECT * FROM teacher')
        for j in my_cursor:
            list_of_id.append(str(j[0]))

        teacher_id = []
        while teacher_id not in list_of_id:
            teacher_id = input('Please enter an existing teacher id, else terminate the program and create one: ')

        my_cursor.execute('INSERT INTO principal (name, age, sex, teacher_id) VALUES (%s, %s, %s, %s)',
                          (name, age, sex, teacher_id))
        db.commit()

    elif alter_thing == '2':
        my_cursor.execute('SELECT * FROM principal')
        for j in my_cursor:
            print(j)

    elif alter_thing == '3':
        count_principal = []
        my_cursor.execute('SELECT * FROM principal')
        for j in my_cursor:
            count_principal.append(str(j[0]))

        principal_id = '-1'
        while not principal_id.isdigit() or int(principal_id) not in count_principal:
            principal_id = input("Enter the id of the principal you want to alter, "
                                 "you will be prompted again if the id isn't present in the database: ")

        update = 'yes'
        while update == 'yes':
            column = ''
            while column not in ['name', 'age', 'sex', 'teacher id']:
                column = input("Enter the name of the column you want to alter\n"
                               "options: 'name', 'age', 'sex', 'teacher id'\n\n")

            if column == 'name':
                name = input('Enter the name: ')
                my_cursor.execute(f"UPDATE principal SET name='{name}' WHERE principal_id={principal_id}")
                db.commit()

            if column == 'age':
                age = ''
                while not age.isdigit():
                    age = input('Enter the age: ')
                my_cursor.execute(f"UPDATE principal SET age='{age}' WHERE principal_id={principal_id}")
                db.commit()

            if column == 'sex':
                sex = ''
                while sex not in ['boy', 'girl']:
                    sex = input('Enter the gender (boy/ girl)')
                my_cursor.execute(f"UPDATE principal SET sex='{sex}' WHERE principal_id={principal_id}")
                db.commit()

            if column == 'teacher id':
                my_cursor.execute('SELECT * FROM teacher')
                list_of_id = []
                for j in my_cursor:
                    list_of_id.append(str(j[0]))
                teacher_id = '-1'
                while teacher_id not in list_of_id:
                    teacher_id = input('Enter the teacher id: ')
                my_cursor.execute(f"UPDATE principal SET teacher_id='{teacher_id}' WHERE principal_id={principal_id}")

            update = input('If you want to update something else enter yes: ')

    elif alter_thing == '4':
        count_teacher = []
        my_cursor.execute('SELECT * FROM principal;')
        for j in my_cursor:
            count_teacher.append(str(j[0]))

        print('Enter the principal id of the row you want to delete')

        teacher_id = '-1'
        while not teacher_id.isdigit() or teacher_id not in count_teacher:
            teacher_id = input("Enter the id of the principal you want to alter, "
                               "you will be prompted again if the id isn't present in the database: ")

        my_cursor.execute(f'DELETE FROM principal WHERE principal_id = {teacher_id}')
        db.commit()


login(1)


if count != 0:
    if login__ == 1:
        alter = input('If you want to alter student, press 1\n'
                      'If you want to alter teacher press 2\n'
                      'If you want to alter principal press 3\n\n')

        if alter == '1':
            alter_student()

        elif alter == '2':
            alter_teacher()

        elif alter == '3':
            alter_principal()

        print('You must login again to alter something else')
