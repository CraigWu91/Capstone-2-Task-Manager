# Import datetime module to use in tasks and get current date
import datetime

# Boolean to check if logged in
logged_in = False

# Request user input
username = input("Please enter your username: ")
password = input("Please enter your password: ")

# Open user text file to split and strip the lines
# Check if user input matches the user text file, if yes then change boolean to True
# Use seek function to start the loop lines search back at 0 so login works after unsuccessful login
with open("user.txt", "r") as f:
    while logged_in == False:
        for line in f:
            data = line.split(",")
            user = data[0].strip()
            pas = data[1].strip()
            if username == user and password == pas:
                print("Login successful")
                logged_in = True
        if logged_in == False:
            print("Login unsuccessful")
            username = input("Please enter your username: ")
            password = input("Please enter your password: ")
            f.seek(0)

# Presenting the menu to the user
# Convert all user inputs to lower case
# Added extra if statement for compulsory task2 so only admin can see register user and statistics, will not display these for other users
while True:
    if username == "admin":
        menu = input('''Please select one of the following options:
    r - register user
    a - add task
    va - view all tasks
    vm - view my tasks
    s - statistics
    e - Exit
    : ''').lower()
    elif username != "admin":
        menu = input('''Please select one of the following options:
    a - add task
    va - view all tasks
    vm - view my tasks
    e - Exit
    : ''').lower()

# Create a new user to be registered to the user text file
# Ask user to input the password twice, if they are the same then successfully add to user text file
    if menu == "r":
        new_username = input("Please enter a new username: ")
        new_password = input("Please enter a new password: ")
        new_password2 = input("Please enter your new password again: ")
        if new_password2 == new_password:
            with open("user.txt", "a") as g:
                g.write(f"\n{new_username}, {new_password}")
                print("User successfully registered")
        else:
                print("Your password confirmation is incorrect, please try again")

# Create a new task to be added to to task text file
# Used datetime module to get current date and convert to appropriate format
    elif menu == "a":
        t_username = input("Please enter username assigned to this task: ")
        t_title = input("Please provide the title of this task: ")
        t_description = input("Please provide a description of this task: ")
        t_date = input("What is the due date for this task? eg. 10 Oct 2023: ")
        t_today = datetime.date.today()
        t_today = t_today.strftime("%d %b %Y")
        t_complete = "No"
        with open("tasks.txt", "a") as h:
            h.write(f"\n{t_username}, {t_title}, {t_description}, {t_today}, {t_date}, {t_complete}")
            print("Task successfully added")

# View all tasks in tasks text file
# Open tasks file to split and strip lines for appropriate display
    elif menu == "va":
        with open("tasks.txt", "r") as i:
            for lines in i:
                data2 = lines.strip().split(",")
                print(f"\nAssigned to: \t{data2[0]} \nTitle: \t{data2[1]} \nDescription: \t{data2[2]} \nDate assigned: \t{data2[3]} \nDate due: \t{data2[4]} \nTask Complete? \t{data2[5]}")

# View only tasks of logged in user by checking lines in position 0 is the username of logged in user
    elif menu == "vm":
        with open("tasks.txt", "r") as j:
            for lines in j:
                data3 = lines.strip().split(",")
                if data3[0] == username:
                    print(f"\nAssigned to: \t{data3[0]} \nTitle: \t{data3[1]} \nDescription: \t{data3[2]} \nDate assigned: \t{data3[3]} \nDate due: \t{data3[4]} \nTask Complete? \t{data3[5]}")

# Added statistics menu to count the number of lines in tasks and user file to determine how many in each file
    elif menu == "s":
        with open("tasks.txt", "r") as k:
            x = len(k.readlines())
            print(f"Total number of tasks is {x}")
        with open("user.txt", "r") as l:
            y = len(l.readlines())
            print(f"Total number of users is {y}")

# Exit program
    elif menu == "e":
        print('Goodbye!!!')
        exit()

# If user has made an invalid choice
    else:
        print("You have made a wrong choice, Please Try again")