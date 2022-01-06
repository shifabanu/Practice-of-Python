'''
Swap the alphabets only in a given string
'''
str = "A,b$c="
i=0
j=len(str) - 1 
while(i<=j):
    if str[i].isalpha() && str[j].isalpha():
        tmp = str[j]
        str[j] = str[i]
        str[i] = tmp
        i++
        j--
    elif str[i].isalpha() || str[j].isalpha():
        if str[i].isalpha():
            j--
        else:
            i++
    else:
        i++
        j--
    

