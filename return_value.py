#FUNCTION WITH RETURN VALUE
def Kuadrat(argument):
    total=argument**2
    print("Nilai kuadrat dari",argument,"adalah",total)
    return total                                            #Untuk mengembalikan nilai dari function ini

a=Kuadrat(4)                                                #Untuk memasukan value argument
print("Return Valuenya ->",a)                               #Untuk cek output return value

#=====================================================================
print("-"*40)

#FUNCTION WITH RETURN VALUE & MULTIPLE ARGUMENT
#TAMBAH
def tambah(argument1,argument2):
    totalTambah=argument1+argument2
    print(argument1, '+', argument2, '=', totalTambah)
    return totalTambah                                      #Untuk mengembalikan nilai dari function ini

a=tambah(3,5)                                               #Untuk memasukan value argument
print(a)                                                    #Untuk cek output return value

#KALI
def kali(argument1,argument2):
    totalKali=argument1*argument2
    print(argument1, 'x', argument2, '=', totalKali)
    return totalKali

b=kali(10,2)
print(b)


#GABUNGAN TAMBAH KALI
def kaliTambah(argument1,argument2,argument3):
    totalKaliTambah=argument1*argument2+argument3
    print(argument1, 'x', argument2, '+', argument3, '=', totalKaliTambah)
    return totalKaliTambah

c=kaliTambah(10,2,50)
print(c)


#GABUNGAN MENGGUNAKAN VARIABEL PADA ARGUMENT
def kaliTambah(argument1,argument2,argument3):
    totalKaliTambah=argument1*argument2+argument3
    print(argument1, 'x', argument2, '+', argument3, '=', totalKaliTambah)
    return totalKaliTambah

d=kaliTambah(10,2,b)
print(d)