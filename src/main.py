import os
from matkul import Matkul

## DEKLARASI FUNGSI DAN PROSEDUR
# Fungsi untuk mengambil mata kuliah yang sudah tidak memiliki prerequisite
# Input: Array of Matkul
# Proses: 
# 1. Loop seluruh elemen ArrMatkul
# 2. Jika jumlah prerequisite = 0, keluarkan matkul dari array lalu tambahkan pada output
# Output: Array of Matkul yang berisi semua mata kuliah yang tidak memiliki prerequisite saat ini
def takeZeroPrereq(ArrMatkul):
    # Mengambil mata kuliah yang tidak memiliki prerequisite sekaligus menghapusnya dari array
    zeroPrereq = []
    i = 0
    while i < len(ArrMatkul):
        if ArrMatkul[i].unpickedPrereq == 0:
            zeroPrereq.append(ArrMatkul.pop(i))
        else:
            i += 1

    return zeroPrereq

# Prosedur untuk mengurangi jumlah prereq yang belum diambil pada Array Matkul
# I.S : ArrMatkul dan prereq terdefinisi
# F.S : Jumlah prerequisite setiap elemn ArrMatkul berkurang sesuai dengan isi array prereq
# Proses: 
# 1. Untuk setiap elemen prereq, loop elemen ArrMatkul
# 2. Jika elemen prereq tersebut merupakan prerequisite dari matkul, kurangi jumlah prerequisite yang belum diambil dengan 1
def evaluateNewPrereq(ArrMatkul, prereq):
    # Mengurangi prerequisite setiap mata kuliah pada ArrMatkul berdasarkan prereq
    for pr in prereq:
        for m in ArrMatkul:
            if pr.name in m.prereq:
                m.decrementCount()

# Fungsi untuk melakukan planning mata kuliah dengan Topological Sorting dan memanfaatkan algoritma decrease and conquer
# Input: Array of Matkul
# Proses: 
# 1. Mengambil semua mata kuliah yang saat ini tidak memiliki prerequisite dan mengeluarkannya dari array
# 2. Mengurangi prerequisite dari mata kuliah yang belum diambil berdasarkan mata kuliah yang sekarang diambil
# 3. Ulangi langkah 1 dan 2 pada array sisanya hingga array kosong
# Output: A yang bertipe Array of Array of Matkul dengan A[i] menandakan semua mata kuliah
#         yang harus diambil pada semester (i+1), 0 <= i < len(A)
def planKuliah(ArrMatkul):
    # Array kosong
    if len(ArrMatkul) == 0:
        return []
    # Array tidak kosong
    else:
        # Mengambil mata kuliah yang tidak memiliki prerequisite sekaligus menghapusnya dari array
        current = takeZeroPrereq(ArrMatkul)

        # Mengurangi prerequisite setiap mata kuliah pada array sisanya
        evaluateNewPrereq(ArrMatkul, current)

        # Menggabungkan hasil semester sekarang dan hasil dari pemrosesan array sisanya
        return [current] + planKuliah(ArrMatkul)

# Prosedur untuk menuliskan logo ke layar
# I.S : Sembarang
# F.S : Logo tertulis di layar
def printLogo():
    print("======================================================================")
    print("|   /$$   /$$ /$$   /$$ /$$       /$$$$$$        /$$$$$$  /$$   /$$  |")
    print("|  | $$  /$$/| $$  | $$| $$      |_  $$_/       /$$__  $$| $$  | $$  |")
    print("|  | $$ /$$/ | $$  | $$| $$        | $$        | $$  \ $$| $$  | $$  |")
    print("|  | $$$$$/  | $$  | $$| $$        | $$ /$$$$$$| $$$$$$$$| $$$$$$$$  |")
    print("|  | $$  $$  | $$  | $$| $$        | $$|______/| $$__  $$| $$__  $$  |")
    print("|  | $$\  $$ | $$  | $$| $$        | $$        | $$  | $$| $$  | $$  |")
    print("|  | $$ \  $$|  $$$$$$/| $$$$$$$$ /$$$$$$      | $$  | $$| $$  | $$  |")
    print("|  |__/  \__/ \______/ |________/|______/      |__/  |__/|__/  |__/  |")
    print("======================================================================")

## PROGRAM UTAMA
# Menuliskan logo
printLogo()

# Membaca file
# Pengguna menmasukkan nama file yang ingin dibaca lalu program akan membuat array dari input dalam file
# File harus berada pada folder test
listMatkul = []
filename = input("Masukkan nama file: ")
path = os.path.dirname(os.path.dirname(__file__))
f = open(os.path.join(path, "test", filename), "r")
lines = f.readlines()
for line in lines:
    stripped = line.rstrip('.\n').split(', ')
    listMatkul.append(Matkul(stripped[0], stripped[1:]))
f.close()

# Memproses input menjadi plan kuliah
plan = planKuliah(listMatkul)

# Menuliskan plan kuliah dengan batas samapai semester 8
print("\nRencana kuliah:")
for i in range(min(len(plan), 8)):
    print("Semester", i+1, ": ", end='')
    for j in range(len(plan[i])):
        print(('' if j == 0 else ', ') + plan[i][j].name, end ='')
    print()