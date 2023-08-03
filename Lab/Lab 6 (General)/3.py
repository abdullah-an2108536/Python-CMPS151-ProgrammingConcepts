#Write a program to read scores of students in Math and English. The program
#should read two scores for each student. After the user enters scores of a student,
#the program should ask the user “More students? Y/N” so the program keeps
#reading more students until the user inputs ‘N’. Then, your program should
#   - print number of the students(how many of them) who passed in both subjects
#   (a student is passed in a subject if his grade greater than or equal 50).
#   - Print the minimum grade in each subject.
#   - Print the average grade in each subject.

min_math=101
min_english=101
total_math=0
total_english=0
students_passed=0

math_score=int(input('Enter score of a student in math ... '))
english_score=int(input('Enter score of a student in english ... '))
if math_score>=50 and english_score>=50:
    students_passed=students_passed+1
if math_score<min_math:
    min_math=math_score
if english_score<min_english:
    min_english=english_score
total_english=total_english+english_score
total_math=total_math+math_score
number_of_students=1

_continue=input('More students? Y/N')
while _continue=='Y' or _continue=='y':
    math_score=int(input('Enter score of a student in math ... '))
    english_score=int(input('Enter score of a student in english ... '))
    if math_score>=50 and english_score>=50:
        students_passed=students_passed+1
    if math_score<min_math:
        min_math=math_score
    if english_score<min_english:
        min_english=english_score
    total_english=total_english+english_score
    total_math=total_math+math_score
    number_of_students+=1
    _continue=input('More students? Y/N')


average_math=total_math/number_of_students
average_english=total_english/number_of_students

print(students_passed,'amount of students passed')
print(average_math,'was the average grade in math')
print(average_english,'was the average grade in english')
print(min_english,'was the lowest score in english')
print(min_math,'was the lowest score in math')


