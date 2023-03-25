# PROGRAM Berat
# Sebuah program yang digunakan untuk membaca masukan berat tubuh manusia
# sampai pengguna mengetikkan -999. Nilai masukan harus berada dalam range 30-200
# Jika data nilai salah maka data tersebut diabaikan. Program akan menuliskan berapa banyak
# mahasiswa keseluruhan, berapa mahasiswa dengan berat <= 50, berapa banyak mahasiswa dengan berat >= 100
# dan berapa rata-rata berat mahasiswa.

# KAMUS
# berat, count, under50, gtThan100, total = int

# REALISASI
berat = int(input())

if berat == -999:
    print("Data kosong")
else:
    count = 0
    under50 = 0
    gtThan100 = 0
    total = 0
    while berat != -999:
        if berat >= 30 and berat <= 200:
            count += 1
            total += berat
            if berat <= 50:
                under50 += 1
            elif berat >= 100:
                gtThan100 += 1
        berat = int(input())
    if count == 0:
        print("Data kosong")
    else:
        print(count)
        print(under50)
        print(gtThan100)
        print(round(total/count))
