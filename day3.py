# for loop in python
# nums=[1,2,3,4,5] #list

# for i in range(10,21,2):
#     print(i)

# FizzBuzz Challenge

num=range(1,100)
for i in num:
    if i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)



# name="Biratnagar"
# for character in name:
#     print(character)


# function in python
# def cel_to_far( temp_cel):
   
#     temp_far=(9/5)*temp_cel+32
#     return temp_far
# temp_cel=40
# temp_far=cel_to_far(temp_cel)
# print(f"{temp_cel}C={temp_far}F")



# def sum(a,b):
#     r=a+b
#     return r
# res=sum(12,42)
# print(f"Sum={res}")

def mult(a=2,b=8):
    return(b-a)
result=mult(2)
print(result)

    
    
    



