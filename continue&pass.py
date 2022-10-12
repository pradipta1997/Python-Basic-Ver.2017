for i in range(1,11):

    if i == 6:
        print("NILAI i ADALAH", i)
        #break                    #Untuk mengakhiri atau menghentikan for/looping (Terminasi)
        continue                  #Untuk melanjutkan loop ke step selanjutnya, walaupun yang dicari sudah ditemukan
        #pass                     #Untuk melewati/meneruskan looping

    print("Nilai saat ini", i)

else:
    print("Akhir dari loop!")

print("Print di luar loop")

