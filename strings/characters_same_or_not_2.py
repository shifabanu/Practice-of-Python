'''

check whether each string in a list has all the characters same or not.

'''

string_list = ["aaaaaaaa", "abbbababba", "dddddddddd"]

for string in string_list:
    if string == len(string)*string[0]:
        print("String {} has all the characters same".format(string))
    else:
        print("String {} does not have same characters".format(string))
