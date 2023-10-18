# Assesment :- 1.Python - Collections, functions and Modules in 

import datetime

Fruit = {}

file = open("Fruit.txt","r") # read File
data  = file.readlines()

for line in data:
    Fruit_data = line.strip() #Remove "" Quatation Mark
    if Fruit_data:
        Fruit_info = Fruit_data.split(',') #Data Divide into ' '
        Add_Fruit=int(Fruit_info[0])
        fruit_name = Fruit_info[1]
        fruit_qty=int(Fruit_info[2])
        fruit_Amount = Fruit_info[3]
        Fruit[Add_Fruit]={'Name': fruit_name,'Quantity':fruit_qty,'Amount' : fruit_Amount}


while True:

    print("")
    print(" "*20,"WELCOME TO PYTHON FRUIT MANAGEMENT SYSTEM \n")
    print("")   
    print(" "*20,"Select Your Role ")
    print(" ")
    print(" "*20,"1) Manager")
    print(" "*20,"2) Customer")
    print(" "*20,"3) Exits")

    Role = input("Choose Your Role : ")
    try:
        Role = int(Role)
    except ValueError:
        print("Error Caught : Enter Role As A  Numberical Value ")

# Manager Choice
    if Role == 1:

        while True:
            print(" "*20,"Welcome to Fruit's App")
            print(" ")
            print(" "*20,"1) Add Fruit stock")
            print(" "*20,"2) View Fruit stock")
            print(" "*20,"3) Update Fruit stock")
           
            Operaction = input("Enter Operaction You Want To Perform : ")

            try:
                Operaction = int(Operaction)
            except ValueError:
                print("Error Caught : Enter Operation as a  Numberical Value ")


            if Operaction == 1: #Add Fruit

                Add_Fruit = input("ADD FRUIT STOCK ")
                try:
                    Add_Fruit = str(Add_Fruit)
                except ValueError:
                    print("Error Caught : Enter Numberical Value ")
                    continue

                if Add_Fruit in Fruit:
                    print("Fruit is  Already Exists")

                else:
                    fruit_name = input("Enter Fruit Name : ")
                    fruit_qty = input("Enter Fruit qty(in kg) : ")
                    fruit_Amount = input("Enter Fruit  price : ")
            
                    
                    # Data Save In Dictionary 
                    opening_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    Fruit[Add_Fruit] = {'Name': fruit_name,'Quantity':fruit_qty,'Amount':fruit_Amount}
                    print("Your Fruit is Successfuly Add")
                    

            elif Operaction==2: #View Fruits

                Add_Fruit = input("Enter Fruit name : ")
                try:
                    Add_Fruit = str(Add_Fruit)
                except ValueError:
                    print("Error Caught : Enter Numberical Value ")
                    continue

                if Add_Fruit in Fruit:
                    print(Fruit[Add_Fruit])
                else:
                    print(f"fruit is- {Add_Fruit} Does Not Exist")



            elif Operaction == 3: #update Fruits
                Add_Fruit = input("Enter Fruit name : ")
                try:
                    Add_Fruit = str(Add_Fruit)
                except ValueError:
                    print("Error Caught : Enter Numberical Value ")
                    continue
                if Add_Fruit in Fruit:
                    print("Fruits are available")
                else:
                    print("Fruit are not available in Fruit")


                    
# Data save using File Management
file = open("Fruit.txt", "w")
for Add_Fruit, Fruit_data in Fruit.items():
    file.write(f"{Fruit_no},{Fruit_data['Name']},{Fruit_data['qty']},{Fruit_data['Amount']}\n")
file.close() 