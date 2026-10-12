usernames = ['boy1','boy2','boy3']
passwords = ['abc123','def456','xyz789']

def login():
    username = input("Enter username: ")
    if username in usernames:
        index = usernames.index(username)
        password = input("Enter password: ")
        if password == passwords[index]:
            print("Login successful!\n")
            return True
        else:
            print("Wrong password!\n")
    else:
        print("Username not found!\n")

def add_user():
    username = input("Enter new username: ")
    if username in usernames:
        print("Username already exists!\n")
        return
    password = input("Enter password: ")
    usernames.append(username)
    passwords.append(password)
    print("User added successfully!\n")

is_running=True
def menu():
    global is_running
    while is_running==True:
        print("1. Login")
        print("2. Add User")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            if login()==True:
                is_running=False
        elif choice == "2":
            add_user()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice!\n")

menu()
