# Soal Test Awal 08

Uji awal ini menguji kemampuan memakai `input()` untuk membaca tiga data, menyimpannya ke dalam variabel, lalu menampilkannya kembali dengan f-string.

---

## Bagian 1 — Tulis programnya

Buat program yang meminta tiga data dari pengguna, masing-masing disimpan ke dalam variabel tersendiri:

| No | Data | Sifat |
| --- | --- | --- |
| 1 | NIM | teks |
| 2 | Nama lengkap | teks |
| 3 | Umur | teks |

Setelah ketiga data diterima, program menampilkan satu baris berikut.

## Keluaran yang diharapkan

```text
Si Rian Indra ( 123456789 ) berusia 18 tahun.
```

Perhatikan tiga hal pada keluaran itu.

- angka di dalam kurung adalah NIM
- nilai panjang adalah Umur
- susunan kalimatnya adalah `Si {nama_lengkap} ( {nim} ) berusia {umur} tahun.`

## Bagian 2 — Coba sendiri

Jalankan program lalu masukkan data berikut.

| NIM | Nama lengkap | Umur |
| --- | --- | --- |
| 123456789 | Rian Indra | 18 |

Cocokkan keluarannya dengan format di atas. Coba lagi memakai data berbeda untuk memastikan program bukan hanya benar untuk satu data saja.

## Bagian 3 — Uji pemahaman

Jawab pertanyaan berikut tanpa menjalankan program.

1. Mengapa `print(f"...")` dipakai, bukan `print("...")` biasa?
2. Jika tanda kurung kurawal `{nim}` dihapus dan diganti `{nama_lengkap}`, apa yang terjadi pada keluaran?
3. Apa yang terjadi bila `f` dihapus dari awalan string, sehingga menjadi `print("Si {nama_lengkap} ...")`? Jalankan untuk memastikan.
4. Jika umur diganti menjadi 25 dan 7, apakah kurawal `{umur}` masih berfungsi? Jelaskan alasannya.
5. Perhatikan jumlah spasi di dalam kurung pada keluaran. Apakah spasi itu muncul karena program, atau karena penulisan di dalam kurung kurawal?

## Bagian 4 — Variasi

Ubah program sehingga memenuhi semua ketentuan berikut.

1. Tahun lahir dihitung dari umur dan tahun sekarang, bukan diminta langsung.
2. Keluarannya berbunyi `Rian Indra, lahir tahun 2008.` tanpa tanda kurung.
3. Angka tahun lahir berubah sesuai umur yang dimasukkan, dan program tetap benar pada tahun mana pun.

Untuk acuan, dengan umur 18 pada tahun 2026, tahun lahirnya 2008.

## Jawaban singkat

1. f-string dipakai agar nilai variabel bisa disisipkan langsung ke dalam teks.
2. Yang tampil adalah isi variabel `nama_lengkap`, bukan NIM.
3. Kurawal kurawal akan tercetak apa adanya sebagai teks biasa, bukan diisi nilainya.
4. Masih berfungsi. Nilai variabel tidak bergantung pada angkanya, baik 25 maupun 7.
5. Spasi itu berasal dari penulisan di dalam kurung kurawal pada program, bukan dari program itu sendiri.

Untuk bagian 4, tahun lahir dihitung dengan mengurangi tahun sekarang dengan umur.