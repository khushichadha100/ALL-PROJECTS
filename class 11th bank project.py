username=['khushi','shourya','arav']
password=["1212","3434","5656"]
balance=[1000000,80000,17000]
print("****HELLO!!! & WELCOME TO KHUSHI INTERNATIONAL BANK****")
print("*******************")
print("CHOOSE YOUR SERVICE")
print("*******************")
print(" TO CREATE ACCOUNT_____________(C)")
print(" TO CHECK BALANCE______________(B)") 
print(" TO WITHDRAW MONEY_____________(W)")
print(" TO DEPOSIT MONEY______________(D)")
print(" TO CHANGE YOUR PASSWORD_______(p)")
print(" TO TAKE AN EXIT_______________(E)")
service=input("ENTER YOUR SERVICE KEY: C/B/W/D/P/E:")
service=service.lower()
if service == 'c':
 name=input("-----ENTER YOUR NAME-----:")
 name=name.lower()
 print("HELLO",name,"!!!!!!")
 print("*******************")
 print("!!CONGRATULATIONS!!")
 print("*******************")
 print("YOUR ACCOUNT HAS BEEN CREATED")
 
 print("*****************************")
 username.append(name);
 print(username,"------->CHANGES HAS BEEN DONE!!!!")
 
 print("*******************************************")
 print("YOUR PASSWORD IS:------->2020")
 password.append(2020);
 print(password,"------->CHANGES HAS EEN DONE!!!!") 
 print("****KINDLY REMEMBER THIS PASSWORD AND DO NOT SHARE IT WITH OTHERS****")
 print()
elif service == 'b':
 name=input("-----ENTER YOUR NAME-----:")
 name=name.lower()
 if name==username[0]:
  print("YOUR BALANACE IS RS.",balance[0])
 elif name==username[1]:
  print("YOUR BALANCE IS RS.",balance[1])
 elif name==username[2]:
  print("YOUR BALANCE IS RS.",balance[2])
 else:
     print("****************")
     print("INVALID USERNAME") 
     print("****************")
 
elif service == 'w':
 name=input("-----ENTER YOUR NAME-----: ")
 name=name.lower()
 if name==username[0]:
  print("YOUR BALANACE IS RS.",balance[0])
  print("***********************************************")
  amount=int(input("ENTER AMOUNT YOU WANT TO WITHDRAW: "))
  print("************************************************")
  if amount > balance[0]:
   print("INSUFFEICIENT BALANCE")
   print("*********************")
  else:
     balance[0]=balance[0] - amount
     print("AFTER WITHDRAWING YOUR NEW BALANCE IS",balance[0])
     print("************************************************")
 
 elif name==username[1]:
    print("YOUR BALANACE IS RS.",balance[1])
    print("***********************************************")
    amount=int(input("ENTER AMOUNT YOU WANT TO WITHDRAW: "))
    print("************************************************")
    if amount > balance[0]:
      print("INSUFFEICIENT BALANCE")
      print("*********************")
    else:
         balance[1]=balance[1] - amount
         print("AFTER WITHDRAWING YOUR NEW BALANCE IS",balance[1])
         print("************************************************")
 else:
       print("YOUR BALANACE IS RS.",balance[2])
       print("***********************************************")
       amount=int(input("ENTER AMOUNT YOU WANT TO WITHDRAW: "))
       print("************************************************")
       balance[2]=balance[2] - amount
       print("AFTER WITHDRAWING YOUR NEW BALANCE IS",balance[2])
       print("************************************************")
elif service == 'd':
 name=input("-----ENTER YOUR NAME-----: ")
 name=name.lower()
 if name==username[0]:
  print("*********************************************")
  print("YOUR CURRENT BALANCE IS RS.",balance[0])
  print("*********************************************")
  amount=int(input("ENTER AMOUNT YOU WANT TO DEPOSIT: "))
  balance[0]=balance[0] + amount
  print("AFTER DEPOSTION YOUR NEW BALANCE IS RS.",balance[0])
  print("***************************************************")
  print(balance[0],"-------->CHANGES HAS BEEN MADE")
  print("***************************************************")
 elif name==username[1]:
  print("*********************************************")
  print("YOUR CURRENT BALANCE IS RS.",balance[1])
  print("*********************************************")
  amount=int(input("ENTER AMOUNT YOU WANT TO DEPOSIT: "))
  balance[1]=balance[1] + amount
  print("AFTER DEPOSTION YOUR NEW BALANCE IS RS.",balance[1])
  print("***************************************************")
  print(balance[1],"-------->CHANGES HAS BEEN MADE")
  print("***************************************************")
 else:
     print("*********************************************")
     print("YOUR CURRENT BALANCE IS RS.",balance[2])
     print("*********************************************")
     amount=int(input("ENTER AMOUNT YOU WANT TO DEPOSIT: "))
     balance[2]=balance[2] + amount
     print("AFTER DEPOSTION YOUR NEW BALANCE IS RS.",balance[2])
     print("***************************************************")
     print(balance[2],"-------->CHANGES HAS BEEN MADE")
     print("***************************************************")
