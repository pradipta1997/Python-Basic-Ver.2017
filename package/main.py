#DARI FILE MAIN INI HANYA CUKUP TINGGAL MEMANGGIL
# PACKAGES SAJA (SCIENT) YANG BERACUAN PADA FILE
# (__INIT__.PY), MAKA SEMUA FUNCTION PADA MASING2
# MODULE AKAN TERPANGGIL.

import scient # <-- Memanggil file package scient yang beracuan pada file __init__ yg mana sudah mewakil setiap modul

t = scient.tambah(1,1)
print(t)