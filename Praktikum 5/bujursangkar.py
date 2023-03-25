# PROGRAM Luas Bujur Sangkar
# Sebuah program yang digunakan untuk menghitung luas bujur sangkar. 
# Program menerima input sisi (int) > 0. Jika nilainya tidak valid maka program akan
# mengeluarkan pesan error

# KAMUS
# s, luas = int

# REALISASI

s = int(input())
if s <= 0:
    print('Sisi harus > 0')
else:
    luas = s*s
    print(luas)