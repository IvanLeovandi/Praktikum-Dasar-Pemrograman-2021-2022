module KonversiSuhu where
-- KONVERSI SUHU            konversiSuhu(t, k)

-- DEFINISI DAN SPESIFIKASI
konversiSuhu :: Float -> Char -> Float
{-konversiSuhu(t, k) menerima masukan 2 buah masukkan, yaitu 1 buah nilai bertipe
real (float) yang merupakan besaran suhu dalam derajat Celcius dan 1 buah kode satuan
suhu konversi. Fungsi ini digunakan untuk mengkonversi suhu dari satu satuan Celcius
ke satuan suhu yang lain, yaitu Fahrenheit, Reamur, atau Kelvin.-}

-- REALISASI
konversiSuhu t k
    | k == 'R' = 4 / 5 * t
    | k == 'F' = (9 / 5 * t) + 32
    | k == 'K' = t + 273.15