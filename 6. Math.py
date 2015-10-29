from math import sqrt #Here we are inporting a python modules

a = input("Number 1: ")
b = input("Number 2: ")
c = a + b
d = a - b
e = a * b
print str(a) + " + " + str(b) + " = " + str(c) #Here is one way to write stuff
                                               #You may note I use str() that
                                               #Defines 

print a , "-" , b , "=" , d # Here I use "," instead of "+"
print a,"X ",b,"=",e # You can use spaces or not either way works
print a,"/",b,"=",(a/b) # Now a do the math within print
print "The square root of",a,"is",sqrt(a) #sqrt is square root
print "The square root of",b,"is",sqrt(b)

