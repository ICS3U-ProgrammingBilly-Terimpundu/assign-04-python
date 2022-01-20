#!/usr/bin/env python3

# Created by:  Billy Terimpundu
# Created on: January 2022
# This program  that asks the user for two numbers
# then calculates and displays the Lowest Common Multiple of the two numbers
# Python Program to Find the LCM using if..else statement and while Loop

def compute_LCM(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

# To Take Input from the User
num1 = int(input("Enter the First Number: "))
num2 = int(input("Enter the Second Number: "))

print("The L.C.M. of {0} and {1} is {2}".format(num1, num2, compute_LCM(num1, num2)))