var = "domba"
angka = 4
angka = str(angka)
gabung = var + angka
print(type(gabung))
print(gabung)

no_pert = angka

path_pertemuan = "\"//option[. = 'Pertemuan" + no_pert + "']\""
print(type(path_pertemuan))
print(path_pertemuan)
