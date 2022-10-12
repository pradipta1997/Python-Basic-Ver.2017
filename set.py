#SET/HIMPUNAN
Superhero = set()   # <-- Set/Himpunan berguna untuk membuat daftar list yang tidak berurutan

Superhero.add("Batman")
Superhero.add("Daredevil")
Superhero.add("Superman")
Superhero.add("ManRay")
Superhero.add("Iron Man")
Superhero.add("Spiderman")

print(Superhero)

#===================================================================================================
print(90*'=')
print(" ")

#STRUKTUR PEMBUATAN METODE SET
angkaGanjil = {1,3,5,7,9}
angkaGenap = {2,4,6,8,10}
angkaPrima = {2,3,5,7}

print(angkaGanjil.union(angkaGenap))    #Pengabungan variable Ganjil & Genap dengan Fucntion UNION
print(angkaGanjil.intersection(angkaPrima)) #Pengabungan variable Ganjil dan Prima dengan Function Intersection