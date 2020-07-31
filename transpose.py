from numpy import *
r,c=[int(a) for a in input("Enter rows,cols: ").split()]
str=input("Enter matrix elements:\n")
x=reshape(matrix(str),(r,c))
print("The original matrix: ")
print(x)
print("Transpose matrix: ")
y=x.transpose()
print(y)
