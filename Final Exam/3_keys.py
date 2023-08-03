# The third one is to sort a dictionary thats
# has a key=country name , and value=population percent
# I guess anyway u will sort it from the highest to the lowest n
# return them n a table form by using a 2d list

x = {"Doha": 78, "Islamabad": 34, "Karachi": 43}

for i in sorted(x):  # by keys, sorted(dict) will create list of keys
    print(i, x[i])

# sort by values sorted(dict, key=dict.get, reversr=False/True)
for w in sorted(x, key=x.get, reverse=False):
    print(w, x[w])
