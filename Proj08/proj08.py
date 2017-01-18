###############################################################################
#List of languages and associated translation files are established
#Text to be translated is established
#.tei dictionaries are imported
#   The time proceding dictionary import is recorded
#   .tei files are imported in loadListFormattedDatabases()
#   These files are compiled into a single lised based database of translations
#   The time proceding dictionary import is recorded
#Text is preprocessed to convert it into a list of words. This list is 
#displayed
#Translation is conducted via a list based translation database
#   The time proceding list based translation is recorded
#   performListBasedTranslations() is called, passing the processed text and
#   the list based language databases created above
#       translateFromList is called passing the translation database of each
#       language into it. These translations are then deplayed under the
#       language in which they happened
#   The time following list based translation is recorded
#Translation is conducted via a dict based translation database
#   The time proceding dict based translation is recorded
#   performDictBasedTranslations() is called, passing the processed text and
#   the dict based language databases created above
#       translateFromDict is called passing the translation database of each
#       language into it. These translations are then deplayed under the
#       language in which they happened
#   The time following dict based translation is recorded
#Runtimes are displayed showing the diffrence between the start and stop times
###############################################################################
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 13:00:10 2016

This project was initially created for CSE 231 at Michigan State University.
The main goal of this project is to help students understand the notion of
dictionaries versus the notion of lists in Python (and the corresponding
datastructures in any other programming language). After completing his/her
part of the code, the student should be able to pinpoint the performance
differences between the two of them. A student taking this project is expected
to know how to code control structures, lists, functions and basic I/O.

@author: Haitham Seada
"""
import time

from tei_parser import parseTeiFile

def preprocess(text):
    """
    Prepares the input string for later processing. It converts questions marks
    '?' and exclamation marks '!' to dots '.', removes all other special 
    symbols except dots and makes sure that a dot is always adjacent to its 
    previous word and one space away from its subsequent word. In addition, 
    this function converts all letters to lower case.
    """
    scan1 = ""
    for c in text:
        if c.isalnum() or c.isspace() or c == '.':
            scan1 += c.lower()
        elif c in ['?', '!']:
            scan1 += '.'
    scan2 = ""
    for c in scan1:
        if len(scan2) > 0:
            if scan2[-1].isspace() and c == '.':
                scan2 = scan2.strip()
            elif scan2[-1] == '.' and c.isalnum():
                scan2 += ' '
        scan2 += c
    return scan2

def display(languageName, text):
    """
    Display text titled with the name of its language
    """
    print()
    print("-------")
    print(languageName)
    print("-------")    
    print(text)

def displayTimeInfo(loadStartTime, loadEndTime, listBasedTranslationStartTime,\
    listBasedTranslationEndTime, dictBasedTranslationStartTime,\
    dictBasedTranslationEndTime):
    print()
    print("--------------------")
    print("Running-Time Summary")
    print("--------------------")
    print("\tPrasing input files: {:3.2f} seconds.".format( \
        loadEndTime-loadStartTime))
    print("\tList-based translations: {:3.2f} milliseconds.".format( \
        (listBasedTranslationEndTime-listBasedTranslationStartTime)*1000))
    print("\tDict-based translations: {:3.2f} milliseconds.".format( \
        (dictBasedTranslationEndTime-dictBasedTranslationStartTime)*1000))

"""
*******************************************************************************

All the functions in the following section deals with list-based databases.
A single list-based is structured as simply a list of tuples as follows:
[(w1,w1-translation), (w2,w2-translation), ...].

