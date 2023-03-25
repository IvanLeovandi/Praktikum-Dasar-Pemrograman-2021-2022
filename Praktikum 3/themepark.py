t = int(input())
b = int(input())
k = int(input())

def cek(li, k):
    for a in li:
        if a == k:
            return "TRUE"
    return "FALSE"
    
if t > 100 and b <= 150:
        li = [2, 3, 4]
elif t <= 100 and b <= 150:
    if b > 30:
        li = [1, 2]
    else:
        li = [1]
elif b > 150:
    if t <= 100:
        li = [2]
    elif 100 < t <= 200:
        li = [2, 3]
    else:
        li = [0]
else:
    li = [0]

print(cek(li, k))
