module ListIndex where

-- LIST INDEX                           listIndex(l,f)
-- DEFINISI DAN SPESIFIKASI
listIndex :: [Int] -> (Int -> Char) -> [Char]

konso :: Char -> [Char] -> [Char]
{-konso (e, lc) merupakan sebuah fungsi yang menghasilkan sebuah list of character
dari e (sebuah karakter) dan lc (list of char), dengan e sebagai elemen pertama-}
-- REALISASI
index n =
    if n >= 80 then 'A'
    else if n >= 70 && n < 80 then 'B'
    else if n >= 65 && n < 70 then 'C'
    else if n >= 55 && n < 65 then 'D'
    else 'E'

konso e lc = [e] ++ lc

listIndex l f =
    if null l then []
    else konso (f (head l)) (listIndex (tail l) f)