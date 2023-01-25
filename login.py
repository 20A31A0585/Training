from userid import User
class Login:
    __db = []
    def __init__(self):
        self.print_menu()
    def print_menu(self):
        print("Welcome User")
        print("1. Register")
        print("2.Logiin")
        print("3. Exit")
    def create_user(self,name,email,password):
        new_user=User(name,email,password)
        self.__db.append(new_user)
        print(self.__db)
    def validate_user(self,email,password):
            temp = self.__db.copy()
            for user_obj in temp:
                if email==user_obj.email:
                    if password==user_obj.get_user_password():
                        return "login successful"
                    else:
                        return 'login failed'
                return 'login failed'
obj=Login()
while(1):
    option = input("Enter your choice: ")
    if option =='1':
        name = input("Enter your full name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        res = obj.create_user(name,email,password)
        if res == True:
            print("Created Successfully")
    elif option=='2':
        email=input("enter email: ")
        password = input("enter password: ")
        res=obj.validate_user(email,password)
        print(res)
    elif option=='3':
        pass
    else:
        print('Invalid input')
            
