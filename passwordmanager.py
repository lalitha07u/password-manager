import hashlib
import getpass
password_manager = {}
def create_account():
    username = input("enter the usertname") 
    password = getpass.getpass("enter your password")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print("account created successfully")

def login():
    username = input("enter your username")
    password = getpass.getpass("enter your password")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("login successful")
    else:
        print("login is not succesfull")


def main():
    while True:
        choice = input("enyter 1 to create an account,2 to login: or 0 to exit ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "0":
            break
        else:
            print("invalid choice")

            
if __name__== "__main__":
    main()
