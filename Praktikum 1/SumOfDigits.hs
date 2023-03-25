module SumOfDigits where
-- SUM OF DIGITS            sumOfDigits(n)

-- DEFINISI DAN SPESIFIKASI
sumOfDigits :: Int-> Int
{-sumOfDigits(n) menghitung hasil penjumlahan dari setiap bilangan tunggal
yang terdapat di dalam sebuah bilangan integer positif atau 0-}

-- REALISASI
sumOfDigits n 
    | n < 1 = 0                                         -- Basis
    | otherwise = n `mod` 10 + sumOfDigits(n`div`10)    -- Rekurens 