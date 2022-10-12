#SCOPE VARIABLE: LOCAL
namaKucing = 'Joteph'       #Variable global, karena berada di luar scope function tertentu

def rubahNamaKucing(namaBaru):
    namaKucing = namaBaru   #Variable local, karena berada didalam scope function tertentu
    print('Saya merubah nama kucing saya menjadi', namaKucing)

rubahNamaKucing('Lordan')   #Pengisian penamaan variable
print('Nama kucing saya menjadi:', namaKucing)



#==============================================================================================================
print('-'*50)



#SCOPE VARIABLE: GLOBAL
namaKucing2 = 'Fredi'           #Variable global, karena berada di luar scope function tertentu
namaK = 'Zamal'           #Variable global, karena berada di luar scope function tertentu
makananK = 'Royal Canin'   #Variable global, karena berada di luar scope function tertentu

def rubahNamaKucing(namaBaru):
    global namaKucing2       #Untuk membuat variable local pada function tertentu menjadi variable glbal (global)
    namaKucing2 = namaBaru   #Variable local, karena berada didalam scope function tertentu
    print('Saya merubah nama kucing saya menjadi', namaKucing2)

rubahNamaKucing('Soap')         #Pengisian penamaan variable


def kasihMakanKucing(nama,makanan):
    global namaK,makananK
    namaKucing = nama
    makananKucing = makanan
    print('Nama Kucing saya', namaKucing, 'dan makanannya', makananKucing) #Cetak perintah variable local

kasihMakanKucing('Alex','Wiskash')   #Pengisian penamaan variable


print('Nama kucing saya', namaK, 'dan makanannya', makananK) #Cetak perintah variable global


#==============================================================================================================
print('-'*50)