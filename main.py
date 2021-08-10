x0 = 1 
x1 = 1 
y = int(input("x = ? \n"))
x = list(range(0, y))

x[0] = x0 
x[1] = x1
for n in range(len(x)-2):
    x[n+2] = int(x[n+1]) + int(x[n])
    
print(x)