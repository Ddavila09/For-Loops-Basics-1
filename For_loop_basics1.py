for i in range(151):
    print(i)

for i in range (5,1005,5):
    print(i)

for i in range(1,101):
    if i % 10 == 0:
        print("Coding Dojo") 
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

sum = 0
for i in range(1,500001,2):
    sum += i
print(sum)

for i in range(2018,0,-4):
    print(i)

lowNum=13
highNum=27
mult=5

for i in range (lowNum,highNum):
    if i % mult == 0:
        print(i)
