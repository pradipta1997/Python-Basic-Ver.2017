#SIMPLE FUNCTION
def Motor():                            # <-- "def" adalah bentuk sebuah function pada Phyton
    print('PCX')

def HargaMotor():
    Motor()
    print('Harga Motor PCX 30 jt')

#-------------------------------------------------------------------------------------------------------------

#MEMBUAT FUNCTION DENGAN ARGUNMENT
def HargaMotorTotal(unit):              # <-- Perfunction adalah untuk satu jenis motor, jadi jika ingin
    Motor()                             #mengkalkulasikan banyak motor, maka buat beberapa function.
    Harga = 30000000
    HargaTotal = unit*Harga
    print('Harga',unit,'motor PCX adalah',HargaTotal)

HargaMotorTotal(2)