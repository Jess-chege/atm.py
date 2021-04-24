import random
import validation
import database

def __init__(self, balance=500):

       self.balance = balance

       print("Hello!! Welcome to Bank Of Africa")

       have_account = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))


       if have_account == 1:

           login()

       elif have_account == 2:

            register()

       else:
           print("You have selected invalid option")

           init()
def login():
    print("Login")

    account_number_from_user = input("What is your account number? \n")

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = getpass("What is your password \n")

        user = database.authenticated_user(account_number_from_user, password)

        if user:
            bank_operation(user)

        print('Invalid account or password')
        login()

def register():
    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = getpass("Create a password for yourself \n")

    account_number = generation_account_number()

    is_user_created = database.create(account_number, first_name, last_name, email, password)

    if is_user_created:

        print("Your Account Has been created")
        print(" == ==== ====== ===== ===")
        print("Your account number is: %d" % account_number)
        print("Make sure you keep it safe")
        print(" == ==== ====== ===== ===")

        login()

    else:
        print("Something went wrong, please try again")
        register()

def bank_operation(customer):
       print("Welcome %s  " % (customer[1]))


       selectedOption = int(input('Please select an option (1) deposit (2) withdrawal (3) Logout (4) Exit \n'))
       choice = input()

       if choice == '1':

          print('How much would you like to withdraw')
          take = int(input())

       if take % 100 == 0:
          print('please take your cash')

       elif choice == 2:
          print('how much would you like to deposit')
          take = int(input())

       if take % 100 == 0:
          print('current balance is 100 input')

       else:
          print('what issue would you like to report?')
          take = str(input())
          print('Thank you for contacting us')

       if choice == '1':

        print('How much would you like to withdraw')
        take = int(input())

       if take % 100 == 0:
            print('please take your cash')

       elif choice == 2:
        print('how much would you like to deposit')
        take = int(input())

       if take % 100 == 0:
            print('current balance is 100 input')

       else:
        print('what issue would you like to report?')
        take = str(input())
        print('Thank you for contacting us')
def withdrawal_operation():
    print("withdrawal")


def deposit_operation():
    print("Deposit Operations")

def generation_account_number():
    return random.randrange(1000000, 9999999)

def logout():
    login()

