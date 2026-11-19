def tentukan_kategori(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 60:
        return "C"
    else:
        return "D"

jumlah_mahasiswa = int(input("Masukan jumlah mahasiswa: "))
while jumlah_mahasiswa <= 0:
    print("Jumlah harus lebih dari 0!")
    jumlah_mahasiswa = int(input("Masukan jumlah mahasiswa: "))

total = 0
lulus = 0
tidak_lulus = 0

for i in range (jumlah_mahasiswa):
    nilai = int(input("Masukan nilai mahasiswa: "))
    while nilai < 0 or nilai > 100:
        print("Nilai harus 0 sampai 100!")
        nilai = int(input("Masukan nilai mahasiswa: "))

kategori = tentukan_kategori(nilai)
print("Kategori", kategori)
total = total + nilai
if kategori == "D":
    tidak_lulus = tidak_lulus + 1
else:
    lulus = lulus + 1

rata_rata = total / jumlah_mahasiswa

print()
print("Jumlah mahasiswa : ", jumlah_mahasiswa)
print("Total nilai : ", total)
print("Rata-rata : ", rata_rata)
print("Lulus:", lulus, "| Tidak lulus:", tidak_lulus)