module ListOfInteger where
-- DEFINISI DAN SPESIFIKASI LIST
{- type List of Int: [ ] atau [e o List] atau [List o e]  
   Definisi type List of Int
   Basis: List of Int kosong adalah list of Int 
   Rekurens: 
   List tidak kosong dibuat dengan menambahkan sebuah elemen bertype Int di awal 
   sebuah list atau
   dibuat dengan menambahkan sebuah elemen bertype Int di akhir sebuah list -}

-- DEFINISI DAN SPESIFIKASI KONSTRUKTOR
konso :: Int -> [Int] -> [Int]
{- konso e li menghasilkan sebuah list of integer dari e (sebuah integer) dan li 
   (list of integer), dengan e sebagai elemen pertama: e o li -> li' -}
-- REALISASI
konso e li = [e] ++ li

konsDot :: [Int] -> Int -> [Int]
{- konsDot li e menghasilkan sebuah list of integer dari li (list of integer) dan 
   e (sebuah integer), dengan e sebagai elemen terakhir: li o e -> li' -}
-- REALISASI
konsDot li e = li ++ [e]

-- DEFINISI DAN SPESIFIKASI SELEKTOR
-- head :: [Int] -> Int
-- head l menghasilkan elemen pertama list l, l tidak kosong

-- tail :: [Int] -> [Int]
-- tail l menghasilkan list tanpa elemen pertama list l, l tidak kosong

-- last :: [Int] -> Int
-- last l menghasilkan elemen terakhir list l, l tidak kosong

-- init :: [Int] -> [Int]
-- init l menghasilkan list tanpa elemen terakhir list l, l tidak kosong

-- DEFINISI DAN SPESIFIKASI PREDIKAT
isEmpty :: [Int] -> Bool
-- isEmpty l  true jika list of integer l kosong
-- REALISASI
isEmpty l = null l

isOneElmt :: [Int] -> Bool
-- isOneElmt l true jika list of integer l hanya mempunyai satu elemen
-- REALISASI
isOneElmt l = (length l) == 1 

-- ELEMEN KE N                      elmtKeN(l,n)
-- DEFINISI DAN SPESIFIKASI
elmtKeN :: [Int] -> Int -> Int 
{-ElmtKeN (l,n) merupakan sebuah fungsi yang menerima masukan sebuah
list of integer dan sebuah integer dan menghasilkan elemen ke-n dari list
of integer tersebut.-}
-- Asumsi : 0<n<=banyaknya elemen l dan list tidak kosong

-- REALISASI
elmtKeN l n =
    if n == 1 then head l
    else elmtKeN (tail l) (n-1)

-- ELEMEN L1 YANG TIDAK ADA DI L2                       setDiff(l1,l2)
setDiff :: [Int] -> [Int] -> [Int]
{-setDiff(l1,l2) merupakan sebuah fungsi yang menerima masukan dua buah list of integer (l1 dan l2)
dengan elemen unik dan terurut membesar dan mengembalikan sebuah list of integer yang elemennya 
adalah semua elemen l1 yang tidak ada di l2.-}
isElmt :: Int -> [Int] -> Bool 
{-isElmt (n,l) merupakan sebuah fungsi yang memeriksa apakah sebuah angka berada dalam list-}

-- REALISASI
isElmt n l =
   if null l then False 
   else if n == head l then True 
   else isElmt n (tail l)

setDiff l1 l2 =
    if null l1 then []
    else if not (isElmt (head l1) l2) then konso (head l1) (setDiff (tail l1) l2)
    else setDiff (tail l1) (l2)
