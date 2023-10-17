# Assesment :- 1.Python - Collections, functions and Modules in Python

import datetime

Bank = {}


file = open("Bank.txt","r") 
data  = file.readlines()

for line in data:
    Customer_data = line.strip() #Remove "" Quatation Mark
    if Customer_data:
        Customer_info = Customer_data.split(',') #Data Divide into ' '
        Account_no=int(Customer_info[0])
        Customer_name = Customer_info[1]
        Operning_Amount=int(Customer_info[2])
        opening_date = Customer_info[3]
        Bank[Account_no]={'Name': Customer_name,'Balance':Operning_Amount,'Opening Date' : opening_date}





while True:
    
    print("")
    print(" "*20,"WELCOME TO PYTHON BANK MANAGEMENT SYSTEM \n")
    print("")   
    print(" "*20,"Select Your Role ")
    print(" ")
    print(" "*20,"1) Banker")
    print(" "*20,"2) Customer")
    print(" "*20,"3) Exits")
    
    Role = input("Choose Your Role : ")
    try:
        Role = int(Role)
    except ValueError:
        print("Error Caught : Enter Role As A  Numberical Value ")


# Banker Choice
    if Role == 1:
        
        while True:
            print(" "*20,"Welcome to Banker's App")
            print(" ")
            print(" "*20,"1) Add Customer")
            print(" "*20,"2) View Customer")
            print(" "*20,"3) Search Customer")
            print(" "*20,"4) View All Cusomer")
            print(" "*20,"5) Total Amount In Bank")
            
            Operaction = input("Enter Operaction You Want To Perform : ")
                
            try:
                Operaction = int(Operaction)
            except ValueError:
                print("Error Caught : Enter Operation as a  Numberical Value ")
           
              
            if Operaction == 1: #Add Customer 
                
                Account_no = input("Enter Customer Account Number : ")
                try:
                    Account_no = int(Account_no)
                except ValueError:
                    print("Error Caught : Enter Numberical Value ")
                    continue
                
                if Account_no in Bank:
                    print("Account  Number Already Exists")
                    
                else:
                    Customer_name = input("Enter Customer Name : ")
                    Operning_Amount = input("Enter Customer Opening Amount : ")
                    try:
                        Operning_Amount = int(Operning_Amount)
                    except ValueError:
                        print("Error Caught : Enter Numberical Value ")
                        continue
                       
                    # Data Save In Dictionary 
                    opening_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    Bank[Account_no] = {'Name': Customer_name,'Balance':Operning_Amount,'Opening Date':opening_date}
                    print("Your Account is Successfully Created")
                    
                    

            
            
            elif Operaction==2: #View Customer
                
                Account_no = input("Enter Customer Account Number : ")
                try:
                    Account_no = int(Account_no)
                except ValueError:
                    print("Error Caught : Enter Numberical Value ")
                    continue
                
                if Account_no in Bank:
                    print(Bank[Account_no])
                else:
                    print(f"Account No- {Account_no} Does Not Exist")
            
            
            elif Operaction == 3: #Search Customer
                Account_no = input("Enter Customer Account Number : ")
                try:
                    Account_no = int(Account_no)
                except ValueError:
                    print("Error Caught : Enter Numberical Value ")
                    continue
                if Account_no in Bank:
                    print("Customer Account Available")
                else:
                    print("Customer Account Does Not Available in Bank")
            
            
            
            elif Operaction == 4: #View All Customer
                
                print(Bank)


            elif Operaction == 5: #Check Total Balance In Bank
                
                total_balance = 0
                for customer_data in Bank.values():
                    total_balance += customer_data['Balance']
                print("Total Amount In Bank:", total_balance)


            
            else:
                print("Invalid operation. Please try again")

            perform = input('Do you want to perform more operations Press "y" for yes or "n" for no: ')
            if perform.lower() != 'y':
                break


# Customer Choice
    if Role == 2:
        
        while True:
            print("")
            print(" "*20,"Welcome to Customer's App")
            print(" ")
            print(" "*20,"1) Widthraw Amount ")
            print(" "*20,"2) Deposit Amount")
            print(" "*20,"3) View Balance")

            
            Operaction = input("Enter Operaction You Want To Perform : ")
                
            try: # Try use for only Accept int Value
                Operaction = int(Operaction)
            except ValueError:
                print("Error Caught : Enter Numberical Value ")
                
                
            if Operaction == 1: #Withdraw Ammount
                
                Account_no = input("Enter Customer Account Number : ")

                
                if Account_no in Bank:
                    Withdraw_amount = input("Enter Customer Withdraw Amount : ")
                    try:
                        Withdraw_amount= int(Withdraw_amount)
                    except ValueError:
                        print("Error Caught : Enter Withdraw As Numberical Format")
                        continue
                    
                    if Bank[Account_no]['Balance'] >= Withdraw_amount:
                        Bank[Account_no]['Balance'] -= Withdraw_amount
                        print("Your New balance is : ", Bank[Account_no]['Balance'])
                    else:
                        print("Zero Balance")
                else:
                    print("Account Not Exist , Enter Valid Account Number")
            
            
            elif Operaction==2: #Deposit Amount
                
                Account_no = input("Enter Customer Account Number : ")

                
                if Account_no in Bank:
                    Deposit_Amount = input("Enter Customer Deposit_Amount : ")
                    try:
                        Deposit_Amount= int(Deposit_Amount)
                    except ValueError:
                        print("Error Caught : Enter Numberical Value ")                   
                        continue
                    
                    Bank[Account_no]['Balance'] += Deposit_Amount
                    print("Your New balance is : ", Bank[Account_no]['Balance'])
                
                else:
                    print("Account Not Exist , Enter Valid Account Number")
            
            elif Operaction == 3: #View balance
                Account_no = input("Enter Customer Account Number : ")
                
                if Account_no in Bank:
                    print(Bank[Account_no]['Balance'])
                    
                else:
                    print("Account Not Exist , Enter Valid Account Number")
                continue
                    
            else:
                print("Invalid operation. Please try again")
            
            perform = input('Do you want to perform more operations Press "y" for yes or "n" for no: ')
            if perform.lower() != 'y':
                break
        
    elif Role==3:
        print("You Are Successfully Exit")
        break
    
    else:
        print("Invalid operation. Please try again")
        
                 

# Data save using File Management
file = open("Bank.txt", "w")
for account_no, customer_data in Bank.items():
    file.write(f"{account_no},{customer_data['Name']},{customer_data['Balance']},{customer_data['Opening Date']}\n")
file.close()         
           
        