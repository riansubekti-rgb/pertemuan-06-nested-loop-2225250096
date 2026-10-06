# Program untuk menghitung total kombinasi pasangan loop
print("--- Hitung Pasangan ---")
hitung = 0
for i in range(1, 4):
    for j in range(1, 4):
        hitung += 1
        print(f"Pasangan ke-{hitung}: ({i}, {j})")
print(f"Total seluruh pasangan adalah: {hitung}")