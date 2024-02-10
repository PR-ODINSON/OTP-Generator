import random
import string
lenght=int(input("Enter the lenght of the password: "))
def generate_password(length):
  special_characters="!@#$%&"
  password=''.join(random.choices(string.ascii_lowercase+string.digits+special_characters,k=lenght))
  print(password)

generate_password(lenght)