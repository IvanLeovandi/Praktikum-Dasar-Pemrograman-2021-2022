# PROGRAM Barang
# sebuah program yang menghitung jumlah harga barang yang dibeli di minimarket sebanyak N

# KAMUS
# N, i, sum = int

# REALISASI
N = int(input())
sum = 0
for i in range(N):
    harga = int(input())
    sum = sum + harga

print(sum)