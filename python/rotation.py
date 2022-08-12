n, q = map(int, input().split())
s = input()


for i in range(q):
    query1, query2 = map(int, input().split())
    if query1 == 1:
        for j in range(query2):
            strage = s[-1]
            s = s[:-1]
            s = strage+s
    else:
        print(s[query2-1])
