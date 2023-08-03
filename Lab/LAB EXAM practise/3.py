name=input('enter user name')
newpassword=input('enter password')

def valid(name,newpassword):
    if len(newpassword)<8:
        return False
    count=0
    for chr in newpassword:
        if chr.isupper():
            count+=1
    if count<2:
        return False
    if not newpassword.isalnum():
        return False
    special=['$','%','^','$','*','#','@','!']
    count=0
    for i in special:
        if i in newpassword:
            count+=1
    if count<1:
        return False
    if newpassword.startswith(name):
        return False
    return True

print(valid(name,newpassword))
