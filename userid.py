class User:
    full_name = ""
    email = ""
    __password = ""
    mobile_number = ""
    def __init__(self,name,email,password):
        self.full_name = name
        self.email = email
        self.__password = password
    def update_name(self,new_name):
        self.full_name = new_name
    def get_name(self):
        return self.full_name
    """setter method for private variable password"""
    def update_password(self,new_password):
        self.__password = new_password
    def update_new_mobile_number(self,new_number):
        self.mobile_number = new_number
    """ getter method  for accessing number"""
    def get_user_password(self):
        return self.__password

