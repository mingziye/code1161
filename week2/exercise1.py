"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
#I think this will define something here.
some_words = ['what', 'does', 'this', 'line', 'do', '?']#it list a string of words.
#I think this will do something with some_word.
for word in some_words: #it ask for list words in some_word.
    print(word)#it printed “those words in some_word
#I think this will do something with some_word.
for x in some_words:#it ask for x in some_word.
    print(x)#x is not define in some_word so not to be printed.
#I think it will print some_words.
print(some_words)#It printed some_words.
#I think it will define something.
if len(some_words) > 3:#it assumed a consequence.
    print('some_words contains more than 3 words')#it printed"some_words contains more than 3 words."
#I think it will define a usefulFunction.
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())#it ask for print a list of namedtuple attributes and their value.
#I think it will execute the define.
usefulFunction()#it ask for execute the usefulFunction.
