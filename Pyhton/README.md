# Python

Catatan pribadi untuk belajar Python dari nol. Repo ini adalah kumpulan catatan kuliah berbentuk HTML statis, tanpa build system dan tanpa framework. Setiap bab adalah satu file `.html` yang bisa langsung dibuka di peramban.

## Daftar bab
Kalau pemindahan praktikum_32–35 ke Pyhton/praktikum/ itu memang mau ikut, bilang saja — saya buat commit terpisah supaya riwayatnya rapi.
| Bab | Judul | Isi |
| --- | --- | --- |
| 01 | Get Started | Menjalankan Python, interpreter, VS Code, pip, virtual environment |
| 02 | Variabel, Tipe Data, dan Cara Menyimpan Nilai | Variabel, string, integer, float, boolean, operator, konversi tipe, f-string |
| 03 | Input, Output, dan Interaksi dengan Pengguna | `print()`, `input()`, f-string dinamis, konversi `int()` dan `float()`, parameter `sep` dan `end` |
| 04 | Operator Perbandingan, Boolean, dan Percabangan | `== != > < >= <=`, `True` dan `False`, `and` `or` `not`, `if` `elif` `else`, indentasi |
| 05 | Loop dan Perulangan | belum ditulis |
| 06 | Function | belum ditulis |
| 07 | List, Tuple, Dictionary, dan Set | belum ditulis |
| 08 | File, Exception, Module, dan OOP | belum ditulis |

Empat bab pertama sudah ditulis. Bab 05 sampai 08 masih rencana.

## Menjalankan

Tidak ada langkah instalasi. Buka `index.html` dengan klik ganda, lalu pilih babnya.

Untuk menjalankan skrip praktikum, butuh Python 3.14 yang sudah terpasang:

```bash
cd Pyhton/praktikum
python praktikum_36.py
```

## Struktur folder

```
Pyhton/
├── index.html                       daftar bab
├── README.md                        berkas ini
├── catatan/
│   ├── bab 1 - Get started.html
│   ├── bab 2 - Python Dasar.html
│   ├── bab 3 - Input Output dan Interaksi dengan Pengguna.html
│   ├── bab 4 - Operator Perbandingan Boolean dan Percabangan.html
│   └── bab * mentahan.md            materi mentah, tidak dipublikasikan
├── praktikum/
│   ├── praktikum_32.py ... praktikum_37.py
└── soal/
    └── soal_praktikum_32.md ... soal_praktikum_37.md
```

Catatan penting. Nama folder `Pyhton` memang salah eja, dan itu disengaja. Mengubahnya akan merusak seluruh tautan yang sudah ada.

## Aturan penulisan bab

Bab ditulis dalam bahasa Indonesia dengan nada akademis. Larangan keras:

- jangan gunakan `kamu`, `Anda`, atau bentuk alamat pembaca lain
- jangan sebut pernah bahwa teks ini ditulis mesin
- nama variabel dan fungsi memakai `snake_case` berbahasa Inggris, bukan bahasa Indonesia
- setiap contoh program harus benar-benar dijalankan sebelum dipakai
- tuliskan versi Python yang jadi acuan

Bab 03 dan 04 adalah contoh terbaik untuk diikuti. Keduanya memakai struktur yang sama, mulai dari blok kutipan beranimasi di bagian atas, catatan versi, lalu bagian bernomor yang diakhiri ringkasan dan daftar sumber.

## Praktikum

Setiap skrip `praktikum_NN.py` selalu berpasangan dengan `soal/soal_praktikum_NN.md`. Penomorannya sama, jadi menambah skrip tanpa soal berarti pekerjaan belum selesai.

Pasangan yang sekarang ada:

| Skrip | Topik | Isi soal |
| --- | --- | --- |
| 32 | Menyimpan data mahasiswa dengan `input()` dan `f-string` | 1 soal |
| 33 | Menu dan pembacaan pilihan | 1 soal |
| 34 | Perhitungan luas dan keliling lingkaran | Perbaikan kode, 4 pertanyaan |
| 35 | Perhitungan luas dan keliling lingkaran | Perbaikan kode, 4 pertanyaan |
| 36 | Fungsi dasar: sapaan, luas, kalkulator, harga | 8 soal |
| 37 | Fungsi kondisi: nilai huruf, segitiga, stok | 9 soal |

Soal 32 sampai 35 masih memakai format lama tanpa penomoran soal per bagian. Soal 36 dan 37 memakai format terbaru dengan judul `## Soal` dan kunci jawaban di akhir. Ikuti format terbaru untuk tambahan berikutnya.

## Fitur yang belum ada

Bab-bab Python belum memakai drawer daftar isi untuk layar kecil maupun kuis interaktif. Modul Fisika sudah punya keduanya dan menjadi acuan bila ingin ditambahkan.

## Catatan untuk pengerjaan dengan bantuan AI

Bila repo ini dikerjakan bersama bantuan AI, baca `agent-study/agent-pyhton.md` lebih dahulu. Berkas itu memuat inventaris terbaru, aturan isi khusus Python, template bab, dan catatan jebakan validasi yang sudah pernah menjadi masalah.

## Sumber

- [Dokumentasi resmi Python](https://docs.python.org/3/)
- [Tutorial Python](https://docs.python.org/3/tutorial/introduction.html)
- [Referensi bahasa Python](https://docs.python.org/3/reference/)
- [Real Python](https://realpython.com/)