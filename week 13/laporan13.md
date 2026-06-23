# Laporan Praktikum Jaringan Komputer - Modul 13

## Identitas Praktikan
### Nama: Didit Septa Putra
### NIM: 103072400071
### Kelas: IF-04-01
---

## 1. Tujuan Praktikum

Berdasarkan modul praktikum Jaringan Komputer Semester Genap 2025/2026, tujuan dari Modul 13 adalah:
### 1. Mahasiswa dapat menginvestigasi cara kerja Ethernet dan ARP menggunakan Wireshark
### 2 Mahasiswa mampu menganalisis struktur frame Ethernet
### 3. Mahasiswa memahami mekanisme Address Resolution Protocol (ARP)
### 4 Mahasiswa dapat menganalisis cache ARP dan proses resolusi alamat

---

## 2. Langkah Kerja

Berikut adalah langkah-langkah yang dilakukan selama praktikum Modul 13:

### 2.1 Persiapan dan Capture Frame Ethernet

1. Membersihkan cache browser
2. Membuka Wireshark dan memulai packet capture
3. Mengakses URL: `http://gaia.cs.umass.edu/wireshark-labs/HTTP-ethereal-lab-file3.html`
4. Browser menampilkan dokumen "Bill of Rights AS"
5. Menghentikan capture dan menganalisis frame Ethernet

### 2.2 Analisis ARP Cache

1. Melihat isi ARP cache menggunakan perintah:
   - **Windows**: `arp -a` di command prompt
2. Mengamati entry dynamic dan static dalam ARP cache
3. Mengidentifikasi interface network yang aktif

### 2.3 Mengamati Aksi ARP

1. Membersihkan cache ARP dan cache browser
2. Memulai Wireshark capture
3. Mengakses URL yang sama
4. Menganalisis paket ARP Request dan ARP Reply
5. Menggunakan filter `arp.opcode == 2` untuk melihat ARP Reply
6. Menggunakan filter `arp` untuk melihat semua traffic ARP

---

## 3. Hasil dan Pembahasan

### 3.1 Konfigurasi Network Interface


