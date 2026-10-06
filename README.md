Nama: Rian Subekti  
NIM: 2225250096  
Kelas: 3F

## Tujuan
Menggunakan nested loop, pola, akumulasi, dan pencacahan.

## Cara Menjalankan
python3 tugas/tabel_perkalian_dan_statistik.py

## Algoritma Tugas 3
- **Loop Luar (Outer Loop):** Berfungsi untuk mengatur perpindahan baris pada tabel perkalian dari 1 hingga $n$.
- **Loop Dalam (Inner Loop):** Berfungsi untuk mengatur perpindahan kolom atau proses perkalian per baris dari 1 hingga $n$.
- **Akumulator:** Variabel `total_keseluruhan` yang bertugas menjumlahkan seluruh hasil perkalian secara kumulatif.
- **Counter:** Variabel `jumlah_data` yang bertugas menghitung jumlah total iterasi atau elemen data yang diproses.

## Hasil Pengujian

| File Program | Input | Hasil yang Diharapkan | Keluaran Aktual | Status |
| :--- | :--- | :--- | :--- | :--- |
| `latihan/01_pasangan_indeks.py` | *Tidak ada* (Default) `range(3)` | Menampilkan seluruh kombinasi indeks pasangan $(i, j)$ dari $(0,0)$ sampai $(2,2)$ | Menampilkan seluruh kombinasi indeks pasangan $(i, j)$ dari $(0,0)$ sampai $(2,2)$ | Lulus (Valid) |
| `latihan/02_pola_segitiga.py` | `4` | Menampilkan pola segitiga bintang setinggi 4 baris secara berurutan | Menampilkan pola segitiga bintang setinggi 4 baris secara berurutan | Lulus (Valid) |
| `latihan/03_jumlah_per_baris.py` | *Tidak ada* (Default) `range(1, 4)` | Menampilkan nilai per baris (perkalian $i \times j$) beserta total jumlah per barisnya | Menampilkan nilai per baris (perkalian $i \times j$) beserta total jumlah per barisnya | Lulus (Valid) |
| `latihan/04_hitung_pasangan.py` | *Tidak ada* (Default) `range(1, 4)` | Menampilkan rincian pasangan dari $1$ sampai $3$ dan menghitung total keseluruhan pasangan ($9$ pasangan) | Menampilkan rincian pasangan dari $1$ sampai $3$ dan menghitung total keseluruhan pasangan ($9$ pasangan) | Lulus (Valid) |
| `tugas/tabel_perkalian_dan_statistik.py` | `5` | Menampilkan tabel perkalian $1$ sampai $5$, Total Keseluruhan: 225, Jumlah Data: 25, Rata-rata: 9.00 | Menampilkan tabel perkalian $1$ sampai $5$, Total Keseluruhan: 225, Jumlah Data: 25, Rata-rata: 9.00 | Lulus (Valid) |

## Analisis Efisiensi
Badan loop dalam (inner loop) akan berjalan sebanyak $n \times n$ (atau $n^2$) kali untuk setiap input $n$. Hal ini terjadi karena dalam setiap 1 iterasi loop luar, loop dalam akan diselesaikan secara penuh sebanyak $n$ kali.

## Refleksi
- **Kesalahan yang Ditemukan:** Penempatan fungsi `print()` untuk baris baru yang keliru di dalam loop dalam, menyebabkan format tabel perkalian tercetak secara vertikal ke bawah alih-alih membentuk matriks dua dimensi.
- **Cara Memperbaiki:** Memindahkan perintah `print()` baris baru ke dalam ruang lingkup loop luar namun di luar loop dalam, sehingga baris baru hanya dieksekusi setelah satu baris kolom selesai dicetak sepenuhnya.