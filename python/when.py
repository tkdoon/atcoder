K = int(input())
if (K % 60)//10 != 0:
    print(21+K//60, ":", K % 60, sep="")
else:
    print(21+K//60, ":0", K % 60, sep="")
