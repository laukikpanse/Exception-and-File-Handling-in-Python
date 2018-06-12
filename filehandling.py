#we will create a textfile naming demo.txt in the same folder

#writing something to the file
file = open("demo.txt", 'w')

file.write("Hello Sir how are you..!!")



#to access that file we will use a fileholder
file = open("demo.txt", 'r') #specify the filename and r denotes readfile

#pulling the content into a variable
content = file.read()
#print the contents onto the console
print(content)

