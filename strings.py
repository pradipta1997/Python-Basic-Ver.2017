text1 = 'Hallo My Name is Pradipta Ramadhan'
text2 = 'jalan-jalan di hari jum\'at' #<-- [\] untuk "Not" pemisah jika ada lebih dari 2 koma
text3 = 'Pradipta berkata, "Mau kemana hari ini?"' # [""] untuk membuat tanda kutip dialog didalam string
text4 = "Hasna Menjawab, \"Jalan-jalan jauh\"" #Untuk membuat kutip dua didalam kutip dua dengan [\]
text5 = """
A: Mau kemana ?
B: Mau jalan - jalan.
A: Jalan- jalan kemana ?
B: Ke Manchester. """    #Untuk penggunaan Kalimat Dialog pada string

print(text5)
print(text3 + text4) #Untuk menyambung string dengan satu output
print(10 * "Pradipta ") #Penjumlahan jumlah string

print(45 * "-" + "Batas" + 50 * "-") #Batas Code

text0 = "Pradipta Ramadhan"
var = text0[5] #Untuk Mengambil huruf tertentu
print(var)

text00 = "Pradipta Ramadhan"
var = text00[0:8] #Untuk Mengambil huruf awal - akhir
print(var)

text000 = "Pradipta Ramadhan"
var = text000[-8] #Untuk Mengambil huruf dari kalimat akhir
print(var)

