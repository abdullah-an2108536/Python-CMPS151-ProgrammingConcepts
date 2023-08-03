def remove_newline(list):  # function takes in list and return list whithout \n
    i = 0
    while i < len(list):  # remove \n
        list[i] = list[i].rstrip()
        i += 1
    return list


def create_dictionaries(x):  # function takes in filename and creates two dictionaries
    inputfilename = x
    dictionary1 = {}  # dictionary with editor and list of articles
    try:  # prevent FileNotFoundError
        f = open(inputfilename, "r")
        lines = f.readlines()  # use readlines to create list
        f.close()
    except FileNotFoundError:
        print("file not found")
        return False  # return False if file not found
    for line in lines:  # iterate over items in list
        linelist = line.split(" ")  # split and create list of every line
        linelist = remove_newline(linelist)
        if (
            "REVISION" in linelist
        ):  # were only looking for lines that start with "REVISION"
            if (
                linelist[5] not in dictionary1
            ):  # If editor not in dict then create empty list in dictionary 1
                dictionary1[linelist[5]] = []
            if (
                linelist[3] not in dictionary1[linelist[5]]
            ):  # if article not in the list of this editor
                dictionary1[linelist[5]].append(linelist[3])  # append list with article
    dictionary2 = (
        {}
    )  # dictionary 2 with  {article:(count of edits, [list of editors who revised the article}]}
    f = open(inputfilename, "r")  # open and make list using file again
    lines = f.readlines()
    f.close()
    for line in lines:
        linelist = line.split(" ")
        i = 0
        linelist = remove_newline(linelist)  # use remove_newline funciton to remove \n
        if (
            "REVISION" in linelist
        ):  # were only looking for lines that start with "REVISION"
            if (
                linelist[3] not in dictionary2
            ):  # if article not in dict3, set value to  list with count of \
                dictionary2[linelist[3]] = [
                    0,
                    [],
                ]  # edits and list of editors who revised the article
            dictionary2[linelist[3]][0] += 1  # add 1 to count for every new edit
            if (
                linelist[5] not in dictionary2[linelist[3]][1]
            ):  # if editor not in list within value of dict2, append with editors name
                dictionary2[linelist[3]][1].append(linelist[5])
    return dictionary1, dictionary2  # return dict1 and dict 2 to main function


def topeditors(
    n, dictionary1
):  # displays top n editors who have revised the most articles using dict1
    print("-" * 48)  # output table formating
    print("username" + (" " * 25) + "number of edits")
    print("-" * 48)
    sortedkeys = sorted(
        dictionary1, key=str.lower
    )  # create sorted list of dictionary keys, beacause need to use alphabetic order in case of same values.
    while n > len(sortedkeys):  # if n exceeds total editors
        n = int(input("n exceeds total editors, enter again : "))
    while n <= 0:  # if n negative or 0
        n = int(input("n can't be less than or equal to 0, enter again : "))
    for i in range(n):  # user top 'n' as range
        max = 0
        usernamemax = ""
        for key in sortedkeys:
            if (
                len(dictionary1[key]) > max
            ):  # look at length of that key's value in dict 1
                max = len(dictionary1[key])  # set new max
                usernamemax = key  # key is usernmaemax
        print(usernamemax + (" " * (33 - len(usernamemax))) + str(max))  # print output
        sortedkeys.remove(
            usernamemax
        )  # remove max to avoid the same max being displayed n times


def topedits(
    n, dictionary2
):  # displays top n articles which have been edited the most using dict2
    print("-" * 72)  # output table formating
    print("article" + (" " * 30) + "number of times article was revised")
    print("-" * 72)
    sortedkeys = sorted(dictionary2, key=str.lower)
    while n > len(sortedkeys):
        n = int(input("n exceeds total articles, enter again : "))
    while n <= 0:
        n = int(input("n can't be less than or equal to 0, enter again : "))
    for i in range(n):
        max = 0
        articlemax = ""
        for key in sortedkeys:
            if dictionary2[key][0] > max:  # compare index 0 in dictionary 2
                max = dictionary2[key][0]
                articlemax = key
        print(articlemax + (" " * (37 - len(articlemax))) + str(max))
        sortedkeys.remove(articlemax)


def toparticles(
    n, dictionary2
):  # displays articles that have been revised by the most editors
    sortedkeys = sorted(dictionary2, key=str.lower)
    while n > len(sortedkeys):
        n = int(input("n exceeds total articles, enter again : "))
    while n <= 0:
        n = int(input("n can't be less than or equal to 0, enter again : "))
    print("-" * 80)
    print("article" + (" " * 30) + "number of editors that revised this article")
    print("-" * 80)
    for i in range(n):
        max = 0
        articlemax = ""
        for key in sortedkeys:
            if (
                len(dictionary2[key][1]) > max
            ):  # compare length of index one in dictionary 2
                max = len(dictionary2[key][1])
                articlemax = key
        print(articlemax + (" " * (37 - len(articlemax))) + str(max))
        sortedkeys.remove(articlemax)


