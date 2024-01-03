# print("\n\nProgram to check whether a number is palindrome or not!!\n")
num=int(input("Enter the number:"))
t=num
res=0
while (num>0):
    a=num%10
    res=res*10+a
    t=num/10
if num==res:
    print("Palindrome!")
else:
    print("Not Palindrome!")

    

