#Nama Program : Mini Sistem CLI - Tugas 10 (Integrasi File)
#Nim           : 301250033
#Nama Pembuat  : Muhammad Fadil Almubarok Khalili
#Tanggal       : 05 Juli 2026
#Deskripsi     : Refactor sistem dari list ke dictionary untuk penyimpanan
#                dan pencarian yang lebih optimal
data = {
    1: 45, 2: 12, 3: 78, 4: 23, 5: 56,
    6: 89, 7: 11, 8: 67, 9: 34, 10: 90,
    11: 21, 12: 43, 13: 65, 14: 10, 15: 99,
    16: 54, 17: 32, 18: 76, 19: 18, 20: 5
}

def next_id():
    return max(data) + 1 if data else 1

def tampil():
    print("\nData saat ini:")
    for id, nilai in data.items():
        print("ID", id, ":", nilai)
    print("Total data:", len(data))

def tambah():
    jumlah = int(input("Berapa data yang ingin ditambahkan? "))
    for i in range(jumlah):
        angka = int(input("Masukkan data ke-" + str(i+1) + ": "))
        id_baru = next_id()
        data[id_baru] = angka
        print("Disimpan dengan ID", id_baru)
    print("Data berhasil ditambahkan!")

def bubble():
    arr = list(data.values())
    langkah = 0
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            langkah += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print("\nHasil Bubble Sort:", arr)
    print("Jumlah perbandingan:", langkah)

def insertion():
    arr = list(data.values())
    langkah = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            langkah += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    print("\nHasil Insertion Sort:", arr)
    print("Jumlah perbandingan:", langkah)

def linear():
    tampil()
    target = int(input("\nCari angka: "))
    langkah = 0
    hasil = []
    for id, nilai in data.items():
        langkah += 1
        if nilai == target:
            hasil.append(id)
    if hasil:
        print("Data", target, "ditemukan di ID:", hasil)
    else:
        print("Data tidak ditemukan.")
    print("Jumlah langkah:", langkah)

def cari_id():
    id_cari = int(input("\nMasukkan ID yang dicari: "))
    if id_cari in data:
        print("ID", id_cari, "nilainya:", data[id_cari])
    else:
        print("ID", id_cari, "tidak ditemukan.")
    print("Jumlah langkah: 1 (langsung ketemu karena dictionary)")

def binary():
    arr = sorted(data.values())
    print("\nData Terurut:", arr)
    target = int(input("\nCari angka: "))
    awal = 0
    akhir = len(arr) - 1
    langkah = 0
    while awal <= akhir:
        tengah = (awal + akhir) // 2
        langkah += 1
        if arr[tengah] == target:
            print("Data ditemukan di posisi terurut ke-", tengah)
            print("Jumlah langkah:", langkah)
            return
        elif target < arr[tengah]:
            akhir = tengah - 1
        else:
            awal = tengah + 1
    print("Data tidak ditemukan.")
    print("Jumlah langkah:", langkah)

# Menu program
while True:
    print("\n===== MINI SISTEM SEARCHING & SORTING (Dictionary) =====")
    print("nim          : 301250033")
    print("nama pembuat : Muhammad Fadil Almubarok Khalili")
    print("tugas        : pertemuan 9 - Refactor ke Dictionary")
    print("\n===== MENU =====")
    print("1. Tampilkan Data")
    print("2. Tambah Data")
    print("3. Bubble Sort")
    print("4. Insertion Sort")
    print("5. Linear Search (cari nilai)")
    print("6. Cari by ID (dictionary lookup)")
    print("7. Binary Search")
    print("8. Keluar")

    pilih = input("\nPilih menu: ")

    if pilih == "1":
        tampil()
    elif pilih == "2":
        tambah()
    elif pilih == "3":
        bubble()
    elif pilih == "4":
        insertion()
    elif pilih == "5":
        linear()
    elif pilih == "6":
        cari_id()
    elif pilih == "7":
        binary()
    elif pilih == "8":
        print("\nProgram selesai.")
        break
    else:
        print("\nPilihan tidak valid.")