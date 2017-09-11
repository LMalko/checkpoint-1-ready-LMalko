import data
import display
"""
The main program should use functions from data and display modules
"""


def add_new_student(students, new_student):
    """
    ADDITIONAL REQUIREMENT - BONUS

    Creates id for new student, adds it at the beginning of new student data,
    adds new student to students list and appends it to data file.

    :param list students: currently existing students
    :param list new_student: new student data without id. Format:
        name,surname,year of birth,class,average grade,average presence

    :returns: updated students list
    :rtype: list
    """


def delete_student_by_id(students, uid):
    """
    Deletes student from list by given unique id and updates data file

    :param list students: currently existing students
    :param str uid: unique id of student to be deleted

    :returns: updated students list
    :rtype: list
    """


def main():
    """
    Calls all interaction between user and program, handles program menu
    and user inputs. It should have main loop of program that will end only
    when user choose an option from menu to close the program. It should repeat
    displaying menu and asking for input until that moment.

    You should create new functions and call them from main whenever it can
    make the code cleaner
    """
    print("Hello to JERZYBOT. Please select Your option.")
    print("1 --> Create new student.")
    print("2 --> Delete student.")
    print("3 --> Select student.")
    print("4 --> Print all students.")
    print("0 --> Create new student.")
    while True:
        users_choice = int(input("Choose:"))
        if users_choice not in [1, 2, 3, 4, 0]:
            continue
        else:
            break
    


if __name__ == '__main__':
    main()
