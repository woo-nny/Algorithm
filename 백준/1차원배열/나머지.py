numList = []
for i in range(10):
    num = int(input())
    numList.append(num%42)
print(len(set(numList)))
