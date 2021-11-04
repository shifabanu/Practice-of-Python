'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

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
    

