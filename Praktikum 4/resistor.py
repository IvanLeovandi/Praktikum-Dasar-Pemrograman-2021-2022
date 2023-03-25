# Program Resistor
# menghitung total resistor pada sebuah rangkaian

# KAMUS
# R1,R2,R3,RT = float
# jenis = char
# repeat, kondisi = bool

# FUNGSI DAN PROSEDUR
def validasi (R1,R2,R3,jenis):
# sebuah fungsi yang memvalidasi inputan dari user

    # KAMUS LOKAL
    # kondisi = bool
    # listBenar = array of char
    kondisi = True
    listBenar = ['s','S','p','P']
    if (R1 <= 0) or (R2 <= 0) or (R3 <= 0) :
        kondisi = False
    if jenis not in listBenar:
        kondisi = False
    
    if not kondisi:
        print('Masukan salah')
        return False
    else:
        return True

def rtotal (R1,R2,R3,jenis):
# sebuah fungsi yang menghitung nilai resistor total dengan menampilkan hanya 2 desimal
    
    # KAMUS LOKAL
    # RT = float

    if (jenis == 's') or (jenis == 'S'):
        RT = R1 + R2 + R3
        return ("%.2f" % RT)
    else:
        RT = 1/((1/R1) + (1/R2) + (1/R3))
        return ("%.2f" % RT)

# ALGORITMA
repeat = False
while not repeat:
    R1 = float(input())
    R2 = float(input())
    R3 = float(input())
    jenis = input()

    repeat = validasi(R1,R2,R3,jenis)

print(rtotal(R1,R2,R3,jenis))
