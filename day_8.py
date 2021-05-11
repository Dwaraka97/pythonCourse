all_courses = ['Python', 'Java', 'Machine Learning', 'Big data', 'C programming', 'Oracle SQL', 'Power Bi', 'Go lang',
               'C++ Graphics', 'React JS', 'Ruby Rails', 'Flask', 'HTML & CSS', 'Salesforce', 'Javascript', 'Django']

name = input("Enter your name: ")
email = input("Enter your Email-id: ")

user_profile = {
    'name': name,
    'email': email,
    'courses': []
}


def register_course():
    for index, course in enumerate(all_courses, start=1):
        print(f"{index} : {course}")

    choose_course = int(input("Enter the number of course u want to register: "))
    choose_course -= 1
    selected_course = all_courses.pop(choose_course)
    user_profile['courses'].append(selected_course)


def show_registered_courses():
    print("Registered Courses are:", end=" ")
    for course in user_profile['courses']:
        print(course, end=', ')


def show_profile():
    print(f"{user_profile['name'].title()} with mail id {user_profile['email']} has registered for {user_profile['courses']}")


show_menu = """\nPlease enter one of the following options:

- 1 to show All courses and allow user to add a course to profile
- 2 to show user registered courses
- 3 to Show profile
- 0 to quit

What would you like to do?: """

user_choice = int(input(show_menu))
while user_choice != 0:
    if user_choice == 1:
        register_course()
    elif user_choice == 2:
        show_registered_courses()
    elif user_choice == 3:
        show_profile()
    else:
        print("You have Entered an invalid choice!!!, Please enter a valid input!!!!!")
    user_choice = int(input(show_menu))

