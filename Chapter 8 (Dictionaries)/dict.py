#format
phonebook = {'Chris':'5551111', 'Katie':'5552222','Joanne':'5553333'}
print(phonebook['Joanne'])

# can use in using key
if 'Kathryn' in phonebook:
    print('Found')
else:
    print('Not found')

#len works
print(len(phonebook))

#to add a new key-value pair:
#dictionary[key] = value

#del dictionary[key]

#sorted=sorted(dictionary name, keys=string.lower) create sorted list of keys

#for i in grades: will print keys
#print(i)

#Format: dictionary.clear()

#Format: dictionary.get(key, default)
#•default is returned if key is not found



#pop method: returns value associated with specified key and
#removes that key-value pair from the dictionary
#• Format: dictionary.pop(key, default)
#• default is returned if key is not found

#popitem method: returns a randomly selected key-value pair
#and removes that key-value pair from the dictionary
#• Format: dictionary.popitem()


#sets

#Union of two sets: a set that contains all the elements of both sets
#•To find the union of two sets:
#Use the union method
#•Format: set1.union(set2)

#•Intersection of two sets: a set that contains only the elements found in
#both sets
#•To find the intersection of two sets:
#Use the intersection method
#•Format: set1.intersection(set2)

##•Difference of two sets: a set that contains the elements that
#appear in the first set but do not appear in the second set
#•To find the difference of two sets:
#Use the difference method
#•Format: set1.difference(set2)

#To find the symmetric difference of two sets:
#Use the symmetric_difference method
#•Format: set1.symmetric_difference(set2)

#Set A is subset of set B if all the elements in set A are
#included in set B
#• To determine whether set A is subset of set B
#• Use the issubset method
#• Format: setA.issubset(setB)

#Set A is superset of set B if it contains all the elements of
#set B
#• To determine whether set A is superset of set B
#• Use the issuperset method
#• Format: setA.issuperset(setB)