def toparticlesyears(
    n, year, file
):  # displays articles that have been revised by the most editors in a specific year
    yearfound = False
    dict3 = (
        {}
    )  # create new dictionary with article as key, and editors in the entered year
    f = open(file, "r")
    lines = f.readlines()
    f.close()
    lines = remove_newline(lines)
    for line in lines:
        linelist = line.split()
        if "REVISION" in linelist:
            yearfile = (linelist[4].split("-"))[
                0
            ]  # split using '-' and then compare year with enterd year
            if int(yearfile) == year:
                yearfound = True  # yearfound is now true
                article = linelist[3]
                author = linelist[5]
                if article not in dict3:
                    dict3[article] = []
                if (
                    author not in dict3[article]
                ):  # append list in dict3 value with author
                    dict3[article].append(author)
    if (
        not yearfound
    ):  # if no articles in that year then print the following and don't execute rest of the function.
        print("no editors edited articles in the year :", year)
    else:  # if year is found
        sortedkeys = sorted(dict3, key=str.lower)
        while n > len(sortedkeys):
            n = int(input("n exceeds total articles, enter lower amount : "))
        while n <= 0:
            n = int(input("n can't be less than or equal to 0, enter again : "))
        print("-" * 102)  # output table
        print(
            "article"
            + (" " * 30)
            + "number of editors that revised this article with comments in",
            year,
        )
        print("-" * 102)
        for i in range(n):  # top 'n' articles in that year
            max = 0
            articlemax = ""
            for key in sortedkeys:
                if (
                    len(dict3[key]) > max
                ):  # similar to top articles function, comapre lenght
                    max = len(dict3[key])
                    articlemax = key
            print(articlemax + (" " * (37 - len(articlemax))) + str(max))
            sortedkeys.remove(articlemax)


def main():  # main function which recieves commands and calls other functions
    command = input("command : ")  # ask for user command
    command = command.split(" ")  # turn command into list
    while (
        len(command) > 4
    ):  # prevent invalid commands (longest command currenty has len of 4)
        command = input("enter valid command : ")
        command = command.split(" ")
    i = 0  # convert items in list to lower so that case of command has no impact on comparisons
    while i < len(command):
        command[i] = command[i].lower()
        i += 1
    while command[0] != "quit":  # program will keep running until 'quit' is entered
        try:  # avoid situation in which dictionaries were not created and top functions were called
            if (
                command[0] == "help"
            ):  # print possible command if first item in command list is 'help'
                print(
                    "Possible Commands :\n• HELP\n• INPUT filename\n• TOP n EDITORS\n• TOP n EDITS\n• TOP n ARTICLES\n• TOP n ARTICLES YEAR"
                )
            elif (
                command[0] == "input"
            ):  # if first item in command list is 'input', get filename to create dictionaries
                file = command[1]  # file will be second item in command list
                if (
                    create_dictionaries(file) != False
                ):  # create dictionaries function will return False if file is not in user's computer.
                    dict1, dict2 = create_dictionaries(file)  # create two dictionaries
                    print(
                        "data stored"
                    )  # tell user that data has been stored in dictionaries
            elif command[0] == "top":
                n = int(
                    command[1]
                )  # number of items user wants is second item in command list
                if (
                    len(command) == 4
                ):  # if command has len 4, get year for top articles-year function.
                    year = int(command[3])
                if command[2] == "editors":
                    topeditors(n, dict1)  # call topeditors function
                elif command[2] == "edits":
                    topedits(n, dict2)  # call topedits function
                elif (
                    command[2] == "articles" and len(command) == 3
                ):  # if len 3, then no year specified
                    toparticles(n, dict2)  # call top articles function
                else:
                    toparticlesyears(n, year, file)  # else top articles year
            else:  # if user enters anything else, then print the following
                print("command not avaliable. use 'help' to see accpeted ccommands")
        except UnboundLocalError:  # avoid situation in which dictionaries were not created and top functions were called
            print("dictionaries not yet created, use 'input filename' to store data")
        command = input(
            "command : "
        )  # ask for user comment again to continue while loop
        command = command.split(" ")
        i = 0
        while i < len(command):
            command[i] = command[i].lower()
            i += 1
    print("done")  # print done if user enters 'quit'


main()
