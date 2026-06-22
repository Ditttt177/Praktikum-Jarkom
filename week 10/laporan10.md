# Laporan Praktikum Jaringan Komputer - Modul 10
## Internet Protocol (IP) Analysis

## Identitas Praktikan
### Nama: Didit Septa Putra
### NIM: 103072400071
### Kelas: IF-04-01

---

## 1.1 Tujuan Praktikum
**1** Menganalisis cara kerja protokol IP menggunakan Wireshark: Mampu menangkap paket (*capturing*), menyaring (*filtering*), dan membedah isi data pada lapisan jaringan (*network layer*) secara *real-time*. 
**2** Memahami struktur header IPv4 dan field-field penting: Mampu mengidentifikasi fungsi komponen kritis seperti *Version*, *Total Length*, *TTL*, hingga *Source/Destination IP Address*.
**3** Mempelajari fragmentasi IP pada datagram besar: Mampu menganalisis perubahan nilai *Identification*, *Flags*, dan *Fragment Offset* saat paket melebihi kapasitas beban maksimum (MTU).
**4** Mengenal datagram IPv6: Mampu memahami arsitektur *Fixed Header* 40 bytes serta perbedaan karakteristik pengalamatan dan penanganan paket dibanding IPv4.
---

## 1.2 Hasil Praktikum

### 1.2.1 Bagian 1: Analisis IPv4 Dasar

