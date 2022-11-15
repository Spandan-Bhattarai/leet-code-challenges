abc=input("Enter a string: ")
new=[]
new.append(abc[0])
for i in range (len(abc)):
    status="False"
    for j in range (len(new)):
        if (abc[i]==new[j]):
            status="True"
    if (status=="False"):
        new.append(abc[i])
print(len(new))
