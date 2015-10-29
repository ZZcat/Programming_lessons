#!/usr/bin/python

from math import sqrt #Import sqrt from math
a = input("What is the first leg? ") #Here we use input as to define a as a int
b = input("What is the second leg? ") #Same as in line 4

print "   _______________" #Here I print a underline to make a squareroot symble
print "\_|",a,"x",a,"+",b,"x",b

print "   _______________"
print "\_|",a*a,"+",b*b

print "   _______________"
print "\_|",(a*a)+(b*b),"\n" #the \n makes it go to the next line

print sqrt(a*a+(b*b))
