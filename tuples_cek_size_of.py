#CEK SIZE TIPE DATA (LIST/TUPLE)
import sys      # <-- Untuk Import Sistem dari yang sudah ada pada Phyton

data_list = [1,2,3,4,5, "Mobil","Motor","Sepeda",False,3.14]
data_tuple = (1,2,3,4,5, "Mobil","Motor","Sepeda",False,3.14)

besar_dataList = sys.getsizeof(data_list)   # <-- (getsizeof) untuk mengetahui besaran jumlah tipedata (List/Tuple)
besar_dataTuple = sys.getsizeof(data_tuple)

print("Besar dari Data List: ", besar_dataList)
print("Besar dari Data Tuple: ", besar_dataTuple)

print(" ")
#=================================================================================================================
print(150*"=")
print(" ")

#CEK TIME PROSES TIPE DATA (LIST/TUPLE)
import timeit

data_list2 = timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9]", number=1000000)
data_tuple2 = timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9)", number=1000000)

print("Waktu untuk memproses Tipe Data List: ", data_list2)
print("Waktu untuk memproses Tipe Data Tuple: ", data_tuple2)

print(" ")
#=================================================================================================================
print(150*"=")
print(" ")


#NOTE
# DENGAN MENGGUNAKAN DATA TUPLE, ITU DAPAT LEBIH MERINGANKAN
# KETIMBANG MENGGUNAKAN TIPE DATA LIST DALAM PHYTON, DIKARENAKAN
# DIDALAM TIPE DATA TUPLE ATTRIBUTE-NYA LEBIH SEDIKIT.
#
# PERBEDAAN TIPE DATA LIST & TUPLE ADALAH:
# LIST = NILAI/VALUE DIDALAM ARRAY DAPAT DIRUBAH ATAU DIMANIPULASI
#         DENGAN MENGGUNAKAN BEBERAPA ATTRIBUT SEPERTI (append,extend,insert,remove, dll)
#
# TUPLE = SEDANGKAN TUPLE, NILAI DIDALAM ARRAY ITU TIDAK DAPAT DIRUBAH-RUBAH NILAI/VALUENYA,
#         DAN NILAI/VALUE PADA TUPLE MEMANG DI RENCANG UNTUK NILAI YANG FIX/TETAP YANG TIDAK
#         AKAN DIRUBAH RUBAH NANTI KEDEPANNYA.
