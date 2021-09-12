'''

check whether each string in a list has all the characters same or not.

'''

string_list = ["aaaaaaaa", "abbbababba", "dddddddddd", "adhfuvhrk", "sss"]
for string in string_list:
    flag = True
    for i in range(0, len(string)-1):
        if string[i] != string[i+1]:
            flag = False
            print("String {} does not have same characters".format(string))
            break
    if flag == True:
        print("String {} has all the characters same".format(string))
