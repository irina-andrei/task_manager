#=====Importing Libraries=====
import datetime as dt
from datetime import date


#=====Formatting Options=====
RED = '\033[31m'
GREEN = '\033[92m'
BLUE = '\033[94m'
PINK = '\033[95m'
CYAN = '\033[96m'
UNDERL = '\033[4m' # 'Underline'
ENDC = '\033[0m' # Removes all formatting applied.
EM = f"{RED}‼{ENDC}" 
# 'Exclamation Mark' shorthand, preventing repeat code or going over 79char.



def login():
    #===Username Check===
    while True:
        user_name = input(f"Please enter your username: {CYAN}").lower()
        if user_name not in my_users:
            print(f"{EM} Sorry. Username {RED}not found{ENDC}.")
            continue
        # If it doesn't find username in the dictionary, it will
        # continue to ask for it until user enters a valid one.
        break

    print(f"{ENDC}Hi, {CYAN}{user_name}{ENDC}. ", end='')

    #===Password Check===
    while True:
        password = input(f"{ENDC}Enter your password: {CYAN}")
        if password != my_users[user_name]:
            print(f"{EM} Sorry. You entered the {RED}wrong password{ENDC}.",
            f"Remember it's {UNDERL}case sensitive{ENDC}. Let's try again.")
            continue
        # Continues to ask for password until user enters the correct one.
        print(f"{GREEN}Success.{ENDC}",
        f"You have been logged in, {CYAN}{user_name}{ENDC}.")
        break

    return user_name


def reg_user():
    if username != 'admin':
        print(f"{EM} Sorry. Only {RED}admin{ENDC} can add new users.")
        return None
    # Only the 'admin' is allowed to register users.
    
    new_username = input(f"Enter the new username: {CYAN}").lower()
    while new_username in my_users:
        print(f"{EM} Sorry, '{CYAN}{new_username}{ENDC}' is already in use.")
        new_username = input(f"Try again. Enter new username: {CYAN}").lower()
    new_password = input(f"{ENDC}Enter new password: {CYAN}")
    confirmation = input(f"{ENDC}Please confirm the password: {CYAN}")
    
    # This will check the 2 passwords entered are matching.
    if new_password == confirmation:
        with open('user.txt', 'a', encoding='utf-8') as user_file:
            user_file.write(f"\n{new_username}, {new_password}")
        my_users[new_username] = new_password
        user_stats[new_username] = [0, 0, 0]
        # Adds the new user to the 'user.txt' file and to dictionary.
        # Creates new entry in the user stats dictionary for report counting.
        print(f"{GREEN}Success.{ENDC} '{new_username}' was added.")
    else:
        print(f"{EM} Passwords {RED}don't match{ENDC}, user not added.")


def add_task():
    name = input(f"Who do you want to assign a task to? {CYAN}").lower()
    if name not in my_users:
        print(f"{EM} Sorry. '{name}' username {RED}not found{ENDC}.")
        return None
    # If the user doesn't exist, program goes back to menu selection.
    
    title = input(f"{ENDC}What's the title of the task? {CYAN}")
    descr = input(f"{ENDC}Enter description of task: {CYAN}")
    due = input(f"{ENDC}When is the due date? {CYAN}")
    today = date.today().strftime("%d %b %Y")
    # Today's date in the appropriate format 'dd Mmm yyyy'.
    
    with open('tasks.txt', 'a', encoding='utf-8') as task_file:
        task_file.write(f"\n{name}, {title}, {descr}, {today}, {due}, No")
    # Writes the new task to the file in the appropriate format.


def view_all():
    tasks_file = open('tasks.txt', 'r', encoding='utf-8')
    print(f"{BLUE}{'─'*86}{ENDC}")
    
    for line in tasks_file:
        line_data = line.strip().split(", ")
        print(f"Task: {' '*12}{CYAN}{line_data[1]}{ENDC}",
            f"\nAssigned to: {' '*5}{CYAN}{line_data[0]}{ENDC}",
            f"\nDate assigned: {' '*3}{CYAN}{line_data[3]}{ENDC}",
            f"\nDue date: {' '*8}{CYAN}{line_data[4]}{ENDC}",
            f"\nTask complete? {' '*3}{CYAN}{line_data[5]}{ENDC}",
            f"\nTask description:", f"\n   {CYAN}{line_data[2]}",
            f"\n{BLUE}{'─'*86}{ENDC}")
    # For each line in the file represented by a task, it will print out
    # in the appropriate order all the details of each task. 
    
    tasks_file.close()


