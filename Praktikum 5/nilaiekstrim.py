N = int(input())
T = [0 for i in range (N)]

for i in range(N):
    T[i] = int(input())

max = T[0]
min = T[0]
for i in range(1,N):
    if max < T[i]:
        max = T[i]
    elif min > T[i]:
        min = T[i]

X = int(input())
kondisi = False
for i in range(N):
    if X == T[i]:
        kondisi = True

if kondisi == True:
    if X == max and max == min:
        print('maksimum')
        print('minimum')
    elif X == max:
        print('maksimum')
    elif X == min:
        print('minimum')
    else:
        print('N#A')
else:
    print(X,'tidak ada')
        
