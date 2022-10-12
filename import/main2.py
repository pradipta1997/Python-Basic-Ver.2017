#INI ADALAH CARA UNTUK MENGAKSES
# MODULE DENGAN CARA IMPORT

#IMPORT MODULE DENGAN CARA PERTAMA
import matematika

matematika.tambah(20,30)
matematika.kurang(80,40)

#=======================================

#IMPORT MODULE DENGAN CARA KEDUA, DENGAN ALISAN (as)
import matematika as Math

Math.tambah(20,10)
Math.kurang(20,10)

#=======================================

#IMPORT MODULE DENGAN CARA KETIGA, SPESIFIK
from matematika import tambah, kurang
from matematika import *              # <-- Ini untuk mengambil semua function dari semua module matematika

tambah(1,1)
kurang(2,1)

#=======================================

from matematika import tambah as t

t(100,200)