#we will create a textfile naming demo.txt in the same folder

#writing something to the file
file = open("demo.txt", 'w')

file.write("Hello Sir how are you..!!")

#now to add new lines we cannot use 'w' instead use append mode 'a'
file = open("demo.txt", 'a')

file.write("\nThis is the second line")

#to access that file we will use a fileholder
file = open("demo.txt", 'r') #specify the filename and r denotes readfile

#pulling the content into a variable
content = file.read()
#print the contents onto the console
print(content)

#always remember to close the file
file.close()
