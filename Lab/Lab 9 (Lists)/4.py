#Write a program that asks the user to enter a string, then output the
#following:
#a- Number of words.
#b- Number of characters.
#c- Number of digits.
#d- Number of capital letters.
s=input('Enter a string....')
words=s.split()
print('Number of words:',len(words))
count=0
for chr in s:
    if chr!=' ':
        count=count+1
print('count=',count)
