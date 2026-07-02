import sys
import pandas as pd
import random
from datetime import datetime




#---------------------------------------------------------------------------------------------------------------------------------

class create_acc:
    def __init__(self):
        self.name=input("Enter ur name\n")
        self.location=input("Enter ur location\n")
        user_number=str(self.__generate())
        print("Your new user_id is",user_number)
        
        #PASSWORD RECAPTCHA
        while True:
            password=input("Enter a new password \n")
            re_pass=input("Re-enter ur password\n")
            if password==re_pass:
                break
            else:
                print("Passowrds didnt match,Try again...")

        progress=self.__save_userdetails_indatabase(user_number,password,self.name,self.location)
        if progress:
            print("Successfully created ur account.......................")
        else:
            print("Some error occured")

    


        

        
    def __generate(self):
        with open ("User.txt","r") as f:
            user_list_string=f.read().split("\n")
            user_list_number=list(map(int,user_list_string))
            

            
        while True:
            generated_num=random.randint(1000,9000)
            if not generated_num in user_list_number:
                break
        return generated_num
    
    def __save_userdetails_indatabase(self,user_number,password,name,location):
        #saving in username sys
        with open("User.txt","a")as f:
            f.write("\n"+str(user_number))

        #saving in user pass check system
        df=pd.read_csv("Password.csv")
        df_temp=pd.DataFrame([{
            "User_id":user_number,
            "Password":password

        }])
        df_final=pd.concat([df,df_temp])
        df_final.to_csv("Password.csv",index=False)

        #saving in every_user_server_data

        df_every_user=pd.read_csv("everyuser_data.csv")
        df_everytemp=pd.DataFrame([{
            "User_id":user_number,
            "Name":name,
            "Location":location,
            "Balance":100
        }])
        df_everyfinal=pd.concat([df_every_user,df_everytemp])
        df_everyfinal.to_csv("everyuser_data.csv",index=False)

        return True




            
        
        


#------------------------------------------------------------------------------------------------------------------


class verification:
    def check(self,username):
        return self.__username(username)
        
    def __username(self,username):
        with open("User.txt","r") as f:
            data=f.read().split("\n")
            if username in data:
                password=input("Enter your pass \n")
                
                return self.__password(username,password)
            else:
                return False
                
    def __password(self,username,password):
        #i made sure that these two terms:username and pass are always taken out as string.So, i converted the whole database(which omits the index)into string dtype. And explicitely again made index an string
        
        df=pd.read_csv("Password.csv",index_col="User_id",dtype=str)

        df.index=df.index.astype(str)
        
        if password ==df["Password"].loc[username]:
            print("pass done")
            return True
        else:
            print("smg went wrong")
            return False


class main_transaction_process:
    def __init__(self,username):
        #here i only typecasted to string for index, since thats the only thing im needing rn
        df=pd.read_csv("everyuser_data.csv",index_col="User_id")
        df.index=df.index.astype(str)
        df["Balance"] = df["Balance"].astype(int)


        
        self.balance=df["Balance"].loc[username]
        print("-----------------------------------------------\n")
        print(df.loc[username])
        
        deb_cred_choice=input("To deposit, type D or d, or To withdraw ,type W or w\n")

        if deb_cred_choice=='W' or deb_cred_choice=='w':
            purpose=input("Whts the purpose of withdrawal\n")
            amount=int(input("How much would u like to withdraw\n"))
            if self.__debit(amount,username,purpose):
                pass
            else:
                print("Insufficicent balance")
        elif deb_cred_choice=='D' or deb_cred_choice=='d':
            purpose=input("Whts the source of income\n")
            amount=int(input("How much would u like to deposit\n"))
            if self.__credit(amount,username,purpose):
                pass
            else:
                print("Error occured")
            
             

    def __debit(self,amount,username,purpose): #withdrawal
        type="Debit"
        previous_balance=self.balance
        statement=str(amount)+" "+"has been withdrawn for"+" "+purpose+" "+"purpose"
        
        if self.balance-amount < 0:
            return False
        
        
        
        
        self.balance-=amount
        print("Succsssfully withdrawn",amount,"\n")
        print("Now ur new balance is",self.balance)

        print("Making a recipt")
        now=datetime.now()
        date=now.date()
        time=now.time()
        print("------------------------------------------------------------")
        if self.__recipt(username,amount,type,previous_balance,statement,date,time):
            return True
        else:
            return False


    def __credit(self,amount,username,purpose):  #deposited
        type="Credit"
        previous_balance=self.balance
        statement=purpose+" "+"of"+" "+str(amount)+" "+"has been deposited"  
        
        self.balance+=amount
        print("Succsssfully deposited",amount,"\n")
        print("Now ur new balance is",self.balance)

        print("Making a recipt.........................")
        print("\n")
        print("Final_Recipt")
        now=datetime.now()
        date=now.date()
        time=now.time()
        
        if self.__recipt(username,amount,type,previous_balance,statement,date,time):
            return True
        else:
            return False


    def __recipt(self,username,amount,type,previous_balance,statement,date,time):
        #update everyuser_data.csv
        update_df=pd.read_csv("everyuser_data.csv",index_col="User_id")
        update_df.index=update_df.index.astype(str)
        update_df.loc[username,["Balance"]]=self.balance
        update_df.to_csv("everyuser_data.csv")


        df=pd.read_csv("Recipt.csv",index_col="Recipt_Number")
        while True:
            recipt_number=random.randint(100000,200000)
            if not recipt_number in df.index:
                break
        if type=="Debit":
            temp_df=pd.DataFrame([{
            "User_id":username,
            "Recipt_statement":statement,
            "Debit_Amt":amount,
            "Credit_Amt":0,
            "Previous_Balance":previous_balance,
            "Final_Balance":self.balance,
            "Date":date,
            "Time":time
        }],index=[recipt_number])
        elif type=="Credit":
            temp_df=pd.DataFrame([{
            "User_id":username,
            "Recipt_statement":statement,
            "Credit_Amt":amount,
            "Debit_Amt":0,
            "Previous_Balance":previous_balance,
            "Final_Balance":self.balance,
            "Date":date,
            "Time":time
        }],index=[recipt_number])

        final_df=pd.concat([df,temp_df])

        print("-----------------------------------------------------------------------------------------------------")
        print(final_df)
        print("-----------------------------------------------------------------------------------------------------")
        final_df.index.name="Recipt_Number"
        final_df.to_csv("Recipt.csv",index=True)

        return True
        
        

#-------------------------------------------------------------------------------------------------------------------------------------------
            






while True:
    opt=input("Welcome to the demo bank enterprise\nCurrently,You have 3 options\n1)If ur new , You can create a bank account.For this operation,type C or c\n2)If u already have an account, U can press.For this operation,type A or a\n3)You can end this program.For this operation,type Z or z\n")
    if opt=='C' or opt=='c':
        choice=input("Guidelines:1)U need to make an initial deposit of 100 dollars to create an ac.And monthly maintain a transaction of atleast 10 dollars\nType Y or y if u accept this stipulate or Type N or n to cancel this process\n")
        if choice=='Y' or choice=='y':
            create_acc()
        elif choice=='N' or choice=='n':
            pass
        else:
            pass

        
    elif opt=='A' or opt=='a':
        username=input("Enter ur username\n")

        s1=verification()
        check_in_id=s1.check(username)
        if check_in_id:
            print("Access successful")
            account_runner=main_transaction_process(username)
            break

        elif not check_in_id:
            pass
        else:
            pass


    elif opt=='Z' or opt=='z':
        break
    else:
        print("Sorry, You might have entered wrong choice")
        pass
sys.exit()





             


