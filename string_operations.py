""" String Operations using built-in string methods in Python
    Author: Anirban Majumder
    Creation Date: December, 2017
    Version: v1.0                                          """

""" Here are the list of common and popular string functions in Python """

""" (1) capitalize() -> This method is used to capitalize first letter of the string """

str = "the boy is playing in the ground."

print ("str.capitalize(): ", str.capitalize())

""" Output -> str.capitalize():  The boy is playing in the ground. """

#-------------------------------------------------------------------------------------------#

""" (2) center(width,fillchar) -> This method is used to return the original
string centered to a total of width columns with default filler as space """

str = "the boy is playing in the ground."

print ("str.center(50, 'a'): ", str.center(50, 'a'))

""" Output -> str.center(50, 'a'):  aaaaaaaathe boy is playing in the ground.aaaaaaaaa """

#-------------------------------------------------------------------------------------------#

""" (3) count(sub, start=0, end=len(string)) -> This method is used to return the number
of occurences of substring sub in the range [start, end] where start indicates the search
starts from this index and end indicates the search ends from this index """

str = "the boy is playing in the ground."

sub = "o"

print ("str.count(sub, 10, 30): ",str.count(sub, 10, 30))

""" Output -> str.count(sub, 10, 30):  1 """

#-------------------------------------------------------------------------------------------#

""" (4) endswith(suffix, beg=0, end=len(string)) & startswith(suffix, beg=0, end=len(string)) -> These methods
are used to return true if the string ends or starts with the specified suffix, otherwise return false """

str = "the boy is playing in the ground."

suffix = "d."

print ("str.endswith(suffix, 0, len(str)): ", str.endswith(suffix, 0, len(str)))

suffix = "the"

print ("str.startswith(suffix, 0, len(str)): ", str.startswith(suffix, 0, len(str)))

""" Output -> str.endswith(suffix, 0, len(str)):  True
str.startswith(suffix, 0, len(str)):  True  """

#-------------------------------------------------------------------------------------------#

""" (5) find(str, beg=0, end=len(string)) & index(str, beg=0, end=len(string)) -> These methods
are used to determine if string str occurs in string or in substring if beg and end are specified.
If no string is found then find returns -1 and index raises an exception. """

str1 = "the boy is playing in the ground."

str2 = "boy"

print ("str1.find(str2, 0, len(str1)): ", str1.find(str2, 0, len(str1)))

print ("str1.index(str2, 0, len(str1)): ", str1.index(str2, 0, len(str1)))

""" Output -> str1.find(str2, 0, len(str1)):  4
str1.index(str2, 0, len(str1)):  4 """

#-------------------------------------------------------------------------------------------#

""" (6) upper() & lower() -> These methods are used to upper and lower the cases of the string """

str = "The boy is playing in the ground."

print ("str.upper()): ", str.upper())

print ("str.lower()): ", str.lower())

""" Output --> str.upper()):  THE BOY IS PLAYING IN THE GROUND.
str.lower()):  the boy is playing in the ground. """

#-------------------------------------------------------------------------------------------#

""" (7) min(str) & max(str)-> These methods are used to return the minimum and maximum alphabetical
character from the string str """

str = "The boy is playing in the ground."

print ("min(str): ", min(str))

print ("max(str): ", max(str))

""" Output --> min(str):   max(str):  y """


#-------------------------------------------------------------------------------------------#

""" (8) lstrip() & rstrip(str) & strip(str)-> These methods are used to remove all leading whitespaces,
trailing whitespaces and both leading and trailing whitespaces respectively """

str1 = "    The boy is playing in the ground."

str2 = "The boy is playing in the ground.   "

str3 = "   The boy is playing in the ground.   "

print ("str1.lstrip(): ", str1.lstrip())

print ("str2.rstrip(): ", str2.rstrip())

print ("str3.strip(): ", str3.strip())

""" Output --> str1.lstrip():  The boy is playing in the ground.
str2.rstrip():  The boy is playing in the ground.
str3.strip():  The boy is playing in the ground. """

#-------------------------------------------------------------------------------------------#

""" (9) len(str)-> This method is used to return the length of the string """

str = "The boy is playing in the ground."

print ("len(str)): ", len(str))

""" Output --> len(str)):  33 """

#-------------------------------------------------------------------------------------------#

""" (10) replace(old, new, max))-> This method is used to replace old string with the new one
restricting the number of replacements to max """

str = "The boy is playing in the ground. is, is"

print ("str.replace('is','was', 2)): ", str.replace("is","was", 2))

""" Output --> str.replace('is','was', 2)):  The boy was playing in the ground. was, is """

#-------------------------------------------------------------------------------------------#

""" (11) join(sequence)-> This method is used to return a string which is the concatenation
of the strings in the sequence. The seperator between elements is the string providing this method. """

str = "-"

sequence = ("a","b","c","d")

print ("str.join(sequence): ", str.join(sequence))

""" Output --> str.join(sequence):  a-b-c-d """

#-------------------------------------------------------------------------------------------#

""" (12) split(str="", num=string.count(str)) --> This method is used to return a list of all the words
in the string using str as the seperator limiting the number of splits to num.
If str is not specified, it splits on all whitespaces.  """

str1 = "The boy is playing in the ground"

print ("str1.split(): ", str1.split())

""" Output --> str1.split():  ['The', 'boy', 'is', 'playing', 'in', 'the', 'ground'] """

str2 = "The_boy_is_playing_in_the_ground"

print ("str2.split('_'): ", str2.split('_'))

""" Output --> str2.split('_'):  ['The', 'boy', 'is', 'playing', 'in', 'the', 'ground'] """

str3 = "The_boy_is_playing_in_the_ground"

print ("str3.split('_', str3.count('_')): ", str3.split('_', str3.count('_')))

""" Output --> str3.split('_', str3.count('_')):  ['The', 'boy', 'is', 'playing', 'in', 'the', 'ground'] """

str4 = "The_boy_is_playing_in_the_ground"

print ("str3.split('_', 3): ", str3.split('_', 3))

""" Output --> str3.split('_', 3):  ['The', 'boy', 'is', 'playing_in_the_ground'] """
