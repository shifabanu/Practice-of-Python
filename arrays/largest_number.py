'''

Find the largest number without using built in function

'''

array = [] #create an empty array

length = int(input("Length of your array is: "))

for i in range(0, length):
    number = int(input("Enter the element of the array: "))
    array.append(number)

print("You entered: ", array)

#find the largest number among in the array

max = array[0]

for j in range(0, length):
    if array[j] > max:
        max = array[j]

print("The largest number is: ", max)

