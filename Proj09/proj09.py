###############################################################################
#User input file is opened
#In the fuction fill_completions(), a dictionary is created with the format 
#   {([character spot in word],[character]): [list of words that match this 
#   rule]} based on all the words in the input file.
#User is prompted to enter a word stub
#Provided the stub is not "#" (the exit condition) the dictionary created in 
#   fill_completions() is searched for words that begin with the same word stub
#The set returned by fill_completions() is priinted in the desired format
#When the exit condition ("#") is entered, while loop terminates
#File is closed
###############################################################################
import string

def open_file():
    """
    Function opens the file specified by the user while checking to make sure 
    the input is an existing file.
    fp: a file pointer that will assign the contents of the file to a variable
    """
    exit_bool = False
    
    while exit_bool != True:
        try:
            file_name = input("Input a file name: ")
            fp = open(file_name)
        except FileNotFoundError:
            while exit_bool != True:
                try:
                    file_name = input("Error: Input a file name: ")
                    fp = open(file_name)
                except FileNotFoundError:
                    continue
                exit_bool = True
            continue
        exit_bool = True
    return fp

def fill_completions(fp):
    """
    taking a file pointer, this function creates a dictionary with the format:
    {([character spot in word],[character]): [list of words that match this 
    rule]}. This is done by iterating through all the characters in all the 
    words in the file pointer.
    fp: file pointer opened by open_file()
    char_dict: a dictionary of the format described above
    """
    char_dict, word_list = {}, []
    
    for line in fp:
        #the words in the line are split and stripped down and checked to be
        #legitimate words
        word_list = line.strip().split()
        word_list = [w.lower().strip(string.punctuation) for w in word_list]

        for word in word_list:
            skip_word = False
            #if the word is only 1 character long, ignore it
            if len(word) <= 1:
                continue
            #Need to make sure words with "non-alphabetic characters are 
            #ignored"
            for punct in string.punctuation:
                if punct in word:
                    skip_word = True
            if skip_word == False:
                for char_spot, char in enumerate(word):
                    tup = (char_spot, char)
                    if tup not in char_dict:
                        char_dict[tup] = [word]
                    else:
                        char_dict[tup].append(word)
    for key in char_dict:
        list_to_set = set(char_dict[key])
        char_dict[key] = list_to_set
    return char_dict

def find_completions(prefix, c_dict):
    """
    taking a user defined word stub, this function finishes the word based on 
    how the function fill_completions() seen words with that stub tend to be 
    finished.
    prefix: a user defined word stub
    c_dict: the dinctionary created by the function fill_completions()
    completions_set: the set of all the possible ways to finish the word stub
    """
    match_list, matching_words, completions_set = [], (), ()
    
    for keys in c_dict:
        if keys[0] <= len(prefix)-1 and prefix[keys[0]] == keys[1]:
            match_list.append(keys)
    
    #convert the match list to a set so that set intersections can be used
    matching_words = set(c_dict[match_list[0]])
    for keys in match_list:
        try:
            matching_words = c_dict[keys].intersection(matching_words)
        except IndexError:
            continue
    completions_set = matching_words
    return completions_set
    

fp, prefix = "", ""

fp = open_file()
c_dict = fill_completions(fp)

while prefix != "#":
    prefix = input("Enter the prefix to complete (or '#' to quit): ")
    if prefix != "#":
        #search the dictionary for completions
        completions_set = find_completions(prefix, c_dict)
        print("Completions of {}:".format(prefix), end = " ")
        #display results
        for words in completions_set:
            print(words, end = " ")
        print(" ")
    
fp.close()

# Questions 
# Q1: 7
# Q2: 3
# Q3: 2
# Q4: 7