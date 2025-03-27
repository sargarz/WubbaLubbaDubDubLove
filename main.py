
#getter method
#setter method
# 1 class
# 1 method


class User():

    def __init__(self, password, username):
        self.__password = password
        self.username = username


    #getter method for accesing encapsulated password
    @property
    def password(self):
        return self.__password

    #setter method for instances where the user wants to change the password
    @password.setter
    def password(self, new_password):
        self.__password = new_password





