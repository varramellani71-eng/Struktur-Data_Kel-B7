import os

print("COMPETITIVE PROGRAMMING")

DATA_FILE = "peserta_lomba.txt"
peserta_set = set()

# Membaca data dari file jika ada
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as file:
        for line in file:
            nama, prodi, nim = line.strip().split(",")
            peserta_set.add((nama, prodi, nim))

while True:
    print("\n=== MENU PENDAFTARAN ===")
    print("1. Tambah Peserta")
    print("2. Tampilkan Peserta")
    print("3. Keluar")

    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        nama = input("Masukkan nama peserta: ")
        prodi = input("Masukkan asal prodi: ")
        nim = input("Masukkan NIM peserta: ")

        data_peserta = (nama, prodi, nim)

        if data_peserta in peserta_set:
            print("Peserta sudah terdaftar!")
        else:
            peserta_set.add(data_peserta)

            # Simpan ke file
            with open(DATA_FILE, "a") as file:
                file.write(f"{nama},{prodi},{nim}\n")

            print("Peserta berhasil ditambahkan!")

    elif pilihan == "2":
        if not peserta_set:
            print("Belum ada peserta.")
        else:
            print("\n=== DAFTAR PESERTA ===")
            for i, peserta in enumerate(peserta_set, start=1):
                print(f"\nPeserta ke-{i}")
                print(f"Nama : {peserta[0]}")
                print(f"Prodi: {peserta[1]}")
                print(f"NIM  : {peserta[2]}")

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")