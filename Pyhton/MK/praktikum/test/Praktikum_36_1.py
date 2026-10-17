masukan = input("Ketik pesan anda: ")
posisi_x = masukan.find("x")

print(f"Pesan sesudah karakter 'x': {masukan[posisi_x-1:]}")