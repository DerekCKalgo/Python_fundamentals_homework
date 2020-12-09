for x in range (0, 151):
    print (x)

for x in range (5, 1001, 5):
    print (x)

for x in range (1, 101, 1):
    print (x)
    if x%10 == 0:
        print ("Coding Dojo")
    elif x%5 == 0:
        print ("Coding")

sum=0
for x in range (1, 500000, 1):
    if x%2 != 0:
        sum = sum+x
print(sum)

for x in range (2018, 0, -4):
    print (x)
 
lowNum=2
highNum=102
mult=7
for x in range (lowNum, highNum+1, 1):
    if x%mult == 0:
        print (x)
    
