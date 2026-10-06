# Program untuk mencetak pola segitiga bintang menggunakan nested loop
print("--- Pola Segitiga Bintang ---")
tinggi = 4
for i in range(1, tinggi + 1):
    for j in range(i):
        print("*", end=" ")
    print()