*******************************************************************************
"""

def lookUpList(word, listBasedDb):
    """
    Looks up the translation of a word in a list-structured DB
    """
    for combination in listBasedDb:
        if combination[0] == word:
            return combination[1]

def translateFromList(text, listBasedDb):
    """
    Translates text from English to the language of the specified DB. The 
    specified DB must be in a list-based structure. This function searches for 
    each word of the text in that list structure (the DB) and concatenates the 
    translations of all words. It also handles the special case when a full 
    stop follows some word.
    """
    translation = ""
    words = text.split()
    for word in words:
        toAppend = ''
        if word[-1] == '.':
            word = word[:-1]
            toAppend = '.'
        translatedWord = lookUpList(word, listBasedDb)
        if not translatedWord:
            translatedWord = word
        translation += translatedWord + toAppend + ' '
    return translation.strip()  
    
def loadListFormattedDatabases(languages):
    """
    Loads the databases of the languages specified. Each database is structured 
    as a list of pairs (word, translation). The final returned structure is a 
    list of tuples, each tuple has the following structure:
    (langName,langListBasedDb) -- e.g. --> ("Arabic", listBasedArabicDb)
    """
    listBasedDatabases = []
    for language in languages:
        # Get the name of the language e.g. Arabic, Hindi etc.
        langName = language[0]
        print("Preparing English to {:8s} database... ".format(langName), \
              end="")
        # Get the database of translations from English to the current language
        langListBasedDb = parseTeiFile(language[1])
        print("Done.")
        # Add information as a tuple to the final list
        listBasedDatabases.append((langName, langListBasedDb))
    # Return the final list-structured DB
    return listBasedDatabases

def performListBasedTranslations(preprocessedText, listBasedDatabases):
    """
    This function performs all the high-level logic of list-based translations.
    """
    for tup in listBasedDatabases:
        translatedText = translateFromList(preprocessedText, tup[1])
        display(tup[0], translatedText)

"""
*******************************************************************************

All the functions in the following section deals with list-based databases.
A single list-based is structured as simply a list of tuples as follows:
[(w1,w1-translation), (w2,w2-translation), ...].

*******************************************************************************
"""


def getDictFormattedDatabases(listDatabases):
    """
    Loads the databases of the languages specified. Each database is structured 
    as a dictionary {key=word, value=translation}. The final returned structure 
    is a list of tuples, each tuple has the following structure:
    (langName,langDictBasedDb) -- e.g. --> ("Arabic", dictBasedArabicDb)
    """
    DictDatabases = [] #establishes a list
    for element_spot, element in enumerate(listDatabases):
        DictBasedDb = {} #establishes a dictionary
        for word_pair in element[1]:
            try:
                #Used to avoid situations in which the list and dict based Db's
                #produce diffrent translations
                DictBasedDb[word_pair[0]]
                continue
            except KeyError:
                DictBasedDb[word_pair[0]] = word_pair[1]
                word_pair = []
        #Establishes a blank space in list
        DictDatabases.append("")
        #Rewrites blank space with (language, dictionary) pair
        DictDatabases[element_spot] = ((element[0],DictBasedDb))
    return DictDatabases
    """
    The code that goes here should convert databases from their original
    list-based structures to dictionary-based structures. The input parameter
    is a list of tuples in the following form:
    
        [(lang1-name, list-based-DB1), (lang2-name, list-based-DB2), ...]
        e.g.
        [("Arabic", arabicListBasedDb), ("Hindi", hindiListBasedDb), ...]
    
    A single list-based DB (the second element in each of the tuples above)
    takes again the form of a list of tuple, as follows:
    
        [(word1, word1-translation), (word2, word2-translation), ...]
        e.g.
        [('have','avoir'), ('baby','bébé'), ...]
        
    The output format should be in the following form:

        [(lang1-name, dict-based-DB1), (lang2-name, dict-based-DB2), ...]
        e.g.
        [("Arabic", arabicDictBasedDb), ("Hindi", hindiDictBasedDb), ...]
        
    A sinlge dict-based DB (the second element in each of the tuples above)
    should take the following form:

        {word1:word1-translation, word2:word2-translation, ...}
        e.g.
        {'have':'avoir', 'baby':'bébé', ...}
    """

def translateFromDict(text, dictBasedDb):
    """
    Translates text from English to the language of the specified DB. The 
    specified DB must be in a dict-based structure. This looks up each word of 
    the text in that dict-based structure (the DB) and concatenates the 
    translations of all words. It also handles the special case when a full 
    stop follows some word.
    """
    translation = ""
    words = text.split()
    for word in words:
        #This segument keeps track of the apperence of periods so that they can
        #be added in the translation string
        toAppend = ''
        if word[-1] == '.':
            word = word[:-1]
            toAppend = '.'
        #attempt to find the english word key in the dictionary and return the
        #word in the other langauge
        try:
            translatedWord = dictBasedDb[word] 
        #if the translation cant be found, the word is added to the translation
        #string unchanged
        except KeyError:
            translatedWord = word
        translation += translatedWord + toAppend + ' '
    return translation.strip()
    """
    Replace the pass command with the appropriate logic. Your logic should
    return the translation of the text parameter. Special care should be
    given to those words followed by a full stop. Notice that due to the
    initial preprocessing of the inputed text, a full stop will always be
    adjacent to its preceding word and at least one space away from its
    subsequent word.
    """    

def performDictBasedTranslations(preprocessedText, dictBasedDatabases):
    """
    This function performs all the high-level logic of dict-based translations.
    """
    for tup in dictBasedDatabases:
        #tup is a tuple of the name of the language (ex: "Arabic") and the
        #dictionary based translation database
        translatedText = translateFromDict(preprocessedText, tup[1])
        display(tup[0], translatedText)
    """
    In this function, loop over all your dict-based databases, use 
    translateFromDict(...) to get the translation from each database and
    display the name of the language and the translation using display(...)
    """

"""
*******************************************************************************

