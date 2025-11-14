import os
from .DB_project import create_first


def init_console():
    if not os.path.exists("Database.txt"):
        print(" Database.txt tidak ditemukan.")

        # Tanyakan ke user apakah ingin membuat database
        pilihan = input("Apakah kamu ingin membuat dan mengisi database baru? (y/n): ").lower().strip()

        if pilihan == "y":
            create_first()
        else:
            print("\n Program dihentikan. Database tidak dibuat.\n")
            exit()  # keluar dari program
    else:
        print("\n Database.txt ditemukan. Melanjutkan ke proses utama...\n")

def read_database():
    database_file = "Database.txt"

    if not os.path.exists(database_file):
        print("Database belum ada.")
        return

    with open(database_file, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file if line.strip()]

    if not lines:
        print("Database kosong, tidak ada data untuk ditampilkan.")
        return

    # Pisahkan kolom dan buat list data
    data = [line.split(",") for line in lines]

    # Hitung lebar kolom otomatis berdasarkan data terpanjang
    max_penulis = max(len(row[0]) for row in data)
    max_judul = max(len(row[1]) for row in data)
    max_tahun = max(len(row[2]) for row in data)

    # Tambahkan padding agar kolom punya jarak antar batas tabel
    max_penulis += 2
    max_judul += 2
    max_tahun += 2

    # Total lebar garis tabel (disesuaikan dengan kolom dan pemisah)
    total_width = (
        6                # untuk kolom "No" + pemisah
        + max_penulis
        + max_judul
        + max_tahun
        + 10             # tambahan pemisah vertikal dan spasi antar kolom
    )

    # Header tabel
    print("+" + "-" * total_width + "+")
    print(f"| {'No':<3} | {'Penulis':<{max_penulis}} | {'Judul Buku':<{max_judul}} | {'Tahun':<{max_tahun}} |")
    print("+" + "-" * total_width + "+")

    # Isi tabel
    for i, (penulis, judul, tahun) in enumerate(data, start=1):
        print(f"| {i:<3} | {penulis:<{max_penulis}} | {judul:<{max_judul}} | {tahun:<{max_tahun}} |")

    print("+" + "-" * total_width + "+")



