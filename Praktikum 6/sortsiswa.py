# Program SortSiswa
# Spesifikasi : ....
import tulisdata

# KAMUS
# namafile: string

def insertionSort(arr):
    # sebuah fungsi yang mengurutkan array dengan pendekatan insertion sort
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1
        while j >= 0 and temp[0] < arr[j][0]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
            
# ALGORITMA PROGRAM UTAMA
namafile = input()
tulisdata.TulisDataSiswa(namafile)

f = open(namafile,'r')
arr = []

baris1 = f.readline()
if baris1 == "99999999":
    print("File kosong")
else:
    while baris1 != "99999999":
        baris2 = f.readline()
        baris3 = f.readline()
        data_siswa = (int(baris1),baris2,int(baris3))
        arr.append(data_siswa)
        baris1 = f.readline()

    insertionSort(arr)
    for i in range(len(arr)):
        print(arr[i][0], end=",")
        print(arr[i][1].rstrip(),end=",")
        print(arr[i][2])

f.close()