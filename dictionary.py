#DICTIONARY METHOD
Member1 = {"ID":101,
           "Nama":"Pradipta Ramadhan",
           "Pekerjaan":"IT Programmer",
           "Konsentrasi":"Web Dev & Front-End"
           }

Member2 = {"ID":102,
           "Nama":"Anonymous",
           "Pekerjaan":"Back-End",
           "Konsentrasi":"Web Developer"
           }

print(Member1["ID"])    # <--Untuk mengambil value berdasarkan Keys
print(Member2.keys())   # <--Untuk mengambil seluruh Keys
print(Member2.values()) # <--Untuk mengambil seluruh Values
print(Member1.items())  # <--Untuk mengambil seluruh Keys dan Values pada Variable Member1


#================================================================================================

#NOTE

# Metode Dictionary ini sama halnya seperti
# yang dilakukan pada List,Tuple dan Set.
# Perbedaanya disini adalah, Dictionary
# bisa sekaligus membuat Keys & Values
# secara bersamaan, atau sama halnya seperti
# membuat database instan.