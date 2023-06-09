# Program EmpatInteger
# Input: 4 integer: A, B, C, D
# Output: Sifat integer dari A, B, C, D (positif/negatif/nol) 
#         Jika semua integer positif, tampilkan:
#         nilai maksimum, minimum, dan mean olympic
 
# KAMUS
# variabel
#    A, B, C, D : int
#    mo : real
 
# PROCEDURE DAN FUNCTION
def CekInteger (x):
# I.S.: x terdefinisi, bertype int
# F.S.: Jika x positif, maka tertulis di layar: POSITIF
#       Jika x negatif, maka tertulis di layar: NEGATIF
#       Jika x nol, maka tertulis di layar: NOL
# Tuliskan realisasi prosedur CekInteger di bawah ini

    # KAMUS LOKAL
    # x : int
    
    # ALGORITMA
    if x > 0:
        print("POSITIF")
    elif x < 0:
        print("NEGATIF")
    else: # x == 0
        print("NOL")          
                       
def Max (A, B, C, D):
# menghasilkan nilai terbesar di antara a, b, c, d (integer)
# Tuliskan realisasi fungsi Max di bawah ini

    # KAMUS LOKAL
    # max = int
    
    # ALGORITMA
    max = A
    
    if max < B:
        max = B
    if max < C:
        max = C
    if max < D:
        max = D
    
    return max
            
def Min (A, B, C, D):
# menghasilkan nilai terkecil di antara a, b, c, d (integer)
# Tuliskan realisasi fungsi Min di bawah ini

    # KAMUS
    # min : int
    
    # ALGORITMA
    min = A
    
    if min > B:
        min = B
    if min > C:
        min = C
    if min > D:
        min = D
        
    return min

def IsAllPositif (A, B, C, D):
# menghasilkan true jika a, b, c, d seluruhnya positif
# false jika tidak
# Tuliskan realisasi fungsi IsAllPositif di bawah ini
    
    # ALGORITMA
    if (A > 0) and (B > 0) and (C > 0) and (D > 0):
        return True
    else:
        return False
            
# PROGRAM UTAMA
# Tidak boleh diubah-ubah
# Input
A = int(input())
B = int(input())
C = int(input())
D = int(input())

# Menuliskan sifat integer
CekInteger(A)
CekInteger(B)
CekInteger(C)
CekInteger(D)

# Penulisan maksimum, minimum, dan mean olympic
if (IsAllPositif(A,B,C,D)):
    print(Max(A,B,C,D))
    print(Min(A,B,C,D))
    mo = (A + B + C + D - Max(A,B,C,D) - Min(A,B,C,D)) / 2
    print("%.2f" % mo)