MAIN SECTION: This section uses the functions defined above to load translation
databases, perform translation from English to other languages and display
outputs. In addition, this section is responsible for displaying the time
spent on each of these steps.

*******************************************************************************
"""
# Start parsing your dictionaries
languages = [ \
                ("Arabic","eng-ara.tei"), \
                ("Spanish","eng-spa.tei"), \
                ("Hindi","eng-hin.tei"), \
                ("Russian","eng-rus.tei"), \
                ("French","eng-fra.tei"), \
                ("German","eng-deu.tei"), \
                ("Italian","eng-ita.tei")]

# The text to be translated
text = "Have you ever seen the pyramids ?By the way, they are not " + \
            "just three   . Only in Egypt there are approximately 120 " + \
            "pyramids. Other pyramids can be fount in Sudan, Mexico, Peru, "+ \
            "Indonesia, Cambodia, Spain, Algeria, Greece, Iran and China."


# Record loading start time
loadStartTime = time.time()
# Load all list-based databases
listBasedDatabases = loadListFormattedDatabases(languages)
# Record loading end time
loadEndTime = time.time()

# Pre-processing
preprocessedText = preprocess(text)

# Display the preprocessed English message
display("Original English Text", preprocessedText)

print("-"*60)
print("Translating using list-based databases")
print("-"*60)
# Record list-based translation start time
listBasedTranslationStartTime = time.time()
# Translate to all other languages using list structured DBs
performListBasedTranslations(preprocessedText, listBasedDatabases)
# Record list-based translation end time
listBasedTranslationEndTime = time.time()

print("-"*60)
print("Translating using dictionary-based databases")
print("-"*60)

# Convert list-based DBs to dict-based DBs
dictBasedDatabases = getDictFormattedDatabases(listBasedDatabases)

# Record dict-based translation end time
dictBasedTranslationStartTime = time.time()
# Translate to other languages using dict-structured DBs
performDictBasedTranslations(preprocessedText, dictBasedDatabases)
# Record dict-based translation end time
dictBasedTranslationEndTime = time.time()

# Display running-time information
displayTimeInfo(loadStartTime, loadEndTime, \
    listBasedTranslationStartTime, listBasedTranslationEndTime, \
    dictBasedTranslationStartTime, dictBasedTranslationEndTime)


#Questions:
#Q1:7
#Q2:2
#Q3:2
#Q4:7