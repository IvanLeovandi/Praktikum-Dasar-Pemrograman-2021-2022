module ListOfCharacter where

-- DEFINISI DAN SPESIFIKASI LIST
{- type List of Char: [ ] atau [e o List] atau [List o e]
   Definisi type List of Char
   Basis: List of Char kosong adalah list of Char
   Rekurens: 
   List tidak kosong dibuat dengan menambahkan sebuah elemen bertype Char di awal 
   sebuah list atau
   dibuat dengan menambahkan sebuah elemen bertype Char di akhir sebuah list -}

-- DEFINISI DAN SPESIFIKASI KONSTRUKTOR
konso :: Char -> [Char] -> [Char]
{- konso e lc menghasilkan sebuah list of character dari e (sebuah character)  
   dan lc (list of integer), dengan cc sebagai elemen pertama: e o lc -> lc' -}
-- REALISASI
konso e lc = [e] ++ lc

konsDot :: [Char] -> Char -> [Char]
{- konsDot(lc,cc) menghasilkan sebuah list of character dari lc (list of 
   character) dan e (sebuah character), dengan e sebagai elemen terakhir: 
   lc o e -> lc' -}
-- REALISASI
konsDot lc e = lc ++ [e]

-- DEFINISI DAN SPESIFIKASI SELEKTOR
-- head :: [Char] -> Char
-- head l menghasilkan elemen pertama list l, l tidak kosong

-- tail :: [Char] -> [Char]
-- tail l menghasilkan list tanpa elemen pertama list l, l tidak kosong

-- last :: [Char] -> Char
-- last l  menghasilkan elemen terakhir list l, l tidak kosong

-- init :: [Char] -> [Char]
-- init(l) menghasilkan list tanpa elemen terakhir list l, l tidak kosong

-- DEFINISI DAN SPESIFIKASI PREDIKAT
isEmpty :: [Char] -> Bool
-- isEmpty l true jika list of character l kosong
-- REALISASI
isEmpty l = null l

isOneElmt :: [Char] -> Bool
-- isOneElmt l true jika list of character l hanya mempunyai satu elemen
-- REALISASI
isOneElmt l = (length l) == 1

-- MENGHASILKAN LIST DENGAN ELEMEN UNIK                 makeUnique (ls)

-- DEFINISI DAN SPESIFIKASI FUNGSI
makeUnique :: [Char] -> [Char]
{-makeUnique (lc) merupakan sebuah fungsi yang menerima masukan sebuah
list of character, misalnya lc, dan menghasilkan list dengan elemen-elemen unik,
yaitu, kemunculan setiap elemen (jika tidak kosong), hanya 1.-}
-- REALISASI
makeUnique lc =
    if null lc then []
    else if last lc `notElem` init lc then konsDot (makeUnique (init lc)) (last lc)
    else makeUnique (init lc)