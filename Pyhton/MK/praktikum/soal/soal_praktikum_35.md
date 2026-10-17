# Soal Praktikum 35

Perbaiki kode berikut yang memiliki sejumlah *run-time error* sehingga berhasil jalan.

```python
# Minta radius
radius = input("Radius:")
radius = float(radius)

# Hitung
pi = 3,14
luas_lingkaran = pi * radius * radius
keliling_lingkaran = 2 * pi / radius

# Tampilkan hasil
print("Luas lingakran:"  str(luas_lingkaran)
print("Keliling lingkaran:", str(keliling_lingkaran))
```

## Yang perlu diperiksa

1. Baris `pi = 3,14` — tanda apa yang seharusnya menjadi pemisah antara bagian bulat dan desimal?
2. Baris `keliling_lingkaran = 2 * pi / radius` — sudahkah rumus keliling lingkaran benar?
3. Baris `print("Luas lingakran:"  str(luas_lingkaran)` — periksa jumlah tanda kurung dan tanda baca antar nilai.
4. Apakah `float()` perlu dipanggil ulang dengan variabel yang sama, atau cukup satu kali?

## Keluaran yang diharapkan

```text
Radius: 7
Luas lingkaran: 153.86
Keliling lingkaran: 43.96
```

## Batasan

- Nilai `pi` tetap 3.14
- Angka desimal tidak perlu dibulatkan
- Program hanya menampilkan dua baris hasil