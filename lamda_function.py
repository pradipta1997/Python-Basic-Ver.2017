#MENGGUNAKAN FUNCTION DEF
def jumlah(x,y):
    z= x+y
    print(x, '+', y, '=', z)
    return z

hasil=jumlah(5,5)
print('Hasil Return Value',hasil)

#===============BATAS===================
print("="*30)


#MENGGUNAKAN FUNCTION LAMDA
Kali = lambda x,y: x*y                   #Function LAMDA ialah syntax versi simple dari function DEF
hasil = Kali(25,5)
print("Hasil dari perkalian menggunakan LAMDA -> ",hasil)