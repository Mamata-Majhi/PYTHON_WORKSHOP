try:
    with open("welcome.txt", "r") as f:
       print(f.read())
    
except FileNotFoundError:
    print("FILE does not exist!!")
    with open("newFile.txt", "w+") as f:
      f.write("Hello, new file!")

finally:
    print("This is finally block.")
    # f.close()


