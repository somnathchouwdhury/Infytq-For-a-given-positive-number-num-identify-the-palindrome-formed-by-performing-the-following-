#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 20:19:25 2021

@author: samac
"""

"""
For a given positive number num, identify the palindrome formed 
by performing the following operations:-

    Add num and its reverse
    Check whether the sum is palindrome or not. 
    If not, add the sum and its reverse and repeat the process until a 
    palindrome is obtained
"""


#this will reverse the string
def Palindrome(n):
    rev=0
    while(n>0):
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    return rev


#function to check whether string is palindrome
def CheckIsPalindrome(n):
    return Palindrome(n)==n

#function to reverse and add
def ReverseAndAdd(n):
    rev=0
    
    #100000000 is just a random number so that our function can stop at some point nd conclude that it can't be carried out further
    while(n<1000000000):
        rev=Palindrome(n)
        n=n+rev
        if(CheckIsPalindrome(n)):
            print(n)
            break
        else:
            if(n>100000000000):
                print("No Palindrome exist")
    

ReverseAndAdd(int(input()))













