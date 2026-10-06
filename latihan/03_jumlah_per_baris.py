# Program untuk menghitung jumlah nilai per baris dalam nested loop
print("--- Jumlah Nilai per Baris ---")
for i in range(1, 4):
    jumlah = 0
    print(f"Baris {i}: ", end="")
    for j in range(1, 4):
        nilai = i * j
        jumlah += nilai
        print(f"{nilai} ", end="")
    print(f"| Jumlah = {jumlah}")