# Praktikum 37
# Topik: operator perbandingan, Boolean, dan percabangan
# Jalankan dengan: python praktikum_37.py


def nilai_huruf(score):
    """Mengubah angka menjadi nilai huruf A sampai E."""
    if score >= 85:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 65:
        return "C"
    elif score >= 55:
        return "D"
    else:
        return "E"


def perbandingan_angka(first_number, second_number):
    """Membandingkan dua angka dan mengembalikan keterangan."""
    if first_number > second_number:
        return "lebih besar"
    elif first_number == second_number:
        return "sama"
    else:
        return "lebih kecil"


def paritas(number):
    """Menentukan apakah angka genap atau ganjil."""
    if number % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"


def status_stok(stock):
    """Menentukan status stok berdasarkan jumlahnya."""
    if stock == 0:
        return "Stok habis"
    elif stock < 5:
        return "Stok menipis"
    elif stock < 20:
        return "Stok sedang baik"
    else:
        return "Stok aman"


def cek_segitiga(side_a, side_b, side_c):
    """Memeriksa apakah tiga sisi dapat membentuk segitiga."""
    if side_a + side_b > side_c and side_b + side_c > side_a and side_a + side_c > side_b:
        return "Dapat membentuk segitiga"
    else:
        return "Tidak dapat membentuk segitiga"


def main():
    print("=== Program Praktikum 37 ===\n")

    print("1. Perbandingan dua angka")
    first_number = float(input("Angka pertama: "))
    second_number = float(input("Angka kedua: "))
    print("Hasil:", perbandingan_angka(first_number, second_number))

    print("\n2. Genap atau ganjil")
    number = int(input("Masukkan angka: "))
    print("Hasil:", paritas(number))

    print("\n3. Status stok")
    stock = int(input("Jumlah stok: "))
    print("Hasil:", status_stok(stock))

    print("\n4. Syarat segitiga")
    side_a = float(input("Sisi a: "))
    side_b = float(input("Sisi b: "))
    side_c = float(input("Sisi c: "))
    print("Hasil:", cek_segitiga(side_a, side_b, side_c))

    print("\n5. Nilai huruf")
    score = int(input("Masukkan nilai: "))
    print("Nilai huruf:", nilai_huruf(score))

    print("\n=== Selesai ===")


if __name__ == "__main__":
    main()