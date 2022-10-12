Data = [1,4,9,16,25,36,49,64]
Data2 = [100,200,300,400,500,600,700,800,900]

#MENGAKSES/MENGAMBIL LINK
Subdata1 = Data[3]                              # <-- Mengambil data dengan urut ke-3
Subdata2 = Data[-3]                             # <-- Mengambil data dengan urut ke-3 dari belakang

#MEMOTONG LIST
Subdata3 = Data[2:4]                            # <-- Mengambil data dari urut ke-2 sampai ke-4
Subdata4 = Data[:4]                             # <-- Mengambil data dari awal sampai ke no urut ke-4

#MENAMBAH LIST
Subdata5 = Data + Data2                         # <-- Menambah data1 dengan data2

#MERUBAH CONTENT DARI LIST
Data[4] = 30                                    #  <-- Untuk merubah no urut ke4 (25) menjadi (30)

#MENGCOPY LIST KE VARIABLE BARU
a = Data[:]
a[7] = 70

#MERUBAH CONTENT LIST DENGAN MENGGUNAKAN METODE SLICING
Data[3:5] = [11,12]                             # <-- Untuk merubah angka no urut ke 3-5 dengan slicing

#LIST DALAM LIST
x = [Data,Data2]                                # <-- Untuk cetak Variable Data2 didalam list Data1

#MENGAKSES LIST DALAM MULTIDIMENSIONAL LIST
y = x[1][4]                                     # <-- Untuk mengambil data no urut ke4 di multi dimensi

#METHODS UNTUK LIST
Data.append(30)

#FUNCTION YANG BISA DIGUNAKAN KEPADA LIST
Panjang_List = len(Data)


print(Panjang_List)                             # <-- Untuk cetak Var (Panjang_List) Phyton String Function (len)
#print(y)                                       # <-- Untuk cetak Var (x)
#print(x)                                       # <-- Untuk cetak Var (x)
#print(a)                                       # <-- Untuk cetak Var (a)
print(Data)                                    # <-- Untuk cetak Var (Data)
#print(Subdata5)                                # <-- Untuk  cetak Var (Subdata)