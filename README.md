# SISTEM-DONASI
# Kelompok 1
Muhammad Arham Anugrah | 2509116044

Risky Farel Wijaya | 2509116066   

Muhammad Davi Aditya Pratama | 2503116070

Jihan Shafira Rahmah | 2509116073

# Flowchart
Flowchart yang kami buat terbagi menjadi 3 bagian, yaitu: Menuu utama, Menu role staff dan menu user.

# 1. Menu utama.
   Pada flowchart bagian pertama ini terdapat 3 pilihan menu yaitu Login, Register dan keluar. 
 
# 2. Menu role staff
   Flowchart untuk role staff ini terdapat 6 pilihan menu yaitu Tambah Donasi, Lihat Donasi, Edit Donasi, Hapus Donasi, Kelola Posko, dan Logout.
   
# 3. Menu role user
   Flowchart untuk role user memiliki 5 pilihan menu yaitu Tambah Donasi, Lihat Donasi, Top Up Saldo, Cek Saldo, dan Logout.

# LIBRARY
# 1. JSON
Pada program sistem donasi ini, kami menggunakan 3 JSON untuk mendukung jalannya program. 

A. users.json

<img width="894" height="590" alt="Screenshot 2025-10-23 103434" src="https://github.com/user-attachments/assets/0899b815-c856-45c1-be30-88b1e6e5d8d1" />

B. data_donasi.json

<img width="543" height="791" alt="Screenshot 2025-10-26 172234" src="https://github.com/user-attachments/assets/3ae63e8e-ce9c-4563-8fd8-57b2d26cf1cd" />

C. Posko.json


# 2. os
<img width="553" height="267" alt="Screenshot 2025-10-26 172436" src="https://github.com/user-attachments/assets/74b30d6a-71f9-41e2-abf5-54c99b53b941" />

# 3. pwinput
<img width="174" height="66" alt="Screenshot 2025-10-26 004320" src="https://github.com/user-attachments/assets/ccb3a11f-110f-4d92-80e2-40cc325e56ce" />

# 4. time
<img width="482" height="74" alt="Screenshot 2025-10-23 104946" src="https://github.com/user-attachments/assets/6ee59416-1416-47f1-9162-99ec32563950" />

# 5. re
<img width="722" height="215" alt="Screenshot 2025-10-26 143222" src="https://github.com/user-attachments/assets/85306e75-f723-475f-a7f1-1a31b1c36127" />

# 6. PrettyTable
<img width="718" height="218" alt="Screenshot 2025-10-26 172746" src="https://github.com/user-attachments/assets/df4a7588-83ac-40fc-9ba0-1866f7329d71" />

# Menu Utama   
Ketika program ini dijalankan, maka akan masuk ke dalam menu utama yang berisi 3 pilihan menu yaitu Login, Register dan keluar.

<img width="312" height="155" alt="Screenshot 2025-10-19 211549" src="https://github.com/user-attachments/assets/2a3e22ec-0aff-4b8d-92eb-f515bae47e53" />

Untuk masuk ke masing-masing menu, cukup menginputkan nomor dari pilihan menu tersebut. Contohnya masuk menu login, input angka "1"

# RUN 1
Pilihan menu pertama pada sistem ini yaitu Login. Untuk masuk menu login, input angka "1".

<img width="221" height="143" alt="Screenshot 2025-10-26 004259" src="https://github.com/user-attachments/assets/1f7724fc-85c2-41b7-95d8-7b538af9e6a1" />

# RUN 2
Setelah masuk ke menu login, maka akan disuruh untuk mengisi username dan password. Untuk username dan password terbagi menjadi dua role, yaitu staff dan user. Untuk role staff, usernamenya "staff" dan untuk passwordnya adalah "12345". Lalu, untuk role user username dan password disesuaikan dengan yang telah dibuat sebelumnya. Pada sistem login ini, kami menggunakan library pwinput untuk melindungi password agar tidak terlihat saat proses login.

Contoh login role staff:

<img width="174" height="66" alt="Screenshot 2025-10-26 004320" src="https://github.com/user-attachments/assets/e57d1b14-2de8-43e5-b3a7-66bbb3f7f561" />

Contoh login role user:

<img width="160" height="67" alt="Screenshot 2025-10-26 113958" src="https://github.com/user-attachments/assets/fabea4ae-2912-4646-894b-6fe085218450" />

# RUN 3
Pilihan menu kedua yaitu Register. Menu ini berfungsi untuk user membuat username dan password terlebih dahulu sebelum menggunakan sistem. Untuk masuk pada menu Register input angka "2".

<img width="227" height="131" alt="Screenshot 2025-10-23 222409" src="https://github.com/user-attachments/assets/6ac62c83-9c2b-4d75-aef2-9999a099882b" />

# RUN 4
Seteleh masuk menu Register, maka akan disuruh untuk mengisi username baru dan password. Pertama isi dulu username pada "Username baru: ", lalu enter dan isi "Password: ".

<img width="263" height="42" alt="Screenshot 2025-10-23 222449" src="https://github.com/user-attachments/assets/4306d40f-4806-4c34-a5ae-7cc7de5acbb5" />

Sebagai contoh, kami membuat username baru dengan nama Arham dan password 000.

# RUN 5
Setelah memasukkan username baru dan password, tekan enter pada keyboard hingga ada output "Registrasi berhasil" seperti gambar dibawah ini.

<img width="233" height="73" alt="Screenshot 2025-10-23 222456" src="https://github.com/user-attachments/assets/4af3399f-ede4-44bb-88c0-4629587ae6e0" />

# RUN 6
Menu ketiga sekaligus terakhir pada menu utama kali ini adalah Keluar. Menu ini berfungsi jika kita ingin keluar pada sistem ini. Untuk keluar pada menu ini, cukup inputkan angka "0", lalu enter. 

<img width="207" height="132" alt="Screenshot 2025-10-26 115039" src="https://github.com/user-attachments/assets/e68a0953-d035-4bc9-b926-dbce3139c9e4" />

# RUN 7
Hasil yang akan terjadi ketika memilih menu Keluar adalah seperti ini:

<img width="279" height="139" alt="image" src="https://github.com/user-attachments/assets/c1176f92-d3dd-4cd1-997a-bdfb27e6a34f" />

# Role
Pada sistem ini terdapat 2 role yaitu Staff dan user(Donatur). Berikut panduan penggunaan untuk role staff. 
# RUN 1 Staff
Untuk masuk sebagai staff, Login dengan username staff dan password 12345. 

<img width="211" height="91" alt="Screenshot 2025-10-20 204612" src="https://github.com/user-attachments/assets/907df82c-9880-4c52-ad37-4cfe57f586d5" />
  
Karena pada sistem ini kami gunakan library pwinput, password yang diisi pada saat login otomatis akan disembunyikan atau diganti dengan tanda *****

# RUN 2 Staff
Pada menu staff, terdapat 6 pilihan menu yang dapat diakses, seperti: 
1. Tambah Donasi
2. Lihat Donasi
3. Edit Donasi
4. Hapus Donasi
5. Kelola Posko
0. Logout

<img width="594" height="288" alt="image" src="https://github.com/user-attachments/assets/de1a05cd-522a-4254-9e52-5abf8999ff89" />

Untuk mengakses menu-menu tersebut, cukup input nomor pada menu tersebuut. Contoh untuk mengakses menu tambah donasi, input angka 1 lalu enter untuk masuk ke menu tersebut. 
# RUN 3 Staff (Tambah Donasi)
Menu pertama pada role staff yaitu Tambah Donasi. Menu ini berfungsi agar para staff dapat ikut berdonasi melalui sistem ini. Untuk masuk menu ini, input angka 1 lalu enter. 

<img width="257" height="247" alt="Screenshot 2025-10-26 134728" src="https://github.com/user-attachments/assets/fe599d7d-894c-4b0d-bfe0-4a9c450cd77d" />

# RUN 4 Staff (Tambah Donasi)
# RUN 5 Staff (Tambah Donasi)
# RUN 6 Staff (Tambah Donasi)

# RUN  Staff (Lihat Donasi)
Menu kedua pada role staff yaitu Lihat Donasi. Menu ini memiliki fungsi agar para staff dapat memantau atau melihat data donasi beserta jumlah donasi yang masuk. Masuk ke menu ini cukup input angka 2 lalu enter. 

<img width="724" height="281" alt="Screenshot 2025-10-26 134804" src="https://github.com/user-attachments/assets/ba9e478f-b6f6-48fd-9cb2-c5959345c429" />

# RUN  Staff (Edit Donasi)
Selanjutnya pada menu ketiga di role staff adalah Edit Donasi. Tujuan dari menu ini adalah untuk staff dapat melakukan pengubahan pada data donasi jika terjadi kesalahan input pada user maupun staff yang lain. Pada menu ini yang dapat di edit adalah nama donatur dan posko donasi. Untuk masuk ke menu ini, input angka 3, lalu enter. 

<img width="256" height="244" alt="Screenshot 2025-10-26 140035" src="https://github.com/user-attachments/assets/551e9ebd-11da-48bb-8664-f0085925d792" />

# RUN  Staff (Edit Donasi)
Setelah masuk pada menu, tekan enter sekali untuk lanjut mengedit dan setelah itu isi nama donatur yang sesuai pada sistem yang ingin di edit. Lalu, tekan enter kembali. 


# RUN  Staff (Edit Donasi)
Setelah mengisi nama donatur  dan enter, maka akan muncul untuk mengedit nama donatur. Jika yang ingin di edit adalah nama dari donatur, maka input nama baru dari donatur tersebut. 

<img width="458" height="101" alt="Screenshot 2025-10-26 141344" src="https://github.com/user-attachments/assets/b30e1e4b-af55-4f7b-92d6-11a9bdcd565e" />

# RUN  Staff (Edit Donasi)
# RUN 10 Staff (Edit Donasi)

# RUN  Staff (Hapus Donasi)
Lanjut ke menu keempat yaitu Hapus Donasi. Menu ini berfungsi agar para staff dapat menghapus data donasi yang tidak valid. Untuk masuk ke menu ini input angka 4, lalu enter.

<img width="254" height="247" alt="image" src="https://github.com/user-attachments/assets/69afbe78-7e5f-4c08-9b3c-cf31a6f02723" />

# RUN  Staff (Hapus Donasi)
# RUN  Staff (Hapus Donasi)
Cukup input nama donatur untuk menghapus data donasi. Setelah menginput nama donatur yang ingin dihapus, tekan enter.

<img width="439" height="57" alt="Screenshot 2025-10-26 141927" src="https://github.com/user-attachments/assets/de54056f-2fbb-4ad5-9186-6ec49db90d0f" />

# RUN  Staff (Hapus Donasi)
Jika udah menginput dan tekan enter, maka akan muncul output verifikasi apakah yakin untuk menghapus atau tidak. Jika yakin untuk menghapus input "y" lalu tekan enter, jika tidak yakin maka input "n" lalu enter untuk membatalkan.

<img width="431" height="52" alt="Screenshot 2025-10-26 142324" src="https://github.com/user-attachments/assets/8da9bf8f-0d8b-49ae-9800-31dfabc88984" />

# RUN  Staff (Hapus Donasi)
Jika yakin dan telah tekan enter maka akan memberikan output "Data donasi berhasil dihapus".

<img width="434" height="126" alt="Screenshot 2025-10-26 142332" src="https://github.com/user-attachments/assets/a863c05b-d2de-41ad-87ff-81d1a8d10236" />

# RUN  Staff (Hapus Donasi)
Jika tidak yakin atau batal menghapus dan tekan enter, maka akan memberikan output.

<img width="461" height="91" alt="Screenshot 2025-10-26 143102" src="https://github.com/user-attachments/assets/e05d4cdc-69cd-40d9-916f-e16b59cf25e1" />

# RUN  Staff (Kelola Posko)

# RUN Staff (Kelola Posko)
# RUN Staff (Kelola Posko)
# RUN Staff (Kelola Posko)
# Run  Staff (Keluar)
# Role
Lanjut untuk role yang kedua adalah Role User. Berikut panduan penggunaan untuk role staff.
# Run 1 user
  Untuk masuk sebagai user, Login dengan username dan password yang sudah dibuat sebelumnya. Sebagai contoh untuk masuk sebagai user, login dengan username Davi     dan password 1234, lalu enter. Pada menu login, password akan otomatis disembunyikan oleh sistem karena sudah menggunakan library pwinput.
  
   <img width="160" height="67" alt="Screenshot 2025-10-26 113958" src="https://github.com/user-attachments/assets/ca945ae1-4a33-4c2c-bb07-29d6d17b1131" />

# Run 2 user
Pada menu user, terdapat 5 pilihan menu yang dapat diakses, seperti: 
1. Tambah Donasi
2. Lihat Donasi
3. Top Up saldo
4. Cek Saldo
0. Logout


# Run 3 user (Tambah Donasi)
# Run 4 user (Tambah Donasi)
# Run 5 user (Tambah Donasi)

# Run user (Lihat Donasi)
# Run user (Lihat Donasi)
# Run user (Lihat Donasi)

# Run  user (Top up Saldo)
<img width="421" height="161" alt="Screenshot (38)" src="https://github.com/user-attachments/assets/5da200c8-ce99-437b-bb7a-fd0a3d59eb5a" />

# Run  user (Top up Saldo)
# Run  user (Top up Saldo)

# Run  user (Cek Saldo)
# Run  user (Cek Saldo)

# Run  user (Keluar)
