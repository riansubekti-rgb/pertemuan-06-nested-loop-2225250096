# Program untuk menampilkan tabel perkalian dan statistik sederhana
print("=== Tabel Perkalian 1 sampai 5 ===")
total_keseluruhan = 0
jumlah_data = 0

for i in range(1, 6):
    for j in range(1, 6):
        hasil = i * j
        print(f"{i} x {j} = {hasil}\t", end="")
        total_keseluruhan += hasil
        jumlah_data += 1
    print()

rata_rata = total_keseluruhan / jumlah_data
print("\n--- Statistik Sederhana ---")
print(f"Total Keseluruhan : {total_keseluruhan}")
print(f"Jumlah Data       : {jumlah_data}")
print(f"Rata-rata         : {rata_rata:.2f}")