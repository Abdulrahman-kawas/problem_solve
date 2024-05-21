Mynumber = [1, 2, 3, 4, 5]
id = [1, 3, 3]

g = []

for i in Mynumber:
    for n in id:
        if len(str(n)) < len(str(i)): #convert int to string for count length 
            g.append(n * Mynumber[-1])# i appended the result of opperation in empty array 
        else:
            g.append(i * n)

print(g)