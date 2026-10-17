# Soal Praktikum 36

Bab 3 membahas `input()`, `print()`, dan interaksi dengan pengguna. Kerjakan soal-soal berikut secara terpisah. Jalankan setiap program dengan memasukkan data sesuai petunjuk.

---

## Soal 1 — Sapaan

Buat program yang:

1. meminta nama pengguna,
2. menampilkan sapaan berbentuk `Halo, {nama}!`.

Contoh keluaran:

```text
Masukkan nama: Rian
Halo, Rian!
```

---

## Soal 2 — Luas persegi

Buat program yang meminta panjang sisi persegi dari pengguna (boleh berupa desimal), lalu menampilkan luasnya. Gunakan `float()` agar sisi boleh bernilai desimal.

Contoh keluaran:

```text
Masukkan panjang sisi (cm): 5
Luas persegi: 25.0 cm
```

---

## Soal 3 — Sapaan dengan validasi panjang nama

Buat program yang meminta nama pengguna, lalu:

- jika panjang nama lebih dari 3 karakter, tampilkan `Nama valid. Halo, {nama}!`,
- jika tidak, tampilkan `Nama terlalu pendek.`

Untuk sementara, gunakan perbandingan panjang dengan fungsi bawaan `len()`. Contoh:

```python
nama = input("Masukkan nama: ")
if len(nama) > 3:
    print(f"Nama valid. Halo, {nama}!")
else:
    print("Nama terlalu pendek.")
```

> Catatan: materi `if`/`else` dibahas lengkap pada bab berikutnya, tetapi soal ini dapat dikerjakan dengan struktur di atas.

---

## Soal 4 — Kalkulator sederhana

Buat program yang meminta dua bilangan dari pengguna, lalu menampilkan:

- jumlah,
- selisih,
- perkalian,
- pembagian.

Jika pembagi bernilai nol, jangan melakukan pembagian; tampilkan pesan bahwa pembagian dilewati.

Contoh keluaran:

```text
Angka pertama : 10.0
Angka kedua   : 4.0
Jumlah        : 14.0
Selisih       : 6.0
Perkalian     : 40.0
Pembagian     : 2.5
```

---

## Soal 5 — Total harga belanja

Buat program kasir sederhana yang:

1. meminta harga satuan barang (bilangan bulat),
2. meminta jumlah barang (bilangan bulat),
3. menghitung dan menampilkan total pembayaran.

Contoh keluaran:

```text
Harga satuan : Rp25000
Jumlah       : 3
Total        : Rp75000
```

---

## Soal 6 — Mengubah input menjadi tipe yang sesuai

Perhatikan kode berikut:

```python
umur = input("Masukkan umur: ")
print(umur + 1)
```

Jelaskan:
1. Tipe data apa yang dimiliki variabel `umur` setelah `input()` dijalankan?
2. Mengapa baris `print(umur + 1)` menyebabkan `TypeError`?
3. Tuliskan bentuk perbaikan yang menggunakan konversi tipe.

---

## Soal 7 — Formatting keluaran dengan `sep` dan `end`

Buat program yang menampilkan tiga nama dengan pemisah ` | `, lalu menampilkan dua kalimat pada baris yang sama menggunakan `end=" "`.

Contoh keluaran:

```text
Rian | Andi | Sari
Halo selamat belajar
```

---

## Soal 8 — Program gabungan

Buat program yang meminta:

- nama pengguna,
- umur (bilangan bulat),
- tinggi badan dalam cm (bilangan desimal),

lalu menampilkan ringkasan:

```text
=== PROFIL ===
Nama   : Rian
Umur   : 18 tahun
Tinggi : 170.5 cm
```

Pastikan `umur` dikonversi dengan `int()` dan `tinggi` dengan `float()`.

---

## Jawaban singkat

1. Sapaan: gunakan `nama = input(...)` lalu `print(f"Halo, {nama}!")`.
2. Luas persegi: `sisi = float(input(...))`, lalu `luas = sisi * sisi`.
3. Validasi nama: gunakan `len(nama) > 3`.
4. Kalkulator: konversi kedua bilangan dengan `float()`, gunakan `if angka2 != 0` sebelum membagi.
5. Harga: `harga_satuan = int(input(...))`, `jumlah = int(input(...))`, `total = harga_satuan * jumlah`.
6. `input()` menghasilkan `str`; `+` tidak bisa menjumlahkan `str` dan `int`. Perbaikan: `umur = int(input(...))`.
7. `sep=" | "` untuk pemisah, `end=" "` untuk melanjutkan baris.
8. Gabungkan ketiganya dengan konversi yang sesuai.