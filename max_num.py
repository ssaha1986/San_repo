lst = []
num = int(input("Enter the total numbers to be checked in the list: "))

for i in range(0,num):
    n = int(input("Enter the number: "))
    lst.append(n)
print("The list : {}".format(lst))

# Finding the maximum number in the list
print("The number with the maximum value in the list is: {}".format(max(lst)))
