#TEKNIK LOOPING MENGGUNAKAN BEBERAPA METODE/FUNCTION

Nama_Band = ['Bring Me The Horizon',        #Data utama
             'My Chemical Romance',
             '30 Second to Mars',
             'One Ok Rock',
             'Linkin Park']

Kumpulan_Lagu = ['Parasite Eve',            #Data utama
                 'Black Parade',
                 'Kill Me',
                 'Heartache',
                 'Numb']

#====================================================================================================

#ENUMERATE FUNCTION
for index,Band in enumerate(Nama_Band):     # <--Tidak bisa lebih dari 2 variable
    print(index,":",Band)

# Fungsi enumerate() mengembalikan nilai berupa objek enumerate.
# Objek enumerate sendiri merupakan objek iterable yang tiap itemnya
# berpasangan dengan indeks atau angka yang mewakilinya. Dengan kata
# lain fungsi ini akan menambahkan penghitung (indeks) ke objek iterable
# dan mengembalikannya.


print(80*"=")
print(" ")
#====================================================================================================

#ZIP FUNCTION
for Band,Lagu in zip(Nama_Band,Kumpulan_Lagu):      # <--Tidak bisa lebih dari 2 variable
    print(Band,"Membawa Lagu Berjudul: ",Lagu)

# Fungsi function zip() disini adalah
# untuk menggabungkan dua buah variable
# yang memiliki data yang berbeda menjadi
# kedalam satu output yang bersamaan.


print(80*"=")
print(" ")
#====================================================================================================

#SORTED FUNCTION
Playlist_Lagu = {'Rock',
                 'Screamo',
                 'Alternative Rock',
                 'Pop'
                 }

for Daftar in sorted(Playlist_Lagu):
    print(Daftar)

#NOTE
# sorted() berfungsi untuk mengurutkan
# values A-Z (Ascending)


print(80*"=")
print(" ")
#====================================================================================================


#DICTIOARY
Playlist_Lagu2 = {'Metalica': 'Enter Sandman',
                  'Avenged Sevenfold': 'Dear God',
                  'The Red Jump Suit': 'Face Down'}

for i,v in Playlist_Lagu2.items():
    print(i, "Lagunya: ",v)