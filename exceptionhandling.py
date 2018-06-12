#exception handling in Python

#Define a function for an example to divide two numbers

def sum(a,b):
	print(a//b)


#this is try block which will attempt to run the function
try:
	sum(20,0)

#If Zero division error is found following block will be executed
except ZeroDivisionError:
	print("Ooops..there is a ZeroDivisionError")


#Finally Block: No Matter what this section will execute
finally:
	print("I will print anyhow...!!!")