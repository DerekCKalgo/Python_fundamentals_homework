#A function can have multiple return statements. When any of them is executed, the function terminates.

def biggie(list):
    for x in range (len(list)):
        if list[x]>0:
            list[x]="big"
    return list

a=biggie([1, -121, 3, -21, -3, 0, 3, 6, -2])
print(a)


def countpos(list):
    sum=0
    for x in range (len(list)):
        if list[x]>0:
            sum=sum+1
    list[len(list)-1]=sum
    return list

a=countpos([-23, 3, -33, -33, 4, 424, 535, -242, 2342, 2, 77])
print(a)


def sum(list):
    sum=0
    for x in range(len(list)):
        sum=sum+list[x]
    return sum

a=sum([23, 5, -23, 4, 5, 6, 0, 100, 3, -10])
print(a)


def average(list):
    sum=0
    for x in range (len(list)):
        sum=sum+list[x]
    return sum/len(list)

a=average([33, 5, 3, 2, 7])
print(a)


def len(list):
    count=0
    for x in list:
        count += 1
    return count

b=len([2, 42, 534, 535, 33, 7, 43, 435, 9])
print(b)


def mini(list):
    if list == []:
        return False
    else:
        min=list[0]
        for x in list:
            if x<min:
                min=x
        return min

a=mini([4, 54, 12412, 32, 14, 435, 6, 112, -23])
print(a)


def maxi(list):
    if list == []:
        return False
    else:
        max=list[0]
        for x in list:
            if x > max:
                max=x
        return max

a=maxi([32, 5, 23421, 234214234234, -21])
print(a)

def ult(list):
    dic={}
    sum=0
    count=0
    min=list[0]
    max=list[0]
    for x in list:
        sum = sum + x
        count += 1
        if x<min:
            min=x
        if x>max:
            max=x
    dic['sumTotal']=sum
    dic['average']=sum/count
    dic['minimum']=min
    dic['maximum']=max
    dic['length']=count
    return dic

a=ult([5, 9, 12, 13, 1, 2, 7])
print(a)


def rev(list):
    for x in range (int(len(list)/2)):
        temp=list[x]
        list[x]=list[len(list)-1-x]
        list[len(list)-1-x]=temp
    return list

a=rev([12, -2, 4, 6, 8, 0, 7, 1231, -233])
print(a)







    
    


