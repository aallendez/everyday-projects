import os
import random
import numpy as np
import string

def main():
    os.system("clear")
    loop_flag = False
    
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "!@#$%&*-+=<>?"
    
    #Handles possible input errors
    while loop_flag == False:
        try:
            num_number = int(input("\nHow many numbers -> "))
            loop_flag = True
        except ValueError:
            print("\nInvalid input. Please enter an integer.")
            loop_flag = False
    
    os.system("clear")  
    loop_flag = False
    
    #Handles possible input errors        
    while loop_flag == False:
        try:
            num_letters = int(input("\nHow many letters -> "))
            loop_flag = True
        except ValueError:
            print("\nInvalid input. Please enter an integer.")
            loop_flag = False
    
    os.system("clear")    
    loop_flag = False
    
    #Handles possible input errors
    while loop_flag == False:
        try:
            num_symbols = int(input("\nHow many symbols -> "))
            loop_flag = True
        except ValueError:
            print("\nInvalid input. Please enter an integer.")
            loop_flag = False
    
    os.system("clear")
    password = get_password(num_number, num_letters, num_symbols, letters, numbers, symbols)
    
    print("\n\nYour password is: ", password, "\n\n\n")
    
def get_password(num_number, num_letters, num_symbols, letters, numbers, symbols):
    final_password = []
    
    #Generate random letters for password
    for _ in range(num_letters):
        char = random.choice(letters)
        final_password.append(char)
    
    #Generate random numbers for password
    for _ in range(num_number):
        num = random.choice(numbers)
        final_password.append(num)
    
    #Generate random symbols for password   
    for _ in range (num_symbols):
        sym = random.choice(symbols)
        final_password.append(sym)
        
    #Shuffles the content of the password
    random.shuffle(final_password)
    
    #Joins all values of the list into one string
    return "".join(final_password)
    

if __name__ == "__main__":
    main()
