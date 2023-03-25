module HitungBensin where
-- MENGHITUNG BENSIN            hitungBensin(a,b)

-- DEFINISI DAN SPESIFIKASI
hitungBensin :: Int -> Int -> Int
hitungPerjalanan :: Int -> Int
{-hitungBensin(a,b) menerima menerima 2 buah bilangan bulat, A dan B dengan (A <= B)
dan kemudian mengeluarkan sebuah bilangan bulat yang menunjukkan konsumsi bensin
dari tiap-tiap kendaraan dari A sampai B.-}

-- REALISASI
hitungPerjalanan x
    |x == 1 = 0
    |x `mod` 2 == 0 = 1 + hitungPerjalanan (x `div` 2)
    |otherwise = 1 + hitungPerjalanan (3*x + 1)

hitungBensin a b
    |a == b = hitungPerjalanan a
    |otherwise = hitungPerjalanan b + hitungBensin a (b-1)