# Mini Sistem CLI - Tugas 9, 10, & 11

Kumpulan program Python berbasis CLI (Command Line Interface) yang membahas konsep struktur data, penyimpanan file, dan parsing data log.

## Daftar Isi
- [Tugas 9 - Refactor ke Dictionary](#tugas-9---refactor-ke-dictionary)
- [Tugas 10 - Integrasi File](#tugas-10---integrasi-file)
- [Tugas 11 - Parsing Data](#tugas-11---parsing-data)
- [Cara Menjalankan](#cara-menjalankan)

---

## Tugas 9 - Refactor ke Dictionary

**File:** `tugas9.py`

Merefactor sistem penyimpanan data dari list menjadi dictionary, dengan key berupa ID unik (auto-increment) dan value berupa nilai angka.

**Fitur:**
- Tampilkan data
- Tambah data
- Bubble Sort
- Insertion Sort
- Linear Search (cari berdasarkan nilai)
- Cari by ID (memanfaatkan akses langsung O(1) pada dictionary)
- Binary Search

---

## Tugas 10 - Integrasi File

**File:** `tugas10.py`

Melanjutkan sistem Tugas 9 dengan menambahkan integrasi file eksternal, sehingga data tidak hilang setelah program ditutup.

**Fitur tambahan:**
- Simpan data ke file (`data.txt`)
- Baca data secara otomatis saat program dijalankan

---

## Tugas 11 - Parsing Data

**File:** `tugas11.py`
**File pendukung:** `aktivitas.log`

Sistem pembaca file log yang mem-parsing setiap baris log menjadi data user dan aktivitas, lalu menganalisisnya.

**Fitur:**
- Baca dan parsing file log dengan format:
  ```
  [YYYY-MM-DD HH:MM:SS] USER:xxx | AKTIVITAS:yyy | keterangan
  ```
- Hitung jumlah tiap jenis aktivitas (login, logout, upload, download, dll)
- Hitung jumlah user unik menggunakan struktur data `set`
- Tampilkan isi log mentah

---

## Cara Menjalankan

1. Pastikan Python 3 sudah terinstall.
2. Clone atau download repository ini.
3. Jalankan salah satu file program, contoh:
   ```bash
   python tugas9.py
   python tugas10.py
   python tugas11.py
   ```
4. Ikuti menu yang muncul di layar.

> Catatan: untuk `tugas11.py`, pastikan file `aktivitas.log` berada di folder yang sama dengan file program.
