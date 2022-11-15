num = [] 
n = int(input('Enter size of the list: ')) 
 
for i in range(n): 
    temp = int(input('Enter number to add to my list: ')) 
    num.append(temp) 
target=int(input("Enter an interger: "))
for i in range(len(num)):
    for j in range (i):
        s=num[i]+num[j]
        if s==target:
            print(num[i],num[j])
