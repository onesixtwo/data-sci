import numpy as vargas

'''r1 = vargas.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

r2 = vargas.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

r3= vargas.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print('array 1\n',r1)
print('array 2\n',r2)
print('array 2\n',r3)
print('array combined\n')
print(r1+r2+r3)'''

p1 = vargas.array([
    [1,2,3,10],
    [4,5,6,11],
    [7,8,9,12]
])

to = vargas.sum(p1,axis=0)

b = vargas.argmax(((to - to[0])/to[0])*100)
w = vargas.argmin(((to - to[0])/to[0])*100)

print('array \n',p1)
print('array sum \n',to)
print('best performing time period: ',b)
print('best performing time period: ',w)
