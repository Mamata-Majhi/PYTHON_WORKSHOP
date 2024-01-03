# file handling in python
# we use open(filename,mode) for opening file
# read=r,write=w,append=a,delete=d

# with open("file.txt","r") as fd:

f=open("welcome.txt","r")
print(f.read())
f.close()