# Program GambarSegitiga
# Input: N : integer
# Output: Jika N > 0 dan ganjil, gambar segitiga sesuai dengan N
#         Jika tidak, tampilkan pesan kesalahan: 

# KAMUS
# Variabel
#    N : int

def GambarSegitiga(N):
# I.S. N > 0 dan N ganjil
# F.S. Gambar segitiga dengan tinggi sebesar N sesuai spesifikasi soal
# Lengkapilah kamus lokal dan algoritma prosedur di bawah ini

    # KAMUS LOKAL
    # awal, akhir, i, j : int
    
    # ALGORITMA
    awal = (N//2) + 1
    akhir = (N//2)
    
    for i in range(awal): # melakukan print untuk segitiga bagian atas
        print(" " * ((awal - i - 1) * 2) + "*" * ((i+1)*2 - 1) )
    for j in range(akhir): # melakukan print untuk segitiga bagian bawah
        print(" " * ((j+1)*2) + "*" * (N - ((j+1)*2)))
    
def IsValid(N):
# menghasilkan true jika N positif dan ganjil, false jika tidak
# Lengkapilah kamus lokal dan algoritma fungsi di bawah ini

    # KAMUS LOKAL
    # N : int

    # ALGORITMA
    if (N > 0) and (N % 2 == 1):
        return True
    else:
        return False

# ALGORITMA PROGRAM UTAMA
N = int(input())
if IsValid(N):              # lengkapi dengan pemanggilan fungsi IsValid
    GambarSegitiga(N)       # lengkapi dengan pemanggilan prosedur GambarSegitiga
else: # N tidak positif atau N tidak ganjil
    print("Masukan tidak valid")