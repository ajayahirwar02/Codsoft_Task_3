import random

characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*_"

while True:
    
    pass_length=int(input("Enter the length of Required Password : "))
    pass_count=int(input("Enter the number of Required Password : "))

    for i in range(pass_count):
        password=""
        for j in range(pass_length):
            pass_char=random.choice(characters)
            password+=pass_char
        print("The Genereated Password is : ",password)

    repeat=input("Do you wnat to generate more password? ")
    if repeat=="no" or repeat=="No":
        break

