import math
n = int(input())
# c = list(input().split())
c = input()
whiteCount = 0

for i in range(math.ceil(n/2)):
    if c[i] == "W":
        whiteCount += 1
print(whiteCount)
# 失敗作
