inputs = [0, 2, -1, 3.3, -2.7, 1.1, 2.2, -100]

output=[]

for i in inputs:
    if i<=0:
        output.append(0)
    else:
        output.append(i)

print(output)