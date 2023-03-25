module JamTerlambat where
-- MENGHITUNG KETERLAMBATAN            jamTerlambat(j, m, d)

-- DEFINISI DAN SPESIFIKASI
jamTerlambat :: Int -> Int -> Int -> (Int,Int,Int,Bool,Int)
{-jamTerlambat(j, m, d) menerima input tiga buah bilangan integer
yang merepresentasikan jam (0..23), menit (0..59), detik (0..59). Menghasilkan
tuple yang terdiri atas selisish waktu input dalam jam, menit, detik, boolean
apakah terlambat atau tidak, dan tingkat kekecewaan penonton-}

-- REALISASI
jamTerlambat j m d = (jam,menit,detik,terlambat,kecewa) where
    jam --Mencari nilai jam
        | j == 8 = 0
        | otherwise = (abs((8*3600 + 30*60) - (j*3600 + m*60 + d))) `div` 3600  
        
    menit = ((abs((8*3600 + 30*60) - (j*3600 + m*60 + d))) `mod` 3600) `div` 60 -- Mencari nilai menit

    detik = ((abs((8*3600 + 30*60) - (j*3600 + m*60 + d))) `mod` 3600) `mod` 60 -- Mencari nilai detik 

    terlambat -- Mencari nilai Boolean terlambat (False or True)
        | ((8*3600 + 30*60) - (j*3600 + m*60 + d)) < 0 = True 
        | otherwise = False 
        
    kecewa 
        | ((8*3600 + 30*60) - (j*3600 + m*60 + d)) < 0 = abs((8*3600 + 30*60) - (j*3600 + m*60 + d)) * 10 
        | otherwise = 0
