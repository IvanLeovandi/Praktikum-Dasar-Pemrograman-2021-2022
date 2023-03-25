# Program RataRataSiswa
# Spesifikasi : ....
import tulisdata

# KAMUS
# namafile: string 

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

    arr.sort(key=lambda tup: tup[0])
    arr.append("mark")
    i = 0
    while arr[i] != "mark":
        currNim = arr[i][0]
        currSum = 0
        currCount = 0
        while True:
            currSum += arr[i][2]
            currCount += 1
            i += 1
            if currNim != arr[i][0]:
                break
        rata = currSum/currCount
        print(str(currNim) + "=" + "%.2f" % rata)

f.close()