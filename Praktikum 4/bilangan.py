def cekAngka(N):
    if N <= 0 or N > 100:
        return (False)
    else:
        return (True)

def fungsi(array, X):

        if X == 0 :
            for i in range (N):
                if array[i] == 0:
                    print (str(i+1))
                    break
            else : 
                print("Tidak ada 0")
        elif X == -1:
            for i in range (N):
                if array[i] < 0:
                    print (str(i+1) + ' ' + str(array[i]))
                    break
            else : 
                print("Tidak ada negatif")
        elif X == 1:
            for i in range (N):
                if array[i] > 0:
                    print(str(i+1) + ' ' + str(array[i]))
                    break
            else : 
                print("Tidak ada positif")
        else:
            print("Tidak diproses")

N = int(input())

while (cekAngka(N) == False) :
    print('Masukan salah. Ulangi!')
    N = int(input())

array = [0 for i in range (N)]
for i in range (N):
    array[i] = int(input())

X = int(input())

fungsi(array, X)