# Praktikum 36
# Topik: input(), output, dan interaksi dengan pengguna
# Jalankan dengan: python praktikum_36.py
# Jalankan dari folder Pyhton/


def tampilkan_sapaan():
    """Menerima nama dan menampilkan sapaan."""
    nama = input("Masukkan nama: ")
    print(f"Halo, {nama}! Selamat datang.")


def hitung_luas_persegi():
    """Menerima sisi persegi dan menampilkan luasnya."""
    sisi = float(input("Masukkan panjang sisi (cm): "))
    luas = sisi * sisi
    print(f"Luas persegi: {luas} cm")


def kalkulator_sederhana():
    """Menerima dua bilangan dan satu operasi, lalu menghitung."""
    angka1 = float(input("Angka pertama: "))
    angka2 = float(input("Angka kedua: "))
    print(f"Angka pertama : {angka1}")
    print(f"Angka kedua   : {angka2}")
    print(f"Jumlah        : {angka1 + angka2}")
    print(f"Selisih       : {angka1 - angka2}")
    print(f"Perkalian     : {angka1 * angka2}")
    if angka2 != 0:
        print(f"Pembagian     : {angka1 / angka2}")
    else:
        print("Pembagian     : tidak dihitung karena pembagi nol")


def format_harga():
    """Menerima harga dan jumlah, lalu menampilkan total pembayaran."""
    harga_satuan = int(input("Harga satuan (Rp): "))
    jumlah = int(input("Jumlah barang: "))
    total = harga_satuan * jumlah
    print(f"Harga satuan : Rp{harga_satuan}")
    print(f"Jumlah       : {jumlah}")
    print(f"Total        : Rp{total}")


def main():
    print("=== Program Praktikum 36 ===\n")

    print("1. Sapaan")
    tampilkan_sapaan()

    print("\n2. Luas persegi")
    hitung_luas_persegi()

    print("\n3. Kalkulator sederhana")
    kalkulator_sederhana()

    print("\n4. Format harga")
    format_harga()

    print("\n=== Selesai ===")


if __name__ == "__main__":
    main()