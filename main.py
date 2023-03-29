import string
import random


class Password_Generator:

    history = ['ù']


    def __init__(self) -> None:
        self.password = "None"
        self.prev = ''
        self.next = ''

    def generate_password(self, length):
       if length >= 12:
           liste_for_random = string.ascii_letters + string.digits + string.punctuation
           password =  ''.join(random.choice(liste_for_random) for i in range(length))
           self.history.append('**')
           return password
       
       else:
           raise Exception('La taille est minimum 12')
       

 

    
    
    def history(self):
        pass


    def prev(self):
        pass

    def next(self):
        pass


"""
password_genarator = Password_Generator()
my_password = password_genarator.generate_password(12)
print(my_password)
print(password_genarator.history)
# print(my_password.password)
"""
    

class Dusal:
    first = ['1', '2']

    def __init__(self) -> None:
        pass


    @classmethod
    def change(self, new):
        self.first=new
        


one = Dusal()
two = Dusal()

print(Dusal.first)
one.change(['1', '2', '3'])
print(one.first)
print(two.first)