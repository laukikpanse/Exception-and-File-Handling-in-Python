customerList = [3,1,4,2,6] #Ticketing Requirements

P = 2 #focused Customer

timer = 0 #created a Timer
print("The Given List is: "+str(customerList)) #Printing the given list
print("The Value of P is: "+str(customerList[P])+"\n")

print("Start of the calculations: ")


temp = int(customerList[0])

while(customerList[P] != 0 and customerList[P]<len(customerList)):

	print("The value of P is: "+str(customerList[P]))
	if(customerList[P])>0:
		if P <= 0:
			P = len(customerList)-1

		else:
			P = P - 1
	else:
		break

	temp = int(customerList[0]) #keep first customer in a temporary variable
	temp = temp-1 #Decrement the required ticket by 1 of the first customer
	customerList.pop(0) #pop the first customer from the list
	if(temp>0):
		customerList.append(temp) #append the decremented value to the end
		

	print(customerList)
timer = timer + 1 #incremeneted the Timer by 1

		


print("The total time needed is: "+str(timer) +" Seconds")