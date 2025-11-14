📘 Project CRUD Data Buku (Python Dasar) v1

Project ini adalah program Python sederhana untuk mengelola data buku menggunakan konsep CRUD (Create, Read, Update, Delete).
Semua data buku disimpan dalam file teks bernama database.txt, sehingga mudah dipahami untuk pemula tanpa memerlukan database eksternal.

✨ Fitur Program

Program ini memiliki fitur-fitur berikut:

1. Create (Menambah Data Buku)

Menambahkan data buku baru ke dalam database.txt

Format data:

No | Penulis | Judul | Tahun

2. Read (Menampilkan Data Buku)

Menampilkan semua data yang tersimpan dalam bentuk tabel sederhana.

Data dibaca langsung dari file database.txt.

3. Update (Mengubah Data Buku)

Memilih nomor buku yang ingin diperbarui.

Data lama akan diganti dengan data baru yang diinput oleh pengguna.

4. Delete (Menghapus Buku)

Menghapus data buku berdasarkan nomor urutan.

🗂️ Struktur Folder Project
CRUD_Project/
│
├── main.py          # File utama untuk menjalankan program
├── crud.py          # File yang berisi fungsi CRUD
├── database.txt     # File untuk menyimpan data buku
└── README.md        # Dokumentasi project (file ini)

▶️ Cara Menjalankan Program

- Pastikan Python sudah terinstall.
- Buka folder project lewat terminal atau cmd.
- Jalankan perintah:
- python main.py


Pilih menu sesuai kebutuhan:

1 → Tambah buku
2 → Lihat buku
3 → Update buku
4 → Hapus buku
5 → Keluar

📄 Contoh Isi database.txt
1 | Fachry | Black Sun | 2025
2 | Andi   | Dunia Kabel | 2023

🎯 Tujuan Project

- Melatih konsep dasar Python
- Memahami bagaimana data disimpan dalam file
- Belajar membuat fungsi terpisah (modular)
- Fondasi sebelum ke database nyata seperti SQLite / MySQL

💡 Catatan Tambahan
- Jika data tidak berurutan, program akan otomatis men-generate nomor urut.
- Kamu bebas memperluas project (misalnya menambah fitur pencarian, sorting, atau export ke CSV).
Jika data tidak berurutan, program akan otomatis men-generate nomor urut.

Kamu bebas memperluas project (misalnya menambah fitur pencarian, sorting, atau export ke CSV).
