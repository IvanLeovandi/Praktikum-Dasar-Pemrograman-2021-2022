# PROGRAM Cari Character
# sebuah program yang digunakan untuk membaca sebuah integer positif N dengan range 0<N<=100.
# Jika nilai N salah makan program menuliskan pesan kesalahan. Selanjutnya program menerima masukan
# sebuah character CC dan menghasilkan output sesuai ketentuan.

# KAMUS
# array = array of char
# N, i = int
# CC = char
# foundKecil, foundBesar, foundSimbol = bool

# REALISASI

N = int(input())

while N <= 0 or N > 100:
    print('Masukan salah. Ulangi!')
    N = int(input())

array = ["*" for i in range(N)]

foundKecil = False
foundBesar = False
foundSimbol = False

for i in range(N):
    masukan = input()
    array[i] = masukan
    if (ord(masukan) >= 97) and (ord(masukan) <= 122) and (not foundKecil):
        foundKecil = True
        kecil = i
    if (ord(masukan) >= 65) and (ord(masukan) <= 90) and (not foundBesar):
        foundBesar = True
        besar = i
    if ((not (ord(masukan) >= 65 and ord(masukan) <= 90)) and (not (ord(masukan) >= 97 and ord(masukan) <= 122))) and (not foundSimbol):    
        foundSimbol = True
        simbol = i

CC = input()

if (CC == 'S') or (CC == 's'):
    if foundKecil:
        print(kecil+1, array[kecil])
    else:
        print("Tidak ada huruf kecil")
elif (CC == 'L') or (CC == 'l'):
    if foundBesar:
        print(besar+1,array[besar])
    else:
        print("Tidak ada huruf besar")
elif (CC == 'X') or (CC == 'x'):
    if foundSimbol:
        print(simbol+1, array[simbol])
    else:
        print("Semua huruf")
else:
    print("Tidak diproses")