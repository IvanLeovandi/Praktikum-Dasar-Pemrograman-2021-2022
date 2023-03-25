module AlternateSort where

-- ALTERNATE SORT                   alternateSort (l)
-- DEFINISI DAN SPESIFIKASI
sortList :: [Int] -> [Int]
tengah :: [Int]->[Int]
alternateSort :: [Int]-> [Int]
isOneElmt :: [Int] -> Bool
-- isOneElmt l true jika list of integer l hanya mempunyai satu elemen

-- REALISASI
sortList l =
    if null l then []
    else
        let
            kecil = sortList [x | x <- (tail l), x <= head l]
            besar = sortList [x | x <- (tail l), x > head l]
        in kecil ++ [head l] ++ besar

tengah l = init(tail l)

isOneElmt l = (length l) == 1 
alternateSort l =
    if null l then []
    else if isOneElmt l then [head l]
    else
        let listurut = sortList l
        in [head listurut] ++ [last listurut] ++ alternateSort (tengah listurut)