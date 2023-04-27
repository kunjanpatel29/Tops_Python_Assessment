# Write a program to demonstrate the bank management Console based application.

from datetime import datetime

print("WELCOME TO PYTHON BANK MANAGEMENT SYSTEM"+"\n")

print("Select your role")
print("\t1) Banker")
print("\t2) Customer")
print("\t3) Exit")

while True:
    
    choice = int(input("\nChoose Your role : "))
    
    if choice == 1:         
        print("\nWeclome to Banker's app")
        print("\n\t\t Operations Menu")
        print("\t\t 1) Add Customer")
        print("\t\t 2) View Customer")
        print("\t\t 3) Search Customer")
        print("\t\t 4) View All Customer")
        print("\t\t 5) Total Amounts in Bank")
                
    elif choice == 2:
        print("\nWeclome to Customer's app")
        print("\n\t\t Operations Menu")
        print("\t\t 1) Withdraw Amount")
        print("\t\t 2) Deposite Amount")
        print("\t\t 3) View Balance")

    elif choice == 3:
        print("Exit Bank Application")
        break
    else:
        print("Exit")
        break
    
    while True:
        choice = int(input("Enter Operation Which You Want to Perform : "))
        if choice == 1:
            acno = int(input("Enter Account Number : "))
            cname = input("Enter Customer Name : ")
            balance = int(input("Enter Opening Balance : "))
            now = datetime.now()
            
        elif choice == 2:
            d={}
            d[acno] = {}
            d[acno]["name"] = cname 
            d[acno]["balance"]= balance
            d[acno]["Opening Date"] = now
            print(d)
        
        elif choice == 3:
            acno = int(input("Enter Account Number : "))
            if acno in d:
                print("Exists")
            else:
                print("Not Exists")

        elif choice == 4:
            print(d)
            
        elif choice == 5:
            d[acno]["balance"] += balance
            print("Total Amounts in bank is : ",d[acno]["balance"])
        else:
            print("Exit")
            break

    answer = input("Do you want to perform more operations press 'y' for yes and press 'n' for no:")
    answer = answer.lower()
    if answer !='y':
        break

        while True:
            choice = int(input("Enter Operation Which You Want to Perform : "))

            if choice == 1:
                print("Withdraw Amount")

            elif choice == 2:
                print("Deposit Amount")

            elif choice == 3:
                print("View Balance")

            else:
                print("Exit")
                break    
                                
