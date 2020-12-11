#A function can have multiple return statements. When any of them is executed, the function terminates.

def countdown(num):
    list=[]
    for x in range (num, -1, -1):
        list.append(x)
    return list

a=countdown(2)
print(a)

def printandreturn(list):
    print(list[0])
    return list[1]

a=printandreturn([888, 6])
print(a)

sum=0
def first_plus_length(list):
    sum=list[0]+len(list)
    return sum

a=first_plus_length([90, 5, 2, 5, 5343, 2, 33, 343, 'r', 55, 'f'])
print(a)
    

def values_greater_than_second(list):
    if len(list) < 2:
            return False
    newlist=[]
    sum=0
    for x in range (0, len(list), 1):
        if list[x] > list[1]:
            sum=sum+1
            newlist.append(list[x])
    print(sum)
    return newlist

a=values_greater_than_second([2, 1, 4, 55, 34343, 34342, 66])
print(a)


def lengthvalue(size, value):
    list=[]
    for x in range (size):
        list.append(value)
    return list

a=lengthvalue(5, 3)
print(a)













