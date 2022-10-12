#LIST ARRAY
Barang = ['Kunci','Komputer','Motor','Mobil','Meja','Jam','Buku']
print(Barang)

#BEBERAPA METHOD YANG BISA DIGUNAKAN UNTUK MEMANIPULASI LIST
#METHOD UNTUK MENAMBAH DATA KEDALAM LIST
Barang.append('Sepeda') #Untuk menambah value/string kedalam list
print(Barang)

Barang.extend('Jarum')  #Untuk menambah value/string secara terpisah perhuruf
print(Barang)

Barang.insert(3,'Sepeda')   #Untuk insert value di array yang ditentukan
print(Barang)


#========================================================================================
print(100*'-')

#METHOD UNTUK MENGHITUNG ANGGOTA/JUMLAH VALUE
jumlahSepeda = Barang.count('Sepeda')           #Untuk menghitung jumlah value ada berapa didalam array
print('Jumlah Value Sepeda didalam Array: ', jumlahSepeda)

#========================================================================================
print(100*'-')

#REMOVE DATA VALUE
Barang.remove('Sepeda') #Untuk menghapus data value didalam array
print(Barang)

#========================================================================================
print(100*'-')

#REVERSE DATA VALUE
Barang.reverse()    #Untuk membalik data value didalam array
print(Barang)

#========================================================================================
print(100*'-')

Stuff = Barang.copy()   #Untuk Copy variable barang, agar value tidak terinsert seperti pada variable Stuff
Stuff.append('Gelas')
print(Stuff)
print(Barang)


