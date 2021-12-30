a=input("enter the name")
if a=="priti":
    print("yes,itis priti")
    b=input("enter the email")
    if b=="priti@123":
        print("carrect email")
        c=int(input("enter the password"))
        d=int(input("conform your password"))
        if c==d:
            print("log in")
        else:
            print("incorrect password")
    else:
        print("error")
else:
    print("incorrect id")



