a=input("enter the name")
if a=="priti":
    print("yes it's your account")
    b=input("enter the email")
    if b=="priti@123":
        print("correct e-mail")
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