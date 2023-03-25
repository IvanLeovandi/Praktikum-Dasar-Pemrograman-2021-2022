module HitungIndeks where
-- MENGHITUNG INDEKS MAHASISWA            hitungIndeks(nilaiUTS, nilaiUAS, nilaiTubes)

-- DEFINISI DAN SPESIFIKASI
hitungIndeks :: Float -> Float -> Float -> Int
{-hitungIndeks(nilaiUTS, nilaiUAS, nilaiTubes) menerima 3 input bertipe float
yaitu (berturut-turut) nilaiUTS, nilaiUAS, dan nilaiTubes. Fungsi akan mengeluarkan
indeks mahasiswa (dinotasikan dengan bilangan bulat.-}

-- REALISASI
hitungIndeks nilaiUTS nilaiUAS nilaiTubes
    | nilaiUTS == 0 || nilaiUAS == 0 || nilaiTubes == 0 = 0
    | nilaiUTS < 40 || nilaiUAS < 40 = 1
    | nilaiUTS >= 75 && nilaiUAS >= 75 && nilaiTubes >= 75 = 4
    | (nilaiUTS < 75 && nilaiUTS > 40) && (nilaiUAS < 75 && nilaiUAS > 40) && (nilaiTubes < 75 && nilaiTubes > 40) = 2
    | nilaiTubes < 40 && nilaiUTS >= 40 && nilaiUAS >= 40 = 2
    | nilaiUTS >= 75 || nilaiUAS >= 75 || nilaiTubes >= 75 = 3
