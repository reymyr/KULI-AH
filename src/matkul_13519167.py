# Kelas mata kuliah yang menyimpan nama/kode, prerequisite, dan jumlah prerequisite yang belum diambil
class Matkul:
    # Konstruktor
    def __init__(self, name, prereq):
        self.name = name
        self.prereq = prereq
        self.unpickedPrereq = len(prereq)

    # Method untuk mengurangi jumlah prereq yang belum diambil
    def decrementCount(self):
        self.unpickedPrereq -= 1