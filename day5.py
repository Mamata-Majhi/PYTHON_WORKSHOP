# # program to demonstrate a number is palindrome or not
num=int(input("Enter a number:"))
a=num
b=0
while(a>0):
    p=a%10
    b=b*10+p
    a=a/10
if a==b:
    print("The number is palindrome.")
else:
    print("The number is not palindrome.")


    
# contact book
# print("Contact Book")
# print("1.Add\t2.Edit\t3.List\t4.Delete\t5.Exit")

# exception handling
# list=[1,2,3,4,5]
# try:
#     print(list[7])
#     x=100/0
# except ZeroDivisionError:
#     print("Can't divide by zero")
# except IndexError:
#     print("List does not have that index")
# finally:
#     print("Always execute")




