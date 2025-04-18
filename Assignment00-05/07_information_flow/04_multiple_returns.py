def get_user_info():
    fname = input("Enter Your First Name : ")
    lname = input("Enter Your Last Name : ")
    email = input("Enter Your Email Address : ")
    return fname,lname,email

def main():
    user_data = get_user_info()
    print("Recieved User Information as : ",user_data)

if __name__ == "__main__":
    main()    