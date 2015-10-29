# Try and run this:
a = "4"
b = 4 + a
print b
## You will find that it gives a err like:
## "TypeError: unsupported operand type(s) for +: 'int' and 'str'"
## This means that is thinks a is a variable and you can't add a int and str
## Note: int means interger and str means strings

## Now how can we fix this?
## There are two ways to do this we could change a = "4" to a = 4 or
## b = 4 + a to b = 4 + int(a)
## We are going to change "b = 4 + a" to "b = 4 + int(a)"
