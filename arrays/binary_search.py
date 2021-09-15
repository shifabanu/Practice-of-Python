'''
BINARY SEARCH using ITERATIVE METHOD
Search a particular element and return its index

1. Let min = 0 and max = n-1.
2. If max < min, then stop: target is not present in array. Return -1.
3. Compute guess as the average of max and min, rounded down (so that it is an integer).
4. If array[guess] equals target, then stop. You found it! Return guess.
5. If the guess was too low, that is, array[guess] < target, then set min = guess + 1.
6. Otherwise, the guess was too high. Set max = guess - 1.
7. Go back to step 2.

Pseudocode credits to Khan Academy
'''

def iterate_search(array, n, target):
    min=0
    max = n-1
    
    while(min <= max):
        guess = (min + max) // 2
        
        if(array[guess] == target):
            return guess
        elif(array[guess] < target):
            min = guess + 1
        else:
            max = guess - 1
    return -1    


array = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
        41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
n = len(array)
target = int(input("Enter the number you want to find in the given array: "))
index = iterate_search(array, n, target)
if(index != "-1"):
    print("The number is at ", index, " position in the array")
else:
    print("The number is not present in the given array!")
