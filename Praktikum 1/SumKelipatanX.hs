module SumKelipatanX where
-- SUM KELIPATAN X            sumKelipatanX(m, n, x)

-- DEFINISI DAN SPESIFIKASI
sumKelipatanX :: Int -> Int -> Int -> Int
{-sumKelipatanX(m, n, x) menghasilkan jumlah total bilangan kelipatan x di antara
m dan n (m dan n termasuk) dengan menggunakan ekspresi rekursif.-}

-- REALISASI
sumKelipatanX m n x
    | m > n = 0
    | (n `mod` x /= 0) && (n >= m) = sumKelipatanX m (n-1) x
    | (n `mod` x == 0) && (n >= m) = n + sumKelipatanX m (n-1) x