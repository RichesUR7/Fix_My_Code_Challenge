#!/usr/bin/python3
""" 
User class
"""

class User():
    """ Documentation """

    __email = None

    def _init_(self):
        """ Documentation """
        self.__email = None

    @property
    def email(self):
        """ Documentation """
        return self.__email
    
    @email.setter
    def email(self, value):
        """ Documentation """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value

    
   
    
if _name_ == "_main_":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
