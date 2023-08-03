#• Write a function that receives a dictionary contains employees’
#names and their salaries. The function will remove all
#employees whose salaries greater than 6000. Call the function.


def remove(dict):
    finaldict={}
    for i in dict:
        if dict[i]<6000:
            finaldict[i]=dict[i]
    return finaldict

employees={'Ahmed':5000,'Naser':7800,'Sara':6500}
print(remove(employees))


myfile = open("data.txt", 'r')
data_dict = {}
for line in myfile:
    k, v = line.strip().split('=')
    data_dict[k.strip()] = v.strip()
 
myfile.close()
 
print(' text file to dictionary =\n ',data_dict)