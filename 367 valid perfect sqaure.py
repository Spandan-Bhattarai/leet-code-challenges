n=int(input("Enter a number: "))
value="False"
for i in range(1, n+1):
    if(i**2==n):
        value="True"
print(value)


"""
if leetcode says time excedded
just do this

return (num ** 0.5) % 1 == 0

"""