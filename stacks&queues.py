#STACKING/STACKS METHOD
Stacks = [1,2,3,4,5,6]              #Data Awal
print('Data Sekarang: ', Stacks)

#MEMASUKAN DATA BARU
Stacks.append(7)
print('Data Masuk: ', 7)
print('Data Sekarang: ', Stacks)

Stacks.append(8)
print('Data Masuk: ', 8)
print('Data Sekarang: ', Stacks)

Out = Stacks.pop()              #Untuk menghapus data value paling akhir (No Indexing)
print('Data Keluar: ', Out)
print('Data Sekarang: ', Stacks)


#===================================================================================================
print(100*'=')


#QUEUING/QUEUES METHOD
from collections import deque   # <-- Menggunakan Module/Packages pada Phyton

Queue = deque([1,2,3,4,5])  #Data Awal
print('Data Sekarang: ',Queue)

#MENAMBAHKAN DATA VALUE
Queue.append(6)
print('Data Masuk: ', 6)
print('Data Sekarang: ',Queue)

Queue.append(7)
print('Data Masuk: ', 7)
print('Data Sekarang: ',Queue)

#MENGURANGI DATA VALUE
Out2 = Queue.popleft()          # <-- popleft() berguna untuk menghapus data value dari kiri
print('Data Keluar: ', Out2)
print('Data Sekarang: ',Queue)