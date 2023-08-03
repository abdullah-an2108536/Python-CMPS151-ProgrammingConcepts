
# CMPS 151 Home Work 2

import os


def main():  # main function
    outfile = open("attendance.csv", "w")  # created attendance.csv file
    outfile.write("Name,course,section,absence,status\n")
    outfile.close()
    coursesfolder = "/Users/abdullah/Desktop/PROGRAMMING CONCEPTS/HW2/courses"  # location of coursesfolder on my computer
    filenames = os.listdir(coursesfolder)
    filenames.remove(".DS_Store")
    # removed '.DS_Store file' which was showing up in this folder on my mac os (was the first item in this list and wasn't visible in finder(files)).
    #  On windows, maybe this line is not needed, but won't interfere with the program
    filenames.reverse()  # reversed so that the order is the same as the answer sheet provided.
    for filename in filenames:
        sections_in_file = os.listdir(os.path.join(coursesfolder, filename))
        sections_in_file.remove(".DS_Store")
        sections_in_file.reverse()  # reversed so that the order is the same as the answer sheet provided
        for section in sections_in_file:
            sectionpath = os.path.join(coursesfolder, filename, section)
            sectionpath_list = sectionpath.split("/")  # make a list of the path
            course = sectionpath_list[7]  # used indexes to get course name and section
            section_name = sectionpath_list[8]
            write_record(sectionpath, course, section_name)


# Function takes a name and lecture attendance sheet
# returns total of time (in minutes)  attended
def timeattended_session(name, file):
    infile = open(file, "r")
    line = infile.readline()
    found = False
    while line != "":  # keep reading until no more lines
        line = line.rstrip("\n")  # remove \n
        info = line.split(",")  # make a list
        if info[1] == name:  # use index of the list to compare
            found = True
            time_str = info[6]
            time_integer = time_str.split(":")  # convert to minutes
            minutes = (
                (int(time_integer[0]) * 60)
                + int(time_integer[1])
                + (int(time_integer[2]) / 60)
            )
            return minutes  # return in minutes
        line = infile.readline()
    infile.close()
    if not found:  # absent if name not in this session
        return 0


# Function that will take a name and path for a section
# It will return the student's absence in that section in all sessions in that folder
def absence_section(name, section, duration):
    filenames = os.listdir(section)
    absence = 0
    for filename in filenames:
        if "Lecture" in filename:  # ignore classinfo and classlist files
            timeattended = timeattended_session(name, os.path.join(section, filename))
            if timeattended < (
                0.75 * duration
            ):  # absent if less than 75% of class duration
                absence = absence + 1
    return absence


# Function that will read data from classinfo and classlist.
# For every name, it will write a record
def write_record(section, course, section_name):
    filenames = os.listdir(section)
    for filename in filenames:
        if "classInfo.csv" in filename:
            infile = open(os.path.join(section, filename), "r")
            line1 = infile.readline()  # dont need line 1 - it is the header
            line2 = infile.readline().rstrip()
            contents = line2.split(",")  # make a list from line 2
            duration = int(contents[0])  # use indexes to get duration and sessions
            number_of_sessions = int(contents[1])
            infile.close()
    for filename in filenames:
        if "classList.csv" in filename:
            infile = open(os.path.join(section, filename), "r")
            names = infile.readlines()  # makes a list
            names = [x[:-1] for x in names]  # remove \n
            names = names[1:]  # remove 'username'
            infile.close()
            for name in names:
                absences = absence_section(name, section, duration)
                absence_percentage = absences / number_of_sessions
                if absence_percentage >= 0.25:  # status desicions
                    status = "Dismissed"
                elif absence_percentage < 0.25 and absence_percentage > 0.15:
                    status = "Warning"
                else:
                    status = "Ok"
                outfile = open("attendance.csv", "a")
                writing = (
                    name
                    + ","
                    + course
                    + ","
                    + section_name
                    + ","
                    + str(absences)
                    + ","
                    + str(status)
                    + "\n"
                )
                outfile.write(writing)
                outfile.close()


main()