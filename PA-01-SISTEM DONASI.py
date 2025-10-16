import json
import stdiomask
import os
from prettytable import PrettyTable

DATA_FILE = 'data_donasi.json'
SALDO_FILE = 'data_saldo.json'
MAX_DONASI = 1000000

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

if not os.path.exists(SALDO_FILE):
    with open(SALDO_FILE, 'w') as f:
        json.dump({}, f)

users = {
    "staff": {"password": 123, "role": "Staff"},
    "user": {"password": 456, "role": "User"},
}

lokasi_donasi = {
    "1": "Kantor Pusat - Jl. Pramuka No. 123",
    "2": "Cabang Utara - Jl. Perjuangan No. 456",
    "3": "Cabang Selatan - Jl. Perjuangan Baru No. 789"
}

def load_data(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return [] if 'donasi' in file_path else {}

def save_data(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def cek_saldo(username):
    saldo_data = load_data(SALDO_FILE)
    return saldo_data.get(username, 0)

def topup_saldo(username):
    try:
        print("\n=== TOP UP SALDO ===")
        saldo_data = load_data(SALDO_FILE)
        saldo_sekarang = saldo_data.get(username, 0)
        
        print(f"Saldo saat ini: Rp {saldo_sekarang:,}")
        jumlah_topup = int(input("Masukkan jumlah top up: Rp "))
        
        if jumlah_topup <= 0:
            print("Jumlah top up harus lebih dari 0!")
            return
        
        saldo_data[username] = saldo_sekarang + jumlah_topup
        save_data(SALDO_FILE, saldo_data)
        
        print("\nTop up berhasil!")
        print(f"Saldo baru: Rp {saldo_data[username]:,}")
    except ValueError:
        print("Input tidak valid! Masukkan angka.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

#FUNGSI UTAMA CRUD
#READ

def lihat_donasi():
    data = load_data(DATA_FILE)
    if not data:
        print("\nBelum ada data donasi.")
        return None

    table = PrettyTable()
    table.field_names = ["No", "Nama", "Metode", "Lokasi", "Jumlah", "Status"]

    for i, p in enumerate(data, start=1):
        table.add_row([
            i,
            p.get('nama_pendonasi', ''),
            p.get('method', ''),
            p.get('lokasi', ''),
            f"Rp {p.get('jumlah', 0):,}",
            p.get('status', '')
        ])
    print("\nData Donasi:")
    print(table)
    return data

#CREATE
def donasi(username):
    try:
        nama = input("Masukkan nama pendonasi: ")
        
        print("\n=== PILIH METODE DONASI ===")
        print("1. E-Wallet (Pakai Saldo)")
        print("2. Cash (Datang ke Lokasi)")
        method = input("Pilih method (1/2): ")

        if method == "1":
            method_name = "E-WALLET"
            saldo_sekarang = cek_saldo(username)
            print(f"\nSaldo Anda saat ini: Rp {saldo_sekarang:,}")
            jumlah = int(input(f"Masukkan jumlah donasi (Max: Rp {MAX_DONASI:,}): Rp "))
            
            if not 0 < jumlah <= MAX_DONASI:
                print(f"Jumlah donasi tidak valid! Harus antara Rp 1 dan Rp {MAX_DONASI:,}.")
                return
            
            if saldo_sekarang < jumlah:
                print("\nSaldo tidak cukup!")
                if input("Apakah Anda ingin top up saldo? (y/n): ").lower() == 'y':
                    topup_saldo(username)
                return
            
            lokasi = "Online"
            status = "SUKSES"
            saldo_data = load_data(SALDO_FILE)
            saldo_data[username] = saldo_sekarang - jumlah
            save_data(SALDO_FILE, saldo_data)
            
        elif method == "2":
            method_name = "CASH"
            print("\n=== PILIH LOKASI DONASI ===")
            for key, value in lokasi_donasi.items():
                print(f"{key}. {value}")
            pilih_lokasi = input("Pilih lokasi (1-3): ")
            
            if pilih_lokasi not in lokasi_donasi:
                print("Lokasi tidak valid!")
                return
            
            lokasi = lokasi_donasi[pilih_lokasi]
            jumlah = int(input(f"Masukkan jumlah donasi (Max: Rp {MAX_DONASI:,}): Rp "))
            
            if not 0 < jumlah <= MAX_DONASI:
                print(f"Jumlah donasi tidak valid! Harus antara Rp 1 dan Rp {MAX_DONASI:,}.")
                return
            
            status = "PENDING - Silahkan datang ke lokasi"
        else:
            print("Pilihan tidak valid!")
            return

        data = load_data(DATA_FILE)
        data.append({
            "nama_pendonasi": nama, "method": method_name, "lokasi": lokasi,
            "jumlah": jumlah, "status": status
        save_data(DATA_FILE, data)

        print("\n" + "="*40)
        print("=" + " "*13 + "STRUK DONASI" + " "*13 + "=")
        print("="*40)
        print(f"Nama     : {nama}\nMethod   : {method_name}\nLokasi   : {lokasi}")
        print(f"Jumlah   : Rp {jumlah:,}\nStatus   : {status}")
        print("="*40)
        
        if method == "1":
            print(f"Sisa Saldo: Rp {cek_saldo(username):,}")
            print("="*40)
        
        print("TERIMA KASIH ATAS DONASINYA")

        if method == "2":
            print("\nApakah Anda ingin menyelesaikan donasi ini sekarang?")
            if input("1. Ya\n2. Nanti saja\nPilih (1/2): ") == "1":
                data[-1]['status'] = 'SUKSES'
                save_data(DATA_FILE, data)
                print("\nDonasi tunai Anda telah dikonfirmasi. Status diperbarui menjadi SUKSES.")
        
    except ValueError:
        print("Input tidak valid! Pastikan memasukkan angka.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

#UPDATE
def ubah_donasi():
    print("\n=== UBAH DATA DONASI ===")
    data = lihat_donasi()
    if not data:
        return
    
    try:
        nomor = int(input("\nMasukkan nomor donasi yang ingin diubah: "))
        if not 0 < nomor <= len(data):
            print("Nomor tidak valid!")
            return
        
        donasi_dipilih = data[nomor - 1]
        print(f"\nData yang akan diubah: [Nama: {donasi_dipilih['nama_pendonasi']}, Jumlah: Rp {donasi_dipilih['jumlah']:,}, Status: {donasi_dipilih['status']}]")
        
        print("\nApa yang ingin Anda ubah?")
        print("1. Nama Pendonasi\n2. Jumlah Donasi\n3. Status Donasi")
        pilihan_field = input("Pilih (1-3): ")

        if pilihan_field == '1':
            nama_baru = input("Masukkan nama baru: ")
            donasi_dipilih['nama_pendonasi'] = nama_baru
        elif pilihan_field == '2':
            jumlah_baru = int(input("Masukkan jumlah baru: Rp "))
            donasi_dipilih['jumlah'] = jumlah_baru
        elif pilihan_field == '3':
            status_baru = input("Masukkan status baru (e.g., SUKSES, DIBATALKAN): ").upper()
            donasi_dipilih['status'] = status_baru
        else:
            print("Pilihan tidak valid.")
            return

        save_data(DATA_FILE, data)
        print("\nData berhasil diubah!")
        lihat_donasi()

    except ValueError:
        print("Input tidak valid! Masukkan nomor.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

#DELETE
def hapus_donasi():
    data = lihat_donasi()
    if not data:
        return
    try:
        nomor = int(input("\nMasukkan nomor donasi yang ingin dihapus: "))
        if not 0 < nomor <= len(data):
            print("Nomor tidak valid!")
            return
        
        if input(f"Yakin ingin menghapus donasi '{data[nomor-1]['nama_pendonasi']}'? (y/n): ").lower() == 'y':
            data.pop(nomor - 1)
            save_data(DATA_FILE, data)
            print("Donasi berhasil dihapus!")
            lihat_donasi()
        else:
            print("Penghapusan dibatalkan.")
    except ValueError:
        print("Input tidak valid!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def login():
    print("=== SISTEM LOGIN PENCATATAN DONASI ===")
    for attempts in range(3, 0, -1):
        username = input("Username (staff/user): ").lower()
        try:
            password = int(stdiomask.getpass("Password (hanya angka): "))
            if username in users and users[username]["password"] == password:
                print(f"Login berhasil sebagai {users[username]['role']}")
                return username, users[username]["role"]
            else:
                print(f"Username atau password salah. Sisa kesempatan: {attempts-1}\n")
        except ValueError:
            print(f"Password harus berupa angka! Sisa kesempatan: {attempts-1}\n")
        except (KeyboardInterrupt, EOFError):
            print("\nProses input dibatalkan.")
            return None, None
    print("Kesempatan login habis. Program dihentikan.")
    return None, None

def main():
    username, role = login()
    if not role:
        return

    while True:
        print("\n" + "="*40)
        print(f"=== MENU UTAMA - ROLE: {role.upper()} ===")
        print("="*40)
        
        if role == "Staff":
            print("1. Lihat Semua Donasi\n2. Hapus Donasi\n3. Ubah Data Donasi\n0. Keluar")
        else:
            print("1. Donasi\n2. Cek Saldo\n3. Top Up Saldo\n4. Lihat Riwayat Donasi Saya\n0. Keluar")

        pilihan = input("\nPilih menu: ")

        if role == "Staff":
            if pilihan == "1": lihat_donasi()
            elif pilihan == "2": hapus_donasi()
            elif pilihan == "3": ubah_donasi()
            elif pilihan == "0": break
            else: print("Pilihan tidak valid!")
        elif role == "User":
            if pilihan == "1": donasi(username)
            elif pilihan == "2": print(f"\nSaldo Anda: Rp {cek_saldo(username):,}")
            elif pilihan == "3": topup_saldo(username)
            elif pilihan == "4":
                data = load_data(DATA_FILE)
                user_donations = [d for d in data if d.get('username') == username]
                if not user_donations:
                    print("\nAnda belum memiliki riwayat donasi.")
                else:
                    table = PrettyTable()
                    table.field_names = ["No", "Nama", "Method", "Lokasi", "Jumlah", "Status"]
                    for i, p in enumerate(user_donations, start=1):
                        table.add_row([i, p['nama_pendonasi'], p['method'], p['lokasi'], f"Rp {p['jumlah']:,}", p['status']])
                    print("\nRiwayat Donasi Anda:")
                    print(table)
            elif pilihan == "0": break
            else: print("Pilihan tidak valid!")
    
    print("Keluar dari program. Sampai jumpa!")

if __name__ == "__main__":
    main()
