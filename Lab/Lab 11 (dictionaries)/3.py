# Write a program that opens a text file called “text1.text” (download from
# Blackboard) then displays a list of all the unique words found in the file.
# Hint: Store each word as an element of a set.

myfile = open("1.txt", "r")

contents = myfile.read()
list = contents.split()
myfile.close()

unique = set(list)
for word in unique:
    print(word)