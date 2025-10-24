import json
import os
import pwinput
import time
import re
from prettytable import PrettyTable

USER_FILE = 'users.json'
DONASI_FILE = 'data_donasi.json'
LOKASI = [
    "Posko A - Sangatta",
    "Posko B - Bengalon",
    "Posko C - Muara Wahau",
    "Posko D - Rantau Pulung"
]
MAX_DONASI = 10_000_000
MAX_TOPUP = 10_000_000
MAX_SALDO = 50_000_000
LOGIN_ATTEMPTS = 3

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_json(file):
    if not os.path.exists(file):
        with open(file, 'w') as f:
            json.dump([], f)
    with open(file, 'r') as f:
        return json.load(f)

def save_json(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

#REGISTER
def register():
    clear_screen()
    users = load_json(USER_FILE)
    while True:
        username = input("Username baru: ").strip()
        if not re.match(r'^[A-Za-z0-9_]+$', username):
            print("Username hanya boleh berisi huruf, angka, dan underscore (_).")
            continue
        if any(u["username"] == username for u in users):
            print("Username sudah terdaftar.")
            continue
        password = pwinput.pwinput("Password: ")
        if not password:
            print("Password tidak boleh kosong.")
            continue
        users.append({
            "username": username,
            "password": password,
            "role": "User",
            "saldo": 0
        })
        save_json(USER_FILE, users)
        print("Registrasi berhasil!")
        input("Tekan Enter untuk kembali...")
        break

#LOGIN
def login():
    clear_screen()
    users = load_json(USER_FILE)
    attempts = LOGIN_ATTEMPTS
    while attempts > 0:
        username = input("Username: ").strip()
        password = pwinput.pwinput("Password: ").strip()
        if not username or not password:
            print("Username dan password tidak boleh kosong.")
            continue
        for u in users:
            if u["username"] == username and u["password"] == password:
                u["saldo"] = int(u.get("saldo", 0))
                print("Login berhasil. Menyiapkan akun...")
                time.sleep(1)
                return u
        attempts -= 1
        print(f"Username atau password salah. Sisa percobaan: {attempts}")
    print("Kesempatan login habis. Kembali ke menu utama.")
    time.sleep(1)
    return None

#NAMPILIN DONASI
def tampilkan_donasi(current_user=None):
    clear_screen()
    data = load_json(DONASI_FILE)
    if not data:
        print("Belum ada data donasi.")
        input("Tekan Enter untuk kembali...")
        return
    if current_user and current_user["role"] == "User":
        data = [d for d in data if d.get("username") == current_user["username"]]
    if not data:
        print("Tidak ada donasi untuk akun ini.")
        input("Tekan Enter untuk kembali...")
        return
    table = PrettyTable(["Nama Donatur", "Jumlah", "Metode", "Lokasi"])
    total = 0
    for d in data:
        jumlah_int = int(d.get("jumlah", 0))
        total += jumlah_int
        table.add_row([d.get("nama", "-"), f"Rp{jumlah_int:,}", d.get("metode", "-"), d.get("lokasi", "-")])
    print(table)
    if current_user and current_user["role"] == "Staff":
        print(f"\nTotal Donasi Keseluruhan: Rp{total:,}")
    else:
        print(f"\nTotal Donasi Anda: Rp{total:,}")
    input("\nTekan Enter untuk kembali...")

#NAMBAH DONASI
def tambah_donasi(current_user):
    clear_screen()
    data = load_json(DONASI_FILE)
    users = load_json(USER_FILE)

    while True:
        print("=== PILIH LOKASI DONASI ===")
        for i, l in enumerate(LOKASI, start=1):
            print(f"{i}. {l}")
        try:
            pilihan = int(input("Pilih lokasi (nomor): "))
            if 1 <= pilihan <= len(LOKASI):
                lokasi = LOKASI[pilihan - 1]
                break
            else:
                print("Pilihan lokasi tidak valid.")
        except ValueError:
            print("Input harus angka.")

    while True:
        nama = input("Nama Donatur: ").strip()
        if not re.match(r'^[A-Za-z0-9 ]+$', nama):
            print("Nama hanya boleh berisi huruf, angka, dan spasi.")
        elif not nama:
            print("Nama tidak boleh kosong.")
        else:
            break

    while True:
        try:
            jumlah = int(input("Jumlah Donasi: "))
        except ValueError:
            print("Jumlah harus angka.")
            continue
        if jumlah < 10_000:
            print("Minimal donasi Rp10.000.")
        elif jumlah > MAX_DONASI:
            print(f"Maksimal donasi Rp{MAX_DONASI:,}.")
        else:
            break

    #PEMBAYARAN
    if current_user["role"] == "Staff":
        metode = "Tunai (dicatat oleh Staff)"
        sisa_saldo = None
    else:
        for u in users:
            if u["username"] == current_user["username"]:
                saldo_user = int(u.get("saldo", 0))
                while saldo_user < jumlah:
                    print(f"Saldo tidak cukup (Rp{saldo_user:,}).")
                    top = input("Ingin top up? (y/n): ").lower()
                    if top == "y":
                        topup(current_user)
                        users = load_json(USER_FILE)
                        saldo_user = int(next(user['saldo'] for user in users if user['username'] == current_user['username']))
                    else:
                        print("Transaksi dibatalkan.")
                        input("Tekan Enter untuk kembali...")
                        return
                u["saldo"] = saldo_user - jumlah
                sisa_saldo = u["saldo"]
                save_json(USER_FILE, users)
                metode = "E-Wallet"
                break

    #NYIMPAN DONASI
    data.append({
        "username": current_user["username"],
        "nama": nama,
        "jumlah": jumlah,
        "metode": metode,
        "lokasi": lokasi
    })
    save_json(DONASI_FILE, data)

    #STRUK DONASI
    print("\n===== STRUK DONASI =====")
    print(f"Nama    : {nama}")
    print(f"Metode  : {metode}")
    print(f"Jumlah  : Rp{jumlah:,}")
    print(f"Lokasi  : {lokasi}")
    print("========================")
    print("Status Donasi : SUKSES")
    print("TERIMA KASIH ATAS DONASINYA")
    if current_user["role"] == "User":
        print(f"Sisa Saldo Anda: Rp{int(sisa_saldo):,}")
    else:
        print("(Staff tidak menggunakan saldo)")
    input("\nTekan Enter untuk kembali...")

#NGEDIT DONASI
def edit_donasi(current_user):
    clear_screen()
    data = load_json(DONASI_FILE)
    if not data:
        print("Belum ada data donasi.")
        input("Tekan Enter untuk kembali...")
        return
    while True:
        tampilkan_donasi(current_user)
        nama = input("Masukkan nama donatur yang ingin diedit: ").strip()
        for d in data:
            if d.get("nama", "").lower() == nama.lower() and (current_user["role"] == "Staff" or d.get("username") == current_user["username"]):
                print(f"\nEdit data donasi untuk {d['nama']}")
                if current_user["role"] == "Staff":
                    d['nama'] = input(f"Nama Donatur ({d['nama']}): ") or d['nama']
                    # Lokasi baru
                    while True:
                        for i, l in enumerate(LOKASI, start=1):
                            print(f"{i}. {l}")
                        pilih_lokasi = input(f"Pilih lokasi baru (1-{len(LOKASI)}) atau Enter untuk tidak mengubah: ").strip()
                        if not pilih_lokasi:
                            break
                        try:
                            idx = int(pilih_lokasi)
                            if 1 <= idx <= len(LOKASI):
                                d['lokasi'] = LOKASI[idx - 1]
                                break
                            else:
                                print("Pilihan lokasi tidak valid.")
                        except ValueError:
                            print("Input tidak valid.")
                else:
                    d['nama'] = input(f"Nama Donatur ({d['nama']}): ") or d['nama']
                    while True:
                        jumlah_baru = input(f"Jumlah Donasi ({d['jumlah']}): ").strip()
                        if not jumlah_baru:
                            break
                        try:
                            jumlah_baru = int(jumlah_baru)
                            if 10_000 <= jumlah_baru <= MAX_DONASI:
                                # cek saldo user
                                users = load_json(USER_FILE)
                                for u in users:
                                    if u["username"] == current_user["username"]:
                                        saldo_user = int(u.get("saldo", 0)) + int(d['jumlah'])
                                        if jumlah_baru > saldo_user:
                                            print("Saldo tidak cukup untuk jumlah baru.")
                                        else:
                                            u["saldo"] = saldo_user - jumlah_baru
                                            save_json(USER_FILE, users)
                                            d['jumlah'] = jumlah_baru
                                            break
                                break
                            else:
                                print(f"Jumlah harus antara Rp10.000 - Rp{MAX_DONASI:,}.")
                        except ValueError:
                            print("Jumlah harus angka.")
                    
                    # Edit Lokasi (User)
                    while True:
                        for i, l in enumerate(LOKASI, start=1):
                            print(f"{i}. {l}")
                        pilih_lokasi = input(f"Pilih lokasi baru (1-{len(LOKASI)}) atau Enter untuk tidak mengubah: ").strip()
                        if not pilih_lokasi:
                            break
                        try:
                            idx = int(pilih_lokasi)
                            if 1 <= idx <= len(LOKASI):
                                d['lokasi'] = LOKASI[idx - 1]
                                break
                            else:
                                print("Pilihan lokasi tidak valid.")
                        except ValueError:
                            print("Input tidak valid.")

                save_json(DONASI_FILE, data)
                print("Data donasi berhasil diperbarui.")
                input("Tekan Enter untuk kembali...")
                return
        print("Data donatur tidak ditemukan.\n")
        kembali = input("Ingin coba lagi? (y/n): ").lower()
        if kembali != 'y':
            break

#HAPUS DONASI
def hapus_donasi(current_user):
    clear_screen()
    data = load_json(DONASI_FILE)
    if not data:
        print("Belum ada data donasi.")
        input("Tekan Enter untuk kembali...")
        return
    while True:
        tampilkan_donasi(current_user)
        nama = input("Masukkan nama donatur yang ingin dihapus: ").strip()
        for i, d in enumerate(data):
            if d.get("nama", "").lower() == nama.lower() and (current_user["role"] == "Staff" or d.get("username") == current_user["username"]):
                konfirmasi = input(f"Yakin hapus donasi '{d['nama']}'? (y/n): ").lower()
                if konfirmasi == 'y':
                    del data[i]
                    save_json(DONASI_FILE, data)
                    print("Data donasi berhasil dihapus.")
                else:
                    print("Penghapusan dibatalkan.")
                input("Tekan Enter untuk kembali...")
                return
        print("Data donatur tidak ditemukan.")
        kembali = input("Ingin coba lagi? (y/n): ").lower()
        if kembali != 'y':
            break

#TOPAP
def topup(current_user):
    clear_screen()
    users = load_json(USER_FILE)
    while True:
        try:
            nominal = int(input("Masukkan nominal top up: "))
        except ValueError:
            print("Nominal harus angka.")
            continue
        if nominal < 15_000:
            print("Minimal top up Rp15.000.")
        elif nominal > MAX_TOPUP:
            print(f"Maksimal top up Rp{MAX_TOPUP:,}.")
        else:
            break
    for u in users:
        if u["username"] == current_user["username"]:
            saldo_sekarang = int(u.get("saldo", 0))
            if saldo_sekarang + nominal > MAX_SALDO:
                print(f"Saldo tidak boleh melebihi Rp{MAX_SALDO:,}")
                input("Tekan Enter untuk kembali...")
                return
            u["saldo"] = saldo_sekarang + nominal
            save_json(USER_FILE, users)
            print("Memproses top up...")
            time.sleep(0.8)
            print(f"Top up berhasil. Saldo saat ini: Rp{u['saldo']:,}")
            input("Tekan Enter untuk kembali...")
            return

#CEK SALDO
def cek_saldo(current_user):
    clear_screen()
    users = load_json(USER_FILE)
    for u in users:
        if u["username"] == current_user["username"]:
            print(f"Saldo Anda: Rp{int(u.get('saldo', 0)):,}")
            input("Tekan Enter untuk kembali...")
            return

#CARI DONASI
def cari_donasi(current_user):
    clear_screen()
    keyword = input("Masukkan nama donatur yang ingin dicari: ").strip().lower()
    if not keyword:
        print("Kata kunci pencarian tidak boleh kosong.")
        input("Tekan Enter untuk kembali...")
        return

    data = load_json(DONASI_FILE)
    data_pengguna = []

    # Filter data berdasarkan role
    if current_user["role"] == "User":
        data_pengguna = [d for d in data if d.get("username") == current_user["username"]]
    else:
        data_pengguna = data # Staff bisa melihat semua

    # Lakukan pencarian
    hasil_pencarian = [d for d in data_pengguna if keyword in d.get("nama", "").lower()]

    if not hasil_pencarian:
        print(f"Donasi dengan nama yang mengandung '{keyword}' tidak ditemukan.")
        input("Tekan Enter untuk kembali...")
        return

    # Tampilkan hasil menggunakan PrettyTable
    print(f"=== HASIL PENCARIAN UNTUK '{keyword}' ===")
    table = PrettyTable(["Nama Donatur", "Jumlah", "Metode", "Lokasi"])
    total = 0
    for d in hasil_pencarian:
        jumlah_int = int(d.get("jumlah", 0))
        total += jumlah_int
        table.add_row([d.get("nama", "-"), f"Rp{jumlah_int:,}", d.get("metode", "-"), d.get("lokasi", "-")])
    
    print(table)
    print(f"\nTotal Donasi Ditemukan: Rp{total:,}")
    input("\nTekan Enter untuk kembali...")

#URUTKAN DONASI
def urutkan_donasi(current_user):
    clear_screen()
    data = load_json(DONASI_FILE)
    data_pengguna = []

    # Filter data berdasarkan role
    if current_user["role"] == "User":
        data_pengguna = [d for d in data if d.get("username") == current_user["username"]]
    else:
        data_pengguna = data # Staff bisa melihat semua

    if not data_pengguna:
        print("Tidak ada data donasi untuk diurutkan.")
        input("Tekan Enter untuk kembali...")
        return

    print("Pilih kriteria pengurutan:")
    print("1. Nama (A-Z)")
    print("2. Nama (Z-A)")
    print("3. Jumlah (Terkecil ke Terbesar)")
    print("4. Jumlah (Terbesar ke Terkecil)")
    print("5. Lokasi (A-Z)")
    print("6. Lokasi (Z-A)")
    pilihan = input("Pilih (1-6): ").strip()

    data_terurut = []
    judul = "Data Donasi"
    
    if pilihan == "1":
        data_terurut = sorted(data_pengguna, key=lambda d: d.get("nama", "").lower())
        judul = "Donasi Diurutkan Berdasarkan Nama (A-Z)"
    elif pilihan == "2":
        data_terurut = sorted(data_pengguna, key=lambda d: d.get("nama", "").lower(), reverse=True)
        judul = "Donasi Diurutkan Berdasarkan Nama (Z-A)"
    elif pilihan == "3":
        data_terurut = sorted(data_pengguna, key=lambda d: int(d.get("jumlah", 0)))
        judul = "Donasi Diurutkan Berdasarkan Jumlah (Terkecil)"
    elif pilihan == "4":
        data_terurut = sorted(data_pengguna, key=lambda d: int(d.get("jumlah", 0)), reverse=True)
        judul = "Donasi Diurutkan Berdasarkan Jumlah (Terbesar)"
    elif pilihan == "5":
        data_terurut = sorted(data_pengguna, key=lambda d: d.get("lokasi", "").lower())
        judul = "Donasi Diurutkan Berdasarkan Lokasi (A-Z)"
    elif pilihan == "6":
        data_terurut = sorted(data_pengguna, key=lambda d: d.get("lokasi", "").lower(), reverse=True)
        judul = "Donasi Diurutkan Berdasarkan Lokasi (Z-A)"
    else:
        print("Pilihan tidak valid.")
        input("Tekan Enter untuk kembali...")
        return

    # Tampilkan hasil
    clear_screen()
    print(f"=== {judul} ===")
    table = PrettyTable(["Nama Donatur", "Jumlah", "Metode", "Lokasi"])
    total = 0
    for d in data_terurut:
        jumlah_int = int(d.get("jumlah", 0))
        total += jumlah_int
        table.add_row([d.get("nama", "-"), f"Rp{jumlah_int:,}", d.get("metode", "-"), d.get("lokasi", "-")])
    
    print(table)
    print(f"\nTotal Donasi Ditampilkan: Rp{total:,}")
    input("\nTekan Enter untuk kembali...")

#MENU USER
def menu_user(user):
    while True:
        clear_screen()
        print(f"=== MENU USER ({user['username']}) ===")
        print("1. Tambah Donasi")
        print("2. Lihat Donasi")
        print("3. Top Up Saldo")
        print("4. Cek Saldo")
        print("5. Cari Donasi")
        print("6. Urutkan Donasi")
        print("0. Logout")
        pilih = input("Pilih menu: ")
        if pilih == "1":
            tambah_donasi(user)
        elif pilih == "2":
            tampilkan_donasi(user)
        elif pilih == "3":
            topup(user)
        elif pilih == "4":
            cek_saldo(user)
        elif pilih == "5":
            cari_donasi(user)
        elif pilih == "6":
            urutkan_donasi(user)
        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk lanjut...")

#MENU STAFF
def menu_staff(user):
    while True:
        clear_screen()
        print(f"=== MENU STAFF ({user['username']}) ===")
        print("1. Tambah Donasi")
        print("2. Lihat Donasi (Total)")
        print("3. Edit Donasi")
        print("4. Hapus Donasi")
        print("5. Cari Donasi")
        print("6. Urutkan Donasi")
        print("0. Logout")
        pilih = input("Pilih menu: ")
        if pilih == "1":
            tambah_donasi(user)
        elif pilih == "2":
            tampilkan_donasi(user)
        elif pilih == "3":
            edit_donasi(user)
        elif pilih == "4":
            hapus_donasi(user)
        elif pilih == "5":
            cari_donasi(user)
        elif pilih == "6":
            urutkan_donasi(user)
        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk lanjut...")

#MENU UTAMA
def main():
    while True:
        clear_screen()
        print("=== SISTEM DONASI ===")
        print("1. Login")
        print("2. Register")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            user = login()
            if user:
                if user["role"] == "Staff":
                    menu_staff(user)
                else:
                    menu_user(user)
        elif pilihan == "2":
            register()
        elif pilihan == "0":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk lanjut...")

main()
