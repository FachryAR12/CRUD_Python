
def create_first():
    with open("Database.txt", "w", encoding="utf-8") as file:
        print("Membuat file Database.txt baru dan menulis data awal...\n")

        penulis = input("Masukkan nama penulis: ")
        judul = input("Masukkan judul: ")
        tahun = input("Masukkan tahun: ")

        data_str = f"{penulis},{judul},{tahun}\n"
        file.write(data_str)

    print("Database.txt berhasil dibuat dan diisi dengan data pertama.\n")

def create_data():
    with open("Database.txt", "a", encoding="utf-8") as file:
        print("tambahkan data...\n")
        penulis = input("Masukkan nama penulis: ")
        judul = input("Masukkan judul: ")
        tahun = input("Masukkan tahun: ")
        file.write(f"{penulis},{judul},{tahun}\n")
    print("Data berhasil ditambahkan!")

import os

def update_database():
    database_file = "Database.txt"

    # Pastikan file database ada
    if not os.path.exists(database_file):
        print("❌ Database belum ada.")
        return

    # Baca isi database
    with open(database_file, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file if line.strip()]

    if not lines:
        print("📂 Database kosong, tidak ada data untuk diupdate.")
        return

    # Pisahkan data ke dalam list
    data = [line.split(",") for line in lines]

    # Tampilkan tabel (mirip seperti read_database)
    print("\nDaftar data dalam database:")
    print("+----+----------------+----------------+--------+")
    print("| No | Penulis        | Judul Buku     | Tahun  |")
    print("+----+----------------+----------------+--------+")
    for i, (penulis, judul, tahun) in enumerate(data, start=1):
        print(f"| {i:<2} | {penulis:<14} | {judul:<14} | {tahun:<6} |")
    print("+----+----------------+----------------+--------+")

    # Pilih data yang ingin diupdate
    try:
        index = int(input("\nMasukkan nomor data yang ingin diupdate: ")) - 1
        if index < 0 or index >= len(data):
            print("❌ Nomor tidak valid.")
            return
    except ValueError:
        print("❌ Masukkan angka yang benar.")
        return

    # Ambil data lama
    penulis_lama, judul_lama, tahun_lama = data[index]

    # Input data baru (kosongkan jika tidak ingin diubah)
    print("\nMasukkan data baru (kosongkan jika tidak ingin diubah):")
    penulis_baru = input(f"Penulis ({penulis_lama}): ") or penulis_lama
    judul_baru   = input(f"Judul Buku ({judul_lama}): ") or judul_lama
    tahun_baru   = input(f"Tahun ({tahun_lama}): ") or tahun_lama

    # Perbarui data
    data[index] = [penulis_baru, judul_baru, tahun_baru]

    # Simpan kembali ke file
    with open(database_file, "w", encoding="utf-8") as file:
        for item in data:
            file.write(",".join(item) + "\n")

    print("\n✅ Data berhasil diperbarui!")

import os

def delete_database():
    database_file = "Database.txt"

    # Pastikan file database ada
    if not os.path.exists(database_file):
        print("❌ Database belum ada.")
        return

    # Baca isi database
    with open(database_file, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file if line.strip()]

    if not lines:
        print("📂 Database kosong, tidak ada data untuk dihapus.")
        return

    # Pisahkan data ke dalam list
    data = [line.split(",") for line in lines]

    # Tampilkan tabel data (mirip seperti read_database)
    print("\nDaftar data dalam database:")
    print("+----+----------------+----------------+--------+")
    print("| No | Penulis        | Judul Buku     | Tahun  |")
    print("+----+----------------+----------------+--------+")
    for i, (penulis, judul, tahun) in enumerate(data, start=1):
        print(f"| {i:<2} | {penulis:<14} | {judul:<14} | {tahun:<6} |")
    print("+----+----------------+----------------+--------+")

    # Pilih data yang ingin dihapus
    try:
        index = int(input("\nMasukkan nomor data yang ingin dihapus: ")) - 1
        if index < 0 or index >= len(data):
            print("❌ Nomor tidak valid.")
            return
    except ValueError:
        print("❌ Masukkan angka yang benar.")
        return

    # Konfirmasi sebelum hapus
    penulis, judul, tahun = data[index]
    konfirmasi = input(f"\n⚠️ Apakah kamu yakin ingin menghapus data '{penulis} - {judul} ({tahun})'? (y/n): ").lower()

    if konfirmasi != "y":
        print("❎ Penghapusan dibatalkan.")
        return

    # Hapus data dari list
    del data[index]

    # Simpan ulang file tanpa data tersebut
    with open(database_file, "w", encoding="utf-8") as file:
        for item in data:
            file.write(",".join(item) + "\n")

    print("\n✅ Data berhasil dihapus!")

