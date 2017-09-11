import random
"""
This module should use random module to generate_id
"""


def import_data_from_file(filename='class_data.txt'):
    """
    Import data from file to list. Expected returned data format:
        [['M9@p', 'Ela', 'Opak', '1988', 'A', '60', '69'],
        ['E4)i', 'Barbara', 'Loremska', '1991', 'B', '76', '61'],
        ...]

    :param str filename: optional, name of file to be imported

    :returns: list of lists representing students' data
    :rtype: list
    """
    with open(filename, "r", encoding="utf-8") as myfile:
        students = []
        for line in myfile:
            students.append(line.strip().split(','))
        return students


def export_to_file(data, filename='class_data.txt', mode='a'):
    """
    Export data from list to file. If called with mode 'w' it should overwritte
    data in file. If called with mode 'a' it should append data at the end.

    :param list data: students' data
    :param str filename: optional, name of file to export data to
    :param str mode: optional, file open mode with the same meaning as\
    file open modes used in Python. Possible values: only 'w' or 'a'

    :raises ValueError: if mode other than 'w' or 'a' was given. Error message:
        'Wrong write mode'
    """
    if mode == 'w':
        with open(filename, "w", encoding="utf-8") as myfile:
            myfile.write(str(data) + "\n")
    if mode == 'a':
        with open(filename, "a", encoding="utf-8") as myfile:
            myfile.write(str(data) + "\n")
    else:
        raise ValueError('Wrong write mode')


def get_student_by_id(uid, students):
    """
    Get student by unique id

    :param str uid: student unique id
    :param list students: students' data

    :raises ValueError: if student's uid not found in class data.
        Error message: 'Student does not exist'

    :returns: specific student's data
    :rtype: list
    """
    for line in students:
        if line[0] == uid:
            return line
        else:
            raise ValueError('Student does not exist')


def get_students_of_class(students, class_name):
    """
    Get all students from given class

    :param list students: list of nested list imported from file
    :param str class_name: string representing class name that student\
        attends to

    :returns: students from given class only
    :rtype: list
    """
    all_class = []
    for line in students:
        if line[4] == class_name:
            all_class.append(line)
    return all_class


def get_youngest_student(students):
    """
    Get youngest student from all classes

    IMPORTANT:
        Implement this function without built-in functions like max(), min()
        or similar

    :param list students:  students' data

    :returns: youngest student
    :rtype: list
    """
    min = students[0]
    for line in students[1:]:
        if line[3] > min[3]:
            min = line
    return min


def get_youngest_student_of_class(students, class_name):
    """
    Get youngest student from given class

    IMPORTANT:
        Implement this function without built-in functions like max(), min()
        or similar

    :param list students:  students' data
    :param str class_name: string representing class name that student\
        attends to

    :returns: youngest student from given class
    :rtype: list
    """
    class_a = []
    class_b = []
    for line in students:
        if line[4] == "A":
            class_a.append(line)
        if line[4] == "B":
            class_b.append(line)
    if class_name == "A":
        min = class_a[0]
        for line in class_a[1:]:
            if line[3] > min[3]:
                min = line
        return min
    if class_name == "B":
        min = class_b[0]
        for line in class_b[1:]:
            if line[3] > min[3]:
                min = line
        return min
    else:
        raise ValueError("No such class.")


def get_oldest_student(students):
    """
    Get oldest student from all classes

    IMPORTANT:
        Implement this function without built-in functions like max(), min()
        or similar

    :param list students:  students' data

    :returns: oldest student
    :rtype: list
    """
    max = students[0]
    for line in students[1:]:
        if line[3] < max[3]:
            max = line
    return max


def get_oldest_student_of_class(students, class_name):
    """
    Get oldest student from given class

    IMPORTANT:
        Implement this function without built-in functions like max(), min()
        or similar

    :param list students:  students' data
    :param str class_name: string representing class name that student\
        attends to

    :returns: oldest student
    :rtype: list
    """
    class_a = []
    class_b = []
    for line in students:
        if line[4] == "A":
            class_a.append(line)
        if line[4] == "B":
            class_b.append(line)
    if class_name == "A":
        max = class_a[0]
        for line in class_a[1:]:
            if line[3] < max[3]:
                max = line
        return max
    if class_name == "B":
        max = class_b[0]
        for line in class_b[1:]:
            if line[3] < max[3]:
                max = line
        return max
    else:
        raise ValueError("No such class.")


def get_average_grade_of_students(students):
    """
    Calculate average grade of all students

    IMPORTANT:
        Implement this function without built-in functions like sum()
        or similar

    :param list students:  students' data

    :returns: average grade of students value
    :rtype: float
    """
    total_grades = 0
    for item in students:
        total_grades += int(item[5])
    return total_grades / len(students)


def get_average_presence_of_students(students):
    """
    Returns rounded average presence of all students. For instance,
    if average presence is 35.4912, returned value should be 35,
    if average presence is 41.5, returned value should be 42,

    IMPORTANT:
        Implement this function without built-in functions like sum(), round()
        or similar

    :param list students:  students' data

    :returns: average presence of students rounded to int
    :rtype: int
    """
    attendance = 0
    for item in students:
        attendance += int(item[6])
        result = attendance / len(students)
    if result % int(result) < 0.5:
        return int(result)
    else:
        return int(result) + 1


def generate_id(current_ids):
    """
    ADDITIONAL REQUIREMENT - BONUS

    Generate unique id. It should be unique in all existing students list. If
    generated id was already used, function should regenerate it untill it is
    totaly new. Newly generated unique id should be added to current_ids

    REQUIREMENTS:
        - All ids must be 4-characters long
        - Characters should appear in given order:
            1. Upper letter
            2. Digit from 0 to 9
            3. Special character from this list: !@#$%^&*()_+
            4. Lower letter

            Example ids:
                W1&p
                M9@p
                P1!n

    :param list current_ids: list of all ids. It's used to check if
            generated id is unique or not. If new id is unique, current_ids
            should be extended to include this new id.

    :returns: unique id
    :rtype: str
    """


def get_all_by_gender(students, gender):
    """
    ADDITIONAL REQUIREMENT - BONUS

    Get all students with given gender. As someone forgot to ask students about
    it, the only way JERZYBOT can find out if someone is female is her name.
    Treat all students with name ending with 'a' as female (Maria, Anna, etc).
    (we're sorry Miriam, we'll update JERZYBOT as soon as possible)

    :param list students:  students' data
    :param str gender: gender to filter by. 'female' will return female
        students, 'male' will return list of male students

    :raises ValueError: if gender other than 'female' or 'male' was given.
        Error message: 'Wrong gender'

    :returns: list of students filtered by given gender
    :rtype: list
    """


def sort_students_by_age(students, order=None):
    """
    ADDITIONAL REQUIREMENT - BONUS

    Sorts student list by age. User can choose sorting order by passing
    'desc' for descending order or 'asc' for ascening order.
    If order is None returns empty list

    IMPORTANT:
        Implement this function without using sorted() or similar built-in
        functions

    :param list students:  students' data
    :param str order: optional, sorting order

    :raises ValueError: if order other than 'asc', 'desc' or None
        was given

    :returns: sorted students or empty list
    :rtype: list
    """
