# Soal Praktikum 37

Bab 4 membahas operator perbandingan, nilai Boolean, dan percabangan `if`, `elif`, `else`. Kerjakan soal berikut secara terpisah, lalu jalankan setiap program dan cocokkan hasilnya dengan keterangan yang diberikan.

---

## Soal 1 — Perbandingan tiga nilai

Buat program yang meminta dua angka, lalu menampilkan `lebih besar`, `sama`, atau `lebih kecil`.

| Masukan | Keluaran yang diharapkan |
| --- | --- |
| 10 dan 4 | lebih besar |
| 7 dan 7 | sama |
| 3 dan 8 | lebih kecil |

---

## Soal 2 — Genap atau ganjil

Buat program yang meminta satu angka bulat, lalu menentukan apakah angka tersebut genap atau ganjil. Gunakan operator modulo `%`.

---

## Soal 3 — Syarat segitiga

Tiga bilatangan dapat membentuk segitiga apabila jumlah dua sisi selalu lebih besar daripada sisi ketiga. Buat program yang meminta tiga sisi, lalu menampilkan `Dapat membentuk segitiga` atau `Tidak dapat membentuk segitiga`.

Petunjuk: ketiga syarat harus diperiksa sekaligus.

```python
side_a + side_b > side_c and side_b + side_c > side_a and side_a + side_c > side_b
```

| Masukan | Keluaran yang diharapkan |
| --- | --- |
| 3, 4, 5 | Dapat membentuk segitiga |
| 1, 2, 3 | Tidak dapat membentuk segitiga |
| 5, 5, 9 | Tidak dapat membentuk segitiga |

---

## Soal 4 — Status stok

Buat program yang meminta jumlah stok, lalu menampilkan keterangan berikut.

| Jumlah stok | Keluaran |
| --- | --- |
| 0 | Stok habis |
| 1 sampai 4 | Stok menipis |
| 5 sampai 19 | Stok sedang baik |
| 20 atau lebih | Stok aman |

---

## Soal 5 — Nilai huruf

Buat program yang meminta nilai dan menampilkan nilai huruf dengan aturan berikut.

| Nilai | Nilai huruf |
| --- | --- |
| 85 sampai 100 | A |
| 75 sampai 84 | B |
| 65 sampai 74 | C |
| 55 sampai 64 | D |
| di bawah 55 | E |

---

## Soal 6 — Perbaiki kode

Perhatikan kode berikut yang tidak dapat dijalankan.

```python
score = 80
if score = 80
    print("Nilai 80")
```

Jelaskan:
1. Apa yang salah pada baris kedua?
2. Bentukkan perbaikannya.
3. Mengapa tanda `=` tidak dapat dipakai di dalam kondisi?

---

## Soal 7 — Perhatikan indentasi

Perhatikan kode berikut.

```python
score = 80
if score >= 60:
print("Lulus")
print("Program selesai")
```

Jelaskan:
1. Mengapa program berhenti dengan `IndentationError`?
2. Bentukkan perbaikannya.
3. Jika `score` diganti menjadi 50, baris mana yang akan ditampilkan?

---

## Soal 8 — Gabungkan dua syarat

Buat program kasir yang meminta total belanja dan keanggotaan. Diskon 10 persen diberikan apabila total belanja minimal 200.000 **dan** pengguna adalah member. Tampilkan harga akhir.

---

## Soal 9 — Perbandingan bertingkat

Tuliskan satu baris kondisi yang bernilai benar apabila angka yang dimasukkan berada di antara 0 sampai 100, kedua batas termasuk.

---

## Jawaban singkat

1. Gunakan `if`, `elif`, `else` dengan operator `>`, `==`, dan bentuk sisanya.
2. `number % 2 == 0` berarti genap.
3. Periksa ketiga syarat dengan operator `and`.
4. Periksa dari nilai terkecil ke terbesar agar setiap kondisi cukup satu perbandingan.
5. Periksa dari batas tertinggi ke terendah.
6. Kurang tanda titik dua. Perbaikannya `if score == 80:`. Tanda `=` hanya untuk penugasan.
7. Blok `if` harus menjorok. Setelah diperbaiki dan `score` bernilai 50, hanya `Program selesai` yang ditampilkan.
8. `if total_price >= 200000 and member:` lalu `final_price = total_price - total_price * 0.10`.
9. `if 0 <= number <= 100:`