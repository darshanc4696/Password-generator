import random
from src.pass_gen import password_generator

if __name__=="__main__":
    min_length = int(input('Enter the minimum length of the password you want:'))
    number = input("Do you want number in the password (y/n)?").lower() == 'y'
    special_char = input("Do you need the special character in password (y/n)?").lower() == 'y'
    generated_password = password_generator(min_length=min_length, number=number, special_char=special_char)
    print(generated_password)




