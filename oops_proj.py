class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to Chatbook !! how would you like to proceed?
                           1. Press 1 to signup 
                           2. Press 2 to signin 
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit
                            -> """)
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.send_message()
        else:
            exit

    def signup(self):
        email = input("Enter your email here --> ")
        pwd = input("Setup your password here --> ")
        self.username = email
        self.password = pwd
        print("You have signed up successfully")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print('Please signup first')
        else:
            uname = input("Enter your username here --> ")
            pwd1 = input("Enter your password here --> ")
            if self.username == uname and self.password == pwd1:
                print("You have signed in successfully")
                self.loggedin = True
            else:
                print("Please Enter correct credentials")
        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedin == True:
            txt = input("Enter your message here -> ")
            print(f"Following content has been posted -> {txt}")
        else:
            print("You need to sign in to post")
        
        print("\n")
        self.menu()

    def send_message(self):
        if self.loggedin == True:
            txt = input("Enter your message here -> ")
            frnd = input("Whom to send this message? -> ")
            print(f"Your message have been sent to {frnd}")
        else:
            print("you need to sign in first to send message")

        print("\n")
        self.menu()



# user1 = chatbook()