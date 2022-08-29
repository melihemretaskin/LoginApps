import colorsys
import concurrent.futures
import string
import socket
import getpass
import datetime
import colors


platformName = "Scoca"
print(colors.color.BOLD + colors.color.CYAN +"Welcome to {}".format(platformName))
firstName = input(colors.color.YELLOW + colors.color.BOLD +"Please enter a Firstname: ")
lastName = input(colors.color.YELLOW + colors.color.BOLD +"Please enter a Lastname: ")
defaultPassword = 1234
print(colors.color.PROPE + colors.color.RED +"Default PASSWORD is 1234 ")

dp = input(colors.color.YELLOW + colors.color.BOLD +"Enter default password: ")
while True:
 if(int(dp) == int(defaultPassword)):
    print(colors.color.PINK + colors.color.BOLD + "Hi,{}".format(firstName).upper())
    np = input(colors.color.YELLOW + colors.color.BOLD +"Please enter a new password: ") #np = NewPassword

    if( 999 < int(np) < 10000):
        print(colors.color.BOLD + colors.color.GREEN + "New Password is >>> {}".format(np))
        uAge = input(colors.color.YELLOW + colors.color.BOLD +"Please enter your age: ")
        print(colors.color.RED +"\nPhone Number Format Sample 5320000010  10 numbers ")
        uPN = input(colors.color.YELLOW + colors.color.BOLD +"Please enter your phone number: ")
        if(999999999 < int(uPN) < 10000000000):
             print(colors.color.GREEN +"Your phone number {}".format(int(uPN)))
             username = input("Enter a nickname: ")
             bdd = input("Enter your birthday (only day): ")
             bdm = input("Enter your birthday (only month): ")
             bdy = input("Enter your birthday (only year): ")
             print("Your Birthday : {}/{}/{}".format(bdd,bdm,bdy))
             def getProfile() :
                 print("Name >>> {}".format(firstName),end=" ")
                 print("{}".format(lastName))
                 print("Username >>> {}".format(username))
                 print("Password >>> {}".format(np))
                 print("Age >>> {}".format(uAge))
                 print("Birthday >>> {}/{}/{}".format(bdd, bdm, bdy))
                 print("Phone Number >>> +90{}".format(uPN))
                 dt = datetime.datetime.now()
                 print("User created : {} ".format(dt))

             male = "male"
             female = "female"
             print("If you male = 1 , If you female = 2")
             secim = input("Please choose gender: ")
             if(int(secim) == 1):
                 print(colors.color.BOLD + colors.color.BLUE+"Gender : {}".format(male))
             elif(int(secim) == 2):
                 print(colors.color.BOLD + colors.color.PINK+"Gender : {}".format(female))



             getProfile()
             break


        else:
            print(colors.color.RED +"Phone Number Format : [ 5320000010 ]  Only 10 numbers ")




    else:
        print("Password format is >>> ____ example: 1001 [Only numbers and numbers limit 4] ")
    continue

 elif(int(dp) != int(defaultPassword)):
        print(colors.color.RED +"Wrong Password or Format ! Default Password is 1234")
        print(colors.color.RED +"\n Start Again")
        break




