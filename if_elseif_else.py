Nilai1 = 75
Nilai2 = 81

#NESTING IF
if Nilai1 == 75:                        #Equal
    print("Nilai Anda:", Nilai1)

    if Nilai2 == 80:
        print("Nilai Anda:", Nilai2)


if Nilai2 != 80:                        #Not Equal
    print("Nilai Anda Bukan:", Nilai2)

#----------------------------------------------------------------
print(60 * "-")

print("--OPERATOR LOGIKA NUMBERING--")
Nilai3 = 30

if 80 <= Nilai3 <= 100:
    print("Nilai anda adalah", Nilai3, "(A)")
elif 70 <= Nilai3 <= 80:
    print("Nilai anda adalah", Nilai3, "(B)")
elif 65 <= Nilai3 <= 70:
    print("Nilai anda adalah", Nilai3, "(C+)")
elif 60 <= Nilai3 <= 65:
    print("Nilai anda adalah", Nilai3, "(C)")
else:
    print("Maaf anda tidak lulus mata kuliah ini, Nilai Anda di Bawah Rata-Rata", "(", Nilai3, ")")


#----------------------------------------------------------------
print(60 * "-")

print("--OPERATOR LOGIKA UNTUK LIST & STRING")
print(" ")

Mobil = ["Toyota","Hyundai","Nissan","Honda","Proton","Daihatsu","Jeep","Suzuki","Mitsubishi","KIA","Ford"]
Beli = "Tesla"

if Beli in Mobil:
    print('Sales said: "Ya, kita menjual mobil', Beli,'"')

if not Beli in Mobil:
    print('Sales said: "Tidak, Kita tidak menjual mobil', Beli, '"' )



#----------------------------------------------------------------
print(60 * "-")