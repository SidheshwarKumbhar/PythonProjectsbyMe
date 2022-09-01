import time

start = time.time()
inputList = [[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110, 120]]
outputList = []
index = 0
for i in range(len(inputList[0])):
    outputList.append([])
    for j in range(len(inputList)):
        outputList[index].append(inputList[j][index])
    index += 1


time.sleep(10)
print(outputList)
end = time.time()

print("time need to compute is = ", end - start)
