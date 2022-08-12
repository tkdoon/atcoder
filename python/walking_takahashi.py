import math
x, k, d = map(int, input().split())
x = abs(x)
# math.floor(x/d)+1回!absの方向に行く
# k>x/dのときx-math.floor(x/d)*dとx-(math.floor(x/d)+1)*dのうち小さいほうが答え
if k > x/d:
    if (k-math.floor(x/d)) % 2 == 0:
        print(abs(x-math.floor(x/d)*d))

# ここがちがうよ
    else:
        print(abs(x-math.floor(x/d+1)*d))
#     if x-math.floor(x/d)*d < abs(x-(math.floor(x/d)+1)*d):
#         print(x-math.floor(x/d)*d)
#     else:
#         print(abs(x-(math.floor(x/d)+1)*d))
else:
    print(x-k*d)
