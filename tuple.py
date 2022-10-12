#LIST
Ganjil = [1,3,5,7,9]    #Ini adalah type data List

#TUPLE
Genap = (2,4,6,8,10)    #Ini adalah type data Tuple

print(type(Ganjil))     # <-- (Type) adalah function untuk cek tipe data dari variable yang digunakan
print(type(Genap))      # <-- (Type) adalah function untuk cek tipe data dari variable yang digunakan
print(" ")
print(dir(Ganjil))      # <-- (dir) adalah function untuk Attribute apa saja yang ada dalam (List/Tuple)
print(dir(Genap))       # <-- (dir) adalah function untuk Attribute apa saja yang ada dalam (List/Tuple)
print(" ")

print(Genap.index(8))
print(" ")

print('Ini adalah List -->',Ganjil)
print('Ini adalah Tuple -->',Genap)