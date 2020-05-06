# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 21:10:51 2019

File outputs user defined amount of prime numbers into user defined columns

@author: Zac
"""

def display(numPrimes, numCols):
    counter = 0
    x = 0
    while counter != numPrimes:
        if isPrime(x) == True:
            print('%i ' %(x), end="") # end makes it that it isnt printed on a new line
            if(counter % numCols == numCols - 1):
                print('') # makes new row
            counter += 1
        x += 1
    
    
    
def isPrime(number):
    x = 3
    if number == 2:
        return True
    if number < 2:
        return False
    if number % 2 == 0:
        return False
    
    while x < number/2:
        if number % x == 0:
            return False
        x += 1
        
    return True

def main():
    userNums = int(input("How many prime numbers would you like to find?: "))
    while userNums < 1:
        userNums = input("Please enter a number greater than 0: ")
    
    userCols = int(input("How many columns should they be outputted in?: "))
    while userCols < 1:
        userCols = input("Please enter a number greater than 0")

    display(userNums, userCols)

if __name__ == '__main__':
    main()