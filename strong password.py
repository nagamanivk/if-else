password=input("enter the no:")
if len (password)>=6:
    if "@"in  password or "#" in password:
        if password>="A"  or password<="Z":
            if password>="a" or password<="z":
                if password>="0" or password<="9":
                    print("strong password")
                else:
                    print("enter proper number")
            else:
                print("enter proper lower case")
        else:
            print("enter valid upper case")
    else:
        print("enter proper special character")
else:
    print("enter valid length")

# i=1
# while i<=10:
#     if i==6 or i==7 or i==8:
#         print("*")
#     else:
#         print(i)
#     i=i+1

    



        
        

    



    