def view_mine():
    tasks_file = open('tasks.txt', 'r', encoding='utf-8')
    print(f"{BLUE}{'─'*86}{ENDC}")
    
    counter = 0
    choice = 0
    my_tasks_list = []
    other_tasks_list = []
    # Declaring all the variables needed. 

    for line in tasks_file:
        line_data = line.strip().split(", ")
        
        # If statement checks if the task is assigned to current user.
        if username == line_data[0]:
            counter += 1
            # Counts the total number of tasks for logged-in user.
            
            print(f"Task ID number:{' '*3}== {PINK}{counter}{ENDC} ==",
            f"\nTask: {' '*12}{CYAN}{line_data[1]}{ENDC}",
            f"\nAssigned to: {' '*5}{CYAN}{line_data[0]}{ENDC}",
            f"\nDate assigned: {' '*3}{CYAN}{line_data[3]}{ENDC}",
            f"\nDue date: {' '*8}{CYAN}{line_data[4]}{ENDC}",
            f"\nTask complete? {' '*3}{CYAN}{line_data[5]}{ENDC}",
            f"\nTask description:", f"\n   {CYAN}{line_data[2]}",
            f"\n{BLUE}{'─'*86}{ENDC}")
            # Prints out logged-in user tasks in appropriate order. 
            
            my_tasks_list.append(line_data)
            # Saves logged in user tasks in a list.
        else:
            other_tasks_list.append(line_data)
            # Saves all other tasks in a list.

    tasks_file.close()

    if counter == 0:
        print(f"{CYAN}{username}{ENDC}, you have no tasks assigned.")
        print(f"{BLUE}{'─'*86}{ENDC}")
        return None
    # In the case of no tasks found for logged-in user, it exits the function.
    
    while True:
        print(f"\n{ENDC}Edit a task by entering the {PINK}task ID{ENDC}.")
        choice = int(input(f"Select task ID or -1 to return to menu: {PINK}"))

        if choice == -1:
            return None
        # If user selects -1, it will exit the function.

        if my_tasks_list[choice-1][5] == "Yes":
            print(f"{EM} You can't edit a completed task.")
            continue
        # If user selected a completed task, it loops back for another choice.

        edit_or_complete = input(f'''
        Please select one of the following options:
        \b\b♦ {CYAN}a.{ENDC} Mark task {PINK}#{choice}{ENDC} as complete.
        \b\b♦ {CYAN}b. {ENDC} Edit task {PINK}#{choice}{ENDC}.
        {ENDC}Your selection: {CYAN}''').lower()
        
        print(f"{ENDC}", end='') # Resetting colour formatting. 
        
        if edit_or_complete == 'a':
            my_tasks_list[choice-1][5] = "Yes"
            print(f"Task {PINK}#{choice}{ENDC} marked {GREEN}complete{ENDC}.")
            break
        elif edit_or_complete != 'b':
            print("You entered an invalid option. Let's try again.")
            continue
        
        # The following code will only run if user chose 'b' - editing task.
        print(f"{ENDC}You're editing task {PINK}#{choice}{ENDC}.")

        while True:
            print(f"\nEditing Options for task {PINK}#{choice}{ENDC}:",
            f"\n{CYAN}1:{ENDC} Reassign the task to another user",
            f"\n{CYAN}2:{ENDC} Change the due date of the task",
            f"\n{CYAN}3:{ENDC} Exit editing task {PINK}#{choice}{ENDC}")
            
            editing_choice = input(f"\tYour selection: {CYAN}")
            if editing_choice == '3':
                break
            elif editing_choice == '2':
                my_tasks_list[choice-1][4] = input(f"New due date: {CYAN}")
                print(f"{GREEN}Success.{ENDC} Due date changed.")
            elif editing_choice == '1':
                my_tasks_list[choice-1][0] = input(f"Enter new user: {CYAN}")
                print(f"{GREEN}Success.{ENDC} Task reassigned.")

        for task in my_tasks_list:
            other_tasks_list.append(task)
        all_tasks = other_tasks_list
        # Merging both task lists into one list.
            
        with open('tasks.txt', 'w', encoding='utf-8') as task_file:
            task_file.write(", ".join(all_tasks[0]))
        # Writing only position [0] with 'w' to override previous file.
        # The rest of the tasks can now be appended to this file. 
        
        for list_task_info in all_tasks:
            if list_task_info == all_tasks[0]:
                continue
            # We need to skip position [0] as this has been added already.

            current_line = ", ".join(list_task_info)
            
            with open('tasks.txt', 'a', encoding='utf-8') as task_file:
                task_file.write("\n" + current_line)
        # 'all_tasks' is a list of lists, so we need to iterate through
        # the list one by one and add each current line to the file.


