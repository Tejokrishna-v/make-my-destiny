## make my destiny
import random
from time import sleep

credentials ={}

def otp():
    user_otp = random.randint(1000,9999)
    return user_otp
##def phlenchk():
##     phone_no =int(input ("Enter Your Mobile Number:"))
##     if len(phone_no)==10:
##        return email_id
##     else:
##        return phlenchk()
##        
def create_account():
    print("\n*****Welcome To Account Creation*****")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    print("Your Full Name :",first_name+last_name)
    phone_no =input ("Enter PHNO : ")
##    if phone_no == phlenchk():
    email_id = input ("Enter  Email-ID: ")
    user_name = input ("Enter User-Name: ")
    password = input ("Enter Password: ")
    confirm_password = input ("Enter Confirm Password: ")
    if password ==confirm_password:
        credentials['user_name']=user_name
        credentials['password']=password
        credentials['first_name']=first_name
        credentials['last_name']=last_name
        credentials['phone_no']=phone_no
        credentials['email_id']=email_id
        o=otp()
        print("Generating OTP for you.....!")
        sleep(2)
        print("Your otp: ",o)
        u_otp = int(input ("Enter OTP : "))
        if o==u_otp:
            print("ACCOUNT Created !!!")
        else:
            print("Invalid OTP..!")
    else:
        print("Please Check Your confirm-password ")
    

def login():
    print("\n*****Welcome To Login Page*****")
##    print(credentials['user_name'])
    user_name = input("Enter User-name: ")
    if credentials['user_name'] == user_name:
        print("Hello' ",credentials['first_name'],"",credentials['last_name']," ")
        password = input("Now Enter Password : ")
        if credentials['password'] ==password:
            print(" Login Successful :\n ")
            booking()
        else:
            print("Invalid Password for '",user_name,"' Please login again ")
    else:
        print("User Not Found ")   

def main():
    while True:
        print("\n*****-----***  MAKE MY DESTINY  ***-----***** ")
        print("  Available options here  ")
        
        if len(credentials) == 0:
            print("1. CREATE NEW ACCOUNT")

        print("2. LOGIN")
        print("3. Quit")
        choice = int(input("Enter Your Choice Here:==> "))
        if choice ==1:
            create_account()
        elif choice ==2:
            login()
        elif choice ==3:
            print("THANK YOU VISIT AGAIN..\n")
            break
        else:
            print("PLEASE ENTER VALID OPTION.")


def booking():
    print("***---Types of BOOKINGS---***")
    print("1. Buss")
    print("2. Train")
    print("3. Flight")
    print("4. Hotel")
    print("5. EXIT ")
    option=int(input("Enter Your Choice Here:==> "))
    if option==1:
        print("-----Welcome to BUSS booking-----")
        buss()
    elif option==2:
        print("-----Welcome to TRAIN booking-----")
        Train()
    elif option==3:
        print("-----Welcomr to FLIGHT booking-----")
        Flight()
    elif option==4:
        print("-----Welcome to HOTEL booking-----")
        Hotel()
    else:
        print("INVALID OPTION--!")

def buss():
    while True:
        print("\nWelcome to BUSS booking\n")
        froms =input("BORDING POINT :--   ")
        to =input("DROPING POINT :--  ")
        date_of_journey = input("Select journey date :--  ")
        time = input("Select Bording Time :--  ")
        num_of_persons=int(input("Persons to Travel :--  "))
##        if credentials [username]==username:
        credentials['froms']=froms
        credentials['to']=to
        credentials['date_of_journey']=date_of_journey
        credentials['time']=time
        credentials['num_of_persons']=num_of_persons
        print("success-------!!...")
        seat()
        break
           
def seat():
    while True:
        print("\n welcome to seat selection------! ")
        seat_selection =input("SELECT SEAT : ")
        if seat_selection !='' :
            credentials[seat_selection]=seat_selection
            print("Seat Successfully Booked")
            payments()
            break
        else:
            print("please select your seat")
            

def Train():
    while True:
        print("\n welcome to Train booking\n")
        froms =input("Starting From  :--   ")
        to =input("Destiny To :--   ")
        date_of_journey = input("Select journey date :--   ")
        num_of_persons=int(input("Persons to Travel :--   "))
        credentials['froms']=froms
        credentials['to']=to
        credentials['date_of_journey']=date_of_journey
        credentials['num_of_persons']=num_of_persons
        print("success-------!!...")
        seat()
        break

def Flight():
     while True:
        print("\n welcome to Flight booking\n")
        froms =input("Starting From :--   ")
        to =input("Destiny To :--   ")
        date_of_journey = input("Select journey date :--   ")
        num_of_persons=int(input("Persons to Travel :--   "))
        credentials['froms']=froms
        credentials['to']=to
        credentials['date_of_journey']=date_of_journey
        credentials['num_of_persons']=num_of_persons
        print("success-------!!...")
        seat()
        break

def Hotel():
     while True:
        print("\n welcome to Hotel booking\n")
        froms =input("BORDING POINT :--   ")
        to =input("DROPING POINT :--   ")
        date_of_journey = input("Select journey date :--   ")
        num_of_persons=int(input("Persons to Travel :--   "))
        credentials['froms']=froms
        credentials['to']=to
        credentials['date_of_journey']=date_of_journey
        credentials['num_of_persons']=num_of_persons
        print("success-------!!...")
        seat()
        break

def payments():
    print("\n ***---Types of PAYMENTS---***")
    print("1. PhonePe")
    print("2. PayTm")
    print("3. Debit Card")
    print("4. Credit Card")
    print("5.Wallet")
    option=int(input("Enter Your Choice Here:==> "))
    if option==1:
        print("-----Your Choosed The PhonePe-----")
    elif option==2:
        print("-----Your Choosed The  PayTm-----")
    elif option==3:
        print("-----Your Choosed The Debit Card-----")
    elif option==4:
        print("-----Your Choosed The Credit Card-----")
    elif option==5:
        print("-----Your Choosed The Wallet-----")
        main()
    else:
        print("\n invalid option")
        return payments()


main()
