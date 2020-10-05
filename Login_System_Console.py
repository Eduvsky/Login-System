users = []
passwords = []
status = ''

def newuser():
    newname = input('Enter a new name : ')
    while newname in users:
        print('name already taken, please enter a new one ')
        newname = input('Enter a new name : ')  
    users.append(newname)
    newpassword = input('Enter a password : ')
    passwords.append(newpassword)

def olduser():
    namecheck = input('enter your username : ')
    if namecheck not in users:
        while namecheck not in users:
            print('Error 404 // enter your name again')
            namecheck = input('enter your username : ')
    password_check = input('Enter your password : ')
    if passwords[users.index(namecheck)] == password_check:
        print('\n\nCongratulations you\'re logined in\n\n')
    else:
        while passwords[users.index(namecheck)] != password_check:
            print('\n\nError // wrong password\n\n')
            break


def MainMenu():
    while True:
        status = input('Are you registered y/n  ?  ')
        if status == 'y':
            olduser()
        if status == 'n':
            newuser()

MainMenu()