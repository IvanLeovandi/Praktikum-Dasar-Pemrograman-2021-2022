# PROGRAM LUAS SEGITIGA
# sebuah program yang menghitung luas segitiga yang menerima input alas dan tinggi.
# Input akan terus divalidasi, jika input salah maka akan ditampilkan pesan error.

# KAMUS
# a, t = int
# luas = float

# REALISASI

alas, tinggi = map(int, input().split())

if alas > 0 and tinggi > 0:
    luas = round(0.5 * alas * tinggi)
    print(luas)
else:
    print("Alas dan tinggi harus > 0")