#Write a function that receives a dictionary contains employees’
#names and their salaries. The function will remove all
#employees whose salaries greater than 6000. Call the function. 

def salary(dic):
    keys=[]
    for i in dic:
        keys.append(i)
    for i in keys:
        if dic[i]>6000:
            del dic[i]
    return dic


def main():
    employees={'Ahmed':5000,'Naser':7800,'Sara':6500}
    print(salary(employees))

main()

