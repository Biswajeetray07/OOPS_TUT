class  chatbook:
    __user_id = 0
    def __init__(self):
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        self.__name = "Default User" # encapsulated attribute
        self.username = ""
        self.password = ""
        self.loggedin = False
        # self.menu()

    @staticmethod
    def get_id():
        return chatbook.__user_id
    @staticmethod
    def set_id(value):
        chatbook.__user_id = value

        # Getter and Setter methods for encapsulated attribute
    def get_name(self):
        return self.__name
    
    def set_name(self, value):
        self.__name = value

    def menu(self):
        user_input = input("""Welcome to ChatBook! How would you like to proceed?  
                            1. Press 1 to SignUp " 
                            2. Press 2 to SignIn " 
                            3. Press 3 to write a post" 
                            4. Press 4 to message a friend" 
                            5. Press any other key to exit
                            
                            Your choice: """)  
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            self.write_post()
        elif user_input == '4':
            self.message_friend()
        else:
            exit()

    def signup(self):
        email = input("Enter your email: ")
        password = input("setup your password: ")
        self.username = email
        self.password = password
        print("Signup Successful!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == "" and self.password == "":
            print("No user found! Please sign up first.")
            self.menu()
        else:
            uname = input("Enter your email/username: ")
            pwd = input("Enter your password: ")
            if self.username == uname and self.password == pwd:
                print("Login Successful!")
                self.loggedin = True
            else:
                print("Invalid credentials! Please try again.")
                self.menu()
        print("\n")
        self.menu()

    def write_post(self):
        if self.loggedin:
            post_content = input("Write your post here: ")
            print(f"Post published: {post_content}")
        else:
            print("Please sign in to write a post.")
        print("\n")
        self.menu()

    def message_friend(self):
        if self.loggedin:
            friend_username = input("Enter your friend's username: ")
            message_content = input("Enter your message: ")
            print(f"Message sent to {friend_username}: {message_content}")
        else:
            print("Please sign in to message a friend.")
        print("\n")
        self.menu()
obj = chatbook()