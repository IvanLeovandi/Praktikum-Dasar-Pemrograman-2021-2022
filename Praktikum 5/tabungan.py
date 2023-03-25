# PROGRAM Tabungan
# Sebuah program yang menghitung jumlah tabungan sebanyak N dengan N berasal dari masukan user

# KAMUS
# N, i = int

# REALISASI
N = int(input())
sum = 0
for i in range(N):
    uang = int(input())
    sum = sum + uang

print(sum)