#set A
A={1,3,5,6,7,9,10}
#set B
B={0,2,4,6,7,8,10}

# perform union operation
# we can also perform union operation using union()(i.e A.union(B))
print("Union:",A|B)

# perform intersection operation using intersection()
print("Intersection:",A.intersection(B))

# perform difference operation using difference()
print("Difference:",A.difference(B))