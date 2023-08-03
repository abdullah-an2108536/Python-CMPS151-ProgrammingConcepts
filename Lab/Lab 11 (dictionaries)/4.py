myfile = open("file1.txt", "r")
file1 = myfile.read()
myfile.close()
set1 = set(file1.split())

myfile = open("file2.txt", "r")
file2 = myfile.read()
myfile.close()
set2 = set(file2.split())

# unique 
unique = set1.union(set2)
print(unique)

# intersection 
intersection = set1.intersection(set2)
print(intersection)

# appear in the first file but not the second 
x = set1.difference(set2)
print(x)

# appear in the second file but not the first --
y = set2.difference(set1)
print(y)

# words that appear in either the first or second --
z = set1.symmetric_difference(set2)
print(z)
