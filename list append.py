lis1=[2, 1, 3, 5]
lis2=[6, 4, 3]
lis1.extend(lis2)
print(lis1)
for i in range(0, len(lis1)):
    print(lis1[i])
lis1.append(lis2)
print(lis1)
