# PROGRAM Nilai
# sebuah program yang menerima masukan sejumlah nilai mahasiswa secara terus menerus hingga
# pengguna mengetikkan -9999. Jika masukan berada diluar range 0-100 maka data diabaikan.
# Program akan menuliskan banyak mahasiswa keseluruhan, banyak yang lulus, banyak yang tidak lulus,
# dan rata-rata nilai dengan 2 angka di belakang koma.

# KAMUS
# nilai, count, lulus, tidakLulus, total = int

# REALISASI
nilai = int(input())

if nilai == -9999:
    print("Data nilai kosong")
else:
    count = 0
    lulus = 0
    tidakLulus = 0
    total = 0
    while nilai != -9999:
        if nilai >= 0 and nilai <= 100:
            count += 1
            total += nilai
            if nilai >= 40:
                lulus += 1
            else:
                tidakLulus += 1
        nilai = int(input())
    if count == 0:
        print(0)
    else:
        print(count)
        print(lulus)
        print(tidakLulus)
        rata = total/count
        print("%.2f" % rata)
