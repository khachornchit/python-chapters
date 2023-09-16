import re

s = "sajdkasjdsak).' asdasdasds"


def filter_word1(s):
    return s.replace('\"', '').replace(")", '').replace("(", '').replace(",", '').replace(".", '').replace("\'", '')


def filter_word2(s):
    return re.sub("\"|\'|\)|\(|\.", "", s)


print("Original string1: ", s)
print(filter_word2(s))

string = "A master of all is a master of none"
print("Original string2: ", string)

string = re.sub("m|n|\s", "#", string)
print("New string: ", string)
