#LIST SEBAGAI ITERABLE
Mobil = ["Toyota","Hyundai","Nissan","Honda","Proton","Daihatsu","Jeep","Suzuki","Mitsubishi","KIA","Ford"]

for m in Mobil:
    print(m)
    print(len(m))

#------------------------------------------------------
print(60 * "-")
print(" ")

#STRING SEBAGAI ITERABLE
Mobil = "Toyota"

for i in Mobil:
    print(i)

#------------------------------------------------------
print(60 * "-")
print(" ")

#FOR DIDALAM FOR
FireArm = ["SS-2 Pindad","AK-47","M-16","Glock17","AW50","Uzi","Lee Enfield"]
Country = ["Indonesia","Rusia","USA","Austria","Jerman","Israel","Inggris"]

Daftar_List = [FireArm, Country]

for SubDaftarList in Daftar_List:       #Untuk meng-loop layer pertama (perlist)
    print(SubDaftarList)

    for Komponen in SubDaftarList:      #Untuk meng-loop layer kedua (pernama dari isi list)
        print(Komponen)

        for Karakter in Komponen:       #Untuk meng-loop layer ketiga (perkarakternya)
            print(Karakter)