englishscore=int(input('enter english score'))
mathscore=int(input('enter math score'))
max=englishscore
mathsum=mathscore
for i in range(9):
    englishscore=int(input('enter english score'))
    mathscore=int(input('enter math score'))
    if englishscore>max:
        max=englishscore
    mathsum=mathscore+mathsum
print('sum = ',mathsum)
print('max',max)