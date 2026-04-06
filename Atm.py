import json

try:
    with open("Atm.json","r") as f:
        all_accounts=json.load(f)
        print("Data loaded back into the program!")
except (FileNotFoundError, json.decoder.JSONDecodeError):
    all_accounts={}
    
menu={
    "1":"Create an account",
    "2":"Choose your account",
    "3":"Exit"
    }

account_menu={
    "1":"Savings",
    "2":"Current"
    }

status=""

while True:
        print(menu)
        user_choice=int(input("Enter your choice : "))
        
        if user_choice==1:
            print(account_menu)
            a_choice=int(input("Enter your choice: "))
            
            if a_choice==1:
                status="Savings"
            elif a_choice==2:
                status="Current"
            else:
                print("Wrong choice!")
                break
        
            name=input("Enter your name : ")
                
            if (name in all_accounts):
                print("This name is already taken!")
                continue
            age=input("Enter your age: ")
            PIN=int(input("Create a pin: "))
            co_PIN=int(input("Re-enter pin: "))
            
            if PIN==co_PIN:
                print("Account has successfully been created!")
                all_accounts[name]={
                    "age": age,
                    "pin": PIN,
                    "balance": 0,
                    "status": status
                        }
                
            else:
                print("Pin does not match")
                print("Please try again!")
                continue
                
            
        elif user_choice==2:
            p_flag=0
            flag=0
            if not all_accounts:
                print("No accounts exist in the system yet")
                continue
            
            co_name=input("Please enter your account name: ")
            
            ## to check if account present
            if (co_name in all_accounts):
                flag=1
            else:
                flag=0
            
            ## to check correct PIN
            if flag==1:
                co_PIN=0
                co_PIN=int(input("Enter your PIN: "))
                
                if (all_accounts[co_name]['pin']==co_PIN):
                    p_flag=1
                else:
                    p_flag=0
                    
            else:
                print("Account name not found in our system")
                continue
            
            # final checkup
            
            if not (p_flag==1) or not (flag==1):
                print("Information is invalid \n Please try again later")
                continue
            
            print("----ACCOUNT----")
            print(f"Account name: {co_name}")
            print(f"User's age: {all_accounts[co_name]['age']}")
            print(f"Account type: {all_accounts[co_name]['status']}")
            print(f"Account balance: {all_accounts[co_name]['balance']}")
            
            n_choice=int(input("Press 1 : open \nPress 2 : go back\n"))
            
            if n_choice==1:
                while True:
                    bank={
                        "1":"Check balance",
                        "2":"Deposit",
                        "3":"Withdraw",
                        "4":"Exit"
                    }
                
                    print(bank)
                    bank_choice=int(input("Enter your choice: "))
            
                    if bank_choice==1:
                        print(f"Your current balance is: {all_accounts[co_name]['balance']}")
                
                    elif bank_choice==2:
                        add=int(input("Enter the amount you want to add"))
                        all_accounts[co_name]['balance']+=add
                        print(f"Your current balance is: {all_accounts[co_name]['balance']}")
                
                    elif bank_choice==3:
                        print(f"Your current balance is: {all_accounts[co_name]['balance']}")
                        withdraw=int(input("Enter the amount you want to withdraw"))
                    
                        if(withdraw>all_accounts[co_name]['balance']):
                            print("Invalid process, Please try again!")
                        else:
                            all_accounts[co_name]['balance']-=withdraw
                            print(f"Your current balance is: {all_accounts[co_name]['balance']}")
                
                    else:
                        break
            
        else:
            print("Good bye!")
            break
        
with open("Atm.json","w") as f:
    json.dump(all_accounts, f,indent=4)
    
                
                
                
                
                
                
            

            
            
            
                
                
            
                
                
                   
                    
            
                
                
            
            
            
            
            
    
    
    
                    
    
    
    
   
       
                                     
                        
            
    

    
    
    
        


           