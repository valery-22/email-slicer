def main():
    print ("Welcome to the email slice")
    print ("")

    email_input = input("Input your email address:")

    (username,domain) = email_input.split("@")
    (domain,extension) = domain.split(".")

    print("username:",username)
    print("Domain : ", domain)
    print("Extension:",extension)

while True:
    main()
