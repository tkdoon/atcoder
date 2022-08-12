s = input()
t = input()
max_length = 0
# for i in range(len(t)):
#     for j in range(i, len(s)):
#         if t[i] == s[j]:
#             length = 0
#             for k in range(min(len(t)-i, len(s)-j)):
#                 if t[i+k] == s[j+k]:
#                     length += 1
#             for l in range(1, i+1):
#                 if t[i-l] == s[j-l]:
#                     length += 1
#             if length > max_length:
#                 max_length = length
# print(len(t)-max_length)
# for i in range(len(t)):
#     for j in range(i+1, len(t)):
#         t_part = t[i:j]
#         if (t_part in s[i:] and j-i > max_length):
#             max_length = j-i

for i in range(len(s)-len(t)):
    length = 0
    for j in range(len(t)):
        if s[j+i] == t[j]:
            length += 1
    if max_length < length:
        max_length = length
print(len(t)-max_length)
#   あってると思ったけどな
