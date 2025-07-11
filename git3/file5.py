users = {}

def register():
    username = input("Create username: ")
    if username in users:
        print("Username already exists.")
        return
    password = input("Create password: ")
    users[username] = password
    print("User registered successfully!")

def login():
    username = input("Username: ")
    password = input("Password: ")
    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Invalid credentials.")

while True:
    print("\n1. Register\n2. Login\n3. Exit")
    choice = input("Choice: ")
    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        break
    else:
        print("Invalid option.")