def reports():
    generated_files = True
    # This boolean check will confirm the 2 report files were generated.

    #=====Task Report===== (saved to 'task_overview.txt')
    with open('task_overview.txt', 'w', encoding='utf-8') as task_overview:
        task_report, number_tasks = generate_tasks_report()
        task_overview.write(task_report)

    #=====User Report===== (saved to 'user_overview.txt')
    user_report = f"The total number of users registered: {len(my_users)}"
    user_report += f"\nThe total number of tasks: {number_tasks}\n"
    
    for user, stats_list in user_stats.items():
        user_report += f"\n\t== Statistics for '{user}' =="
        
        user_total = stats_list[0]
        completed_tasks = stats_list[1]
        overdue_tasks = stats_list[2]

        not_completed = user_total - completed_tasks
        
        if number_tasks == 0:
            perc = 0
        else:
            perc = int(user_total/number_tasks*100)
        
        if user_total == 0:
            complete_perc = 0
            incompl_perc = 0
            overdue_perc = 0
        else:
            complete_perc = int(completed_tasks/user_total*100)
            incompl_perc = int(not_completed/user_total*100)
            overdue_perc = int(overdue_tasks/user_total*100)
        # These if statements will help avoid ZeroDivisionError problems. 
        
        user_report += f"\nThe number of tasks assigned: {user_total}"
        user_report += f"\nTasks assigned compared to total nr tasks: {perc}%"
        user_report += f"\nPercentage of tasks completed: {complete_perc}%"
        user_report += f"\nPercentage of tasks uncompleted: {incompl_perc}%"
        user_report += f"\nPercentage of tasks overdue: {overdue_perc}%\n"

    with open('user_overview.txt', 'w', encoding='utf-8') as user_overview:
        user_overview.write(user_report)


def generate_tasks_report():
    '''A function that generates the tasks report as well as counts all
    information necessary we'll need for generating the user report.'''
    nr_tasks = 0
    completed = 0
    not_completed = 0
    overdue = 0
    
    tasks_file = open('tasks.txt', 'r', encoding='utf-8')
    for line in tasks_file:
        task_info = line.strip().split(", ")
        current_user = task_info[0]
        # Within current task, task_info[0] is the name of the task user.
        
        nr_tasks += 1
        # Counts the total number of tasks in the file.
        user_stats[current_user][0] += 1
        # Counts the number of tasks only for the current user.
        
        if task_info[5] == 'Yes':
            # Position [5] contains completion information.
            completed += 1
            user_stats[current_user][1] += 1
            # The 2 counters will count only completed tasks.
        else:
            not_completed += 1 
            # Counter for uncompleted tasks.
            due = dt.datetime.strptime(task_info[4], "%d %b %Y").date()
            # Due date converted from string (position [4]) to date format
            if due < date.today():
                overdue += 1
                user_stats[current_user][2] += 1
                # The 2 counters will count how many tasks are overdue.
    
    tasks_file.close()
    
    if nr_tasks == 0:
        incomplete_perc = 0
        overdue_percentage = 0
    else:
        incomplete_perc = int(not_completed/nr_tasks*100)
        overdue_percentage = int(overdue/nr_tasks*100)

    report = f"The total number of tasks: {nr_tasks}\n"
    report += f"The total number of completed tasks: {completed}\n"
    report += f"The total number of uncompleted tasks: {not_completed}\n"
    report += f"The total number of overdue tasks: {overdue}\n"
    report += f"The percentage of uncompleted tasks: {incomplete_perc}%\n"
    report += f"The percentage of overdue tasks: {overdue_percentage}%"

    return report, nr_tasks


def stats():
    if username != 'admin':
        print(f"{EM} Sorry. Only {RED}admin{ENDC} can access this.")
        return None
    # Only the 'admin' is allowed to display statistics.
    
    if not generated_files:
        reports()
    # It will only call reports() if the files have not been generated yet.   
    
    task_report = {}
    # A dictionary that will hold all task reports.

    with open('task_overview.txt', 'r', encoding='utf-8') as t_overview:
        for index, line in enumerate(t_overview):
            task_report[index] = line.strip().split(": ")
    # Saving all the reports from file in the dictionary.

    print(f'''{GREEN}
    \t╒{'═'*45}╕
    \t│{' '*18}{PINK}STATISTICS{' '*17}{GREEN}│
    \t╞{'═'*45}╡
    \t│{ENDC}  Total number of users: {CYAN}{len(my_users)}{' '*19}{GREEN}│
    \t│{ENDC}  {task_report[0][0]}: {CYAN}{task_report[0][1]}{' '*15}{GREEN}│
    \t│{ENDC}  {task_report[1][0]}: {GREEN}{task_report[1][1]}{' '*5}│
    \t│{ENDC}  {task_report[2][0]}: {CYAN}{task_report[2][1]}{' '*3}{GREEN}│
    \t│{ENDC}  {task_report[3][0]}: {RED}{task_report[3][1]}{' '*7}{GREEN}│
    \t│{ENDC}  {task_report[4][0]}: {CYAN}{task_report[4][1]}{' '*3}{GREEN}│
    \t│{ENDC}  {task_report[5][0]}: {RED}{task_report[5][1]}{' '*7}{GREEN}│
    \t{GREEN}└{'─'*45}┘{ENDC}''')
    # Displays all statistics in a user-friendly format.