elif service == 'p':
 name=input("ENTER YOUR NAME: ")
 name=name.lower()
 if name==username[0]:
  print("CONDITIONS FOR PASSWORD CHANGING MUST BE FULLFILLED:--->GIVEN BELLOW:")
  print("*******************************************************")
  print("1.SHOULD BE INT")
  print("*******************************************************")
  print("2.CONSIST OF 4 DIGITS")
  print("*******************************************************")
  print("3.DOES NOT MATCH WITH PREVIOUS ONE")
  print("*******************************************************")
  new_password = str(input("ENTER NEW PASSWORD: "))
  if new_password.isdigit() and new_password != password[0] and len(new_password)==4:
     print("RE-ENTER NEW PASSWORD FOR CONFIRMATION: ")
     print("*****************************************************")
     new_pd = str(input("RE-ENTER NEW PASSWORD FOR CONFIRMATION: "))
     print("*****************************************************")
     if new_password==new_pd:
        password[0]=new_pd;
        print("***************************************")
        print(password[0],"-------->CHANGES HAS BEEN MADE")
        print("***************************************")
        print("NEW PASSWORD SAVED")
        print("***************************************")
     else: 
      print("*************************")
      print("WRONG PASSWORD")
      print("*************************")
  else:
     print("****************")
     print("CONDITION FOR PIN CHANGING UN FULLFILLED")
 
 elif name==username[1]:
      print("CONDITIONS FOR PIN MUST BE FULLFILLED:--->GIVEN BELLOW:")
      print("*******************************************************")
      print("1.SHOULD BE INT")
      print("*******************************************************")
      print("2.CONSIST OF 4 DIGITS")
      print("*******************************************************")
      print("3.DOES NOT MATCH WITH PREVIOUS ONE")
      print("*******************************************************")
      new_password = str(input("ENTER NEW PASSWORD: "))
      if new_password.isdigit() and new_password != password[1] and len(new_password)==4:
          print("RE-ENTER NEW PASSWORD FOR CONFIRMATION: ")
          print("*****************************************************")
          new_pd = str(input("RE-ENTER NEW PASSWORD FOR CONFIRMATION: "))
          print("*****************************************************")
          if new_password==new_pd:
             password[1]=new_pd;
             print("***************************************")
             print(password[1],"-------->CHANGES HAS BEEN MADE")
             print("***************************************")
             print("NEW PASSWORD SAVED")
             print("***************************************")
          else: 
 
           print("*************************")
           print("WRONG PASSWORD")
           print("*************************")
      else:
          print("****************")
          print("CONDITION FOR PIN CHANGING UN FULLFILLED")
 
 else:
     print("CONDITIONS FOR PASSWORD CHANGING MUST BE FULLFILLED:--->GIVEN BELLOW:")
     print("*******************************************************")
     print("1.SHOULD BE INT")
     print("*******************************************************")
     print("2.CONSIST OF 4 DIGITS")
     print("*******************************************************")
     print("3.DOES NOT MATCH WITH PREVIOUS ONE")
     print("*******************************************************")
     new_password = str(input("ENTER NEW PASSWORD: "))
     if new_password.isdigit() and new_password != password[2] and len(new_password)==4:
      print("RE-ENTER NEW PASSWORD FOR CONFIRMATION: ")
      print("*****************************************************")
      new_pd = str(input("RE-ENTER NEW PASSWORD FOR CONFIRMATION: "))
      print("*****************************************************")
      if new_password==new_pd:
          password[2]=new_pd;
          print("***************************************")
          print(password[2],"-------->CHANGES HAS BEEN MADE")
          print("***************************************")
          print("NEW PASSWORD SAVED")
          print("***************************************")
      else: 
         print("***************************************")
         print("WRONG PASSWORD")
         print("*************************")
     else:
         print("****************")
         print("CONDITION FOR PIN CHANGING UN FULLFILLED")
elif service == 'e':
 '''
 print("I REALLY ENJOYED WORKING IN THIS PROJECT ")
 print("THANK YOU MAAM FOR TEACHING SO WELL THAT I WAS ABLE TO DO THIS OWN MY OWN AND WITHIN 2-3 DAYS!!")
 print("THANKU YOU AND LOVE YOU MAAM")
 '''
 print("HAVE A NICE DAY !!!")
 print("VISIT AGAIN !!!!")
 
else:
 print("***************")
 print("INVALID SERVICE")
 print("***************")