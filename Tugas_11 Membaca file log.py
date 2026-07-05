#Nama Program : Sistem Pembaca File Log - Tugas 11
#Nim           : 301250033
#Nama Pembuat  : Muhammad Fadil Almubarok Khalili
#Tanggal       : 05 Juli 2026
#Deskripsi     : Membaca file log, menghitung jumlah aktivitas,
#                dan menghitung user unik menggunakan set

def baca_log(path):
    entri = []
    try:
        file = open(path, "r")
    except FileNotFoundError:
        print("File", path, "tidak ditemukan!")
        return entri

    for baris in file:
        baris = baris.strip()
        if baris == "":
            continue
        try:
            bagian = baris.split(" | ")
            user = bagian[0].split("USER:")[1]
            aktivitas = bagian[1].split("AKTIVITAS:")[1]

            entri.append({"user": user, "aktivitas": aktivitas})
        except (IndexError, ValueError):
            continue
    file.close()
    return entri

def analisis_log(entri):
    # User unik pakai set
    user_unik = set()
    for e in entri:
        user_unik.add(e["user"])

    # Hitung jumlah tiap aktivitas pakai dictionary biasa
    jumlah_aktivitas = {}
    for e in entri:
        a = e["aktivitas"]
        if a in jumlah_aktivitas:
            jumlah_aktivitas[a] += 1
        else:
            jumlah_aktivitas[a] = 1

    return user_unik, jumlah_aktivitas

def tampil_laporan(path):
    print("\nLaporan Analisis File Log")
    print("File:", path)

    entri = baca_log(path)
    if not entri:
        return

    print("Total baris valid:", len(entri))

    user_unik, jumlah_aktivitas = analisis_log(entri)

    print("\nJumlah Aktivitas:")
    for aktivitas, jumlah in jumlah_aktivitas.items():
        print(" -", aktivitas, ":", jumlah)

    print("\nUser Unik (pakai set):")
    print(" Jumlah user unik:", len(user_unik))
    print(" Daftar user     :", user_unik)

def tampil_isi_file(path):
    try:
        file = open(path, "r")
        print("\nIsi file", path, ":")
        print(file.read())
        file.close()
    except FileNotFoundError:
        print("File", path, "tidak ditemukan.")

# Menu program
while True:
    print("\n===== SISTEM PEMBACA FILE LOG =====")
    print("nim          : 301250033")
    print("nama pembuat : Muhammad Fadil Almubarok Khalili")
    print("Tugas: Tugas 11 - Parsing Data")
    print("\n===== MENU =====")
    print("1. Analisis log (aktivitas.log)")
    print("2. Analisis log dari file lain")
    print("3. Tampilkan isi log mentah")
    print("4. Keluar")

    pilih = input("\nPilih menu: ")

    if pilih == "1":
        tampil_laporan("aktivitas.log")
    elif pilih == "2":
        file_lain = input("Masukkan nama file log: ")
        tampil_laporan(file_lain)
    elif pilih == "3":
        tampil_isi_file("aktivitas.log")
    elif pilih == "4":
        print("\nProgram selesai.")
        break
    else:
        print("\nPilihan tidak valid.")