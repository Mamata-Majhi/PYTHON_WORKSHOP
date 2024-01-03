try:
    f = open("hello.txt", "r")

except FileNotFoundError:
    print("FILE does not exist!!")

finally:
    print("hello")

