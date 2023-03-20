x = [1,2,3,4,5]
y= [1,2,3,4,5]
z = [x+y for x,y in zip(x,y)]
print(z)