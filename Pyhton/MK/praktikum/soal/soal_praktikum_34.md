# Soal Praktikum 34

Kode berikut masih mengandung kesalahan. Perbaiki sehingga program dapat berjalan dan menghasilkan luas dan keliling lingkaran dari radius yang dimasukkan pengguna.

```python
# Minta radius
radius = input("Radius:")
radius = float(radius)

# Hitung
pi = 3.14
luas_lingkaran = pi * radius * radius
keliling_lingkaran = 2 pi * radius

# Tampilkan hasil
print("Luas lingakran:,  str(luas_lingkaran))
print("Keliling lingkaran:", str(keliling_lingkaran))
```

## Yang perlu diperbaiki

1. Baris `radius = float(radius)` — apakah aman dijalankan sebelum nilainya dipastikan?
2. Baris `keliling_lingkaran = 2 pi * radius` — operator apa yang hilang di antara `2` dan `pi`?
3. Baris `print("Luas lingakran:,  str(luas_lingkaran))` — periksa jumlah tanda kurung dan teks yang dicetak.
4. Periksa dengan `type()` dan `print()` tanpa konversi ke string.

## Keluaran yang diharapkan

```text
Radius: 7
Luas lingkaran: 153.86
Keliling lingkaran: 43.96
```

## Batasan

- Gunakan `pi = 3.14`
- Angka hasil boleh banyak digit desimal, tidak perlu dibulatkan