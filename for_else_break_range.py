Number = 50

for i in range(0,101):                      #Untuk membuat virtual list dengan (angka awal,angka akhir, increment)
    print(i)

    if i is Number:                         #Untuk mencari nilai yang di input dalam variable Number.
        print('Number Found!', i)
        break                               #Untuk menghentikan loop disaat nomor yang dicari sudah ditemukan.
else:
    print("Number Not Found!, Please Input The Correct Number.")