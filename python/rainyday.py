x = input()

if x == "RRS" or x == "SRR":
    print(2)

elif x == "RRR":
    print(3)

elif x == "RSS" or x == "SRS" or x == "SSR" or x == "RSR":
    print(1)

else:
    print(0)