'''
number_tasks = 0
# This needs to be a global variable for access to functions. 
'''

#========Login Section========
my_users = {}
# A dictionary that will hold usernames and passwords. 
user_stats = {}
# A dictionary which will hold all counters for user reports.

with open('user.txt', 'r', encoding='utf-8') as user_file:
    for line in user_file:
        line_data = line.strip().split(", ")
        my_users[line_data[0]] = line_data[1]
        # Adding all usernames and passwords to dictionary.
        user_stats[line_data[0]] = [0, 0, 0]
        # Initialising all counters for each user to 0.

username = login()


#========Menu Section========


while True:
    # If user is admin, it will present the 'admin-only' menu.
    # NOTE: password for 'admin' is 'adm1n'.
    # User input is converted to lower case.
    if username == "admin":
        menu = input(f'''
        {PINK}╔{'═'*45}╗
        ║{ENDC} Please select one of the following options: {PINK}║
        ║ ♦{CYAN} r {ENDC}- Register user {PINK}{' '*24}║
        ║ ♦{CYAN} a {ENDC}- Add task {PINK}{' '*29}║
        ║ ♦{CYAN} va {ENDC}- View all tasks {PINK}{' '*22}║
        ║ ♦{CYAN} vm {ENDC}- View my tasks {PINK}{' '*23}║
        ║ ♦{CYAN} gr {ENDC}- Generate reports {PINK}{' '*20}║
        ║ ♦{CYAN} ds {ENDC}- Display statistics {PINK}{' '*18}║
        ║ ♦{RED} e {ENDC}- {UNDERL}Exit{ENDC}{PINK}{' '*34}║
        ╚{'═'*45}╝
        {ENDC}  Your selection: {CYAN}''').lower()
    
    # If user is not admin, the general menu will be presented.
    else:
        menu = input(f'''
        {PINK}╔{'═'*45}╗
        ║{ENDC} Please select one of the following options: {PINK}║
        ║ ♦{CYAN} r {ENDC}- Register user {PINK}{' '*24}║
        ║ ♦{CYAN} a {ENDC}- Add task {PINK}{' '*29}║
        ║ ♦{CYAN} va {ENDC}- View all tasks {PINK}{' '*22}║
        ║ ♦{CYAN} vm {ENDC}- View my tasks {PINK}{' '*23}║
        ║ ♦{RED} e {ENDC}- {UNDERL}Exit{ENDC}{PINK}{' '*34}║
        ╚{'═'*45}╝
    {ENDC}  Your selection: {CYAN}''').lower()
    
    print(f"{ENDC}", end='')
    # Resetting the colour formatting. 
    generated_files = False
    # This boolean value will show if the reports have been generated or not.
    
    if menu == 'r':
        # This allows 'admin' to add a new user to the 'user.txt' file.
        reg_user()
    elif menu == 'a':
        # This will add a task to the 'tasks.txt' file.
        add_task()
    elif menu == 'va':
        # This will display the information for each existing task.
        view_all()
    elif menu == 'vm':
        # This will only display tasks assigned to the logged-in user.
        view_mine()
    elif menu == 'gr':
        # This allows 'admin' to generate the reports on users and tasks.
        reports()
        print(f"Reports have been {GREEN}successfully{ENDC} generated.")
    elif menu == 'ds':
        # This allows 'admin' to display statistics.
        stats()
    elif menu == 'e':
        # This will exit the programme.
        print(f"{CYAN}Goodbye!{ENDC}")
        break
    
    else:
        print(f"{EM} You have made a wrong choice, please try again.")


#======References======
# Colour formatting from lectures with Logan.
# Date information from: https://docs.python.org/3/library/datetime.html
# https://stackoverflow.com/questions/23324266/converting-string-to-date-
# object-without-time-info