# Laporan Praktikum Jaringan Komputer - Modul 10
## Internet Protocol (IP) Analysis

## Identitas Praktikan
### Nama: Didit Septa Putra
### NIM: 103072400071
### Kelas: IF-04-01

---
#### 10.1 IPv4 Dasar (Traceroute & TTL)
**Tujuan:** Mengmengamati paket IPv4 standar dan mekanisme kerja Time-to-Live (TTL) menggunakan utilitas traceroute/tracert.

**Bukti *Screenshot* Wireshark:**
![Figure 10.1 Basic IPv4](assets/ipv4.png)

**Analisis:**
Program traceroute memetakan jalur komunikasi dalam jaringan dengan mengirimkan serangkaian paket data menuju host tujuan secara bertahap sembari menaikkan nilai batas waktu hidup atau *Time-to-Live* (TTL). Setiap kali paket melewati sebuah router (hop), router tersebut berkewajiban mengurangi nilai TTL di dalam header IP sebesar 1. Ketika nilai TTL mencapai angka 0 sebelum paket berhasil sampai ke tujuan akhir, router akan membuang paket tersebut dan mengirimkan sinyal kesalahan berupa pesan *ICMP Time-to-live exceeded* kembali ke host pengirim. Melalui pesan kesalahan inilah host pengirim dapat mencatat dan mengidentifikasi alamat IP dari setiap router perantara yang dilewati sepanjang jalur menuju destinasi.

#### 10.2 Fragmentasi IP
**Tujuan:** Menganalisis perilaku fragmentasi pada protokol IPv4 saat ukuran datagram melebihi batas Maximum Transmission Unit (MTU) yang ditentukan oleh arsitektur jaringan.

**Bukti *Screenshot* Wireshark:**
![Figure 10.2 Fragmentasi IP](assets/fragmented.png)

**Analisis:**
Pada pengamatan terhadap aktivitas fragmentasi IP di Wireshark, fokus analisis diarahkan pada paket nomor 18889 yang merupakan bagian dari transmisi datagram berukuran besar dari alamat IP 1.1.1.1 menuju host tujuan 192.168.1.3. Berdasarkan rincian pada header Internet Protocol Version 4, paket ini memiliki nilai Identification sebesar 0xd31d (54045), yang berfungsi sebagai penanda unik agar seluruh serpihan fragmentasi dari pesan yang sama dapat diidentifikasi oleh host penerima. Berbeda dengan potongan awal, pada paket spesifik ini flag More fragments berada dalam kondisi Not Set (0), yang menandakan secara eksplisit bahwa paket ini merupakan kepingan terakhir dari rangkaian fragmentasi tersebut. Hal ini diperkuat oleh nilai Fragment Offset yang menunjukkan angka 2960, mengindikasikan posisi awal data pada fragmen ini terhadap datagram asli sebelum dipecah. Melalui tanda pengenal ID yang identik dan informasi posisi offset tersebut, host tujuan dapat melakukan proses perakitan kembali (reassembly) seluruh potongan paket menjadi satu kesatuan protokol ICMP Echo Reply yang utuh.

#### 10.3 IPv6
**Tujuan:** Mengamati karakteristik struktur header, format pengalamatan, dan mekanisme resolusi alamat pada Internet Protocol generasi terbaru (IPv6).

**Bukti *Screenshot* Wireshark:**
![Figure 10.3 IPv6](assets/ipv6.png)

**Analisis:**
Observasi terhadap datagram IPv6 dilakukan melalui pelacakan paket yang memuat permintaan sistem penamaan domain (DNS) berupa *Standard Query AAAA* untuk domain youtube.com. Query tipe AAAA digunakan secara spesifik untuk memetakan atau mentranslasikan nama domain menjadi alamat IP versi 6, menggantikan query tipe A yang biasa digunakan untuk pemetaan IPv4. Pada panel detail *Internet Protocol Version 6*, terlihat perbedaan fundamental pada format pengalamatan *Source Address* dan *Destination Address* yang tidak lagi menggunakan sistem desimal 32-bit, melainkan mengadopsi sistem blok heksadesimal 128-bit yang jauh lebih panjang. Struktur header IPv6 dirancang lebih ringkas namun menawarkan ruang alokasi alamat global yang jauh lebih masif guna mengantisipasi kelangkaan alamat IP di masa mendatang.

---

### Kesimpulan
Berdasarkan hasil praktikum Modul 10 mengenai investigasi mendalam terhadap protokol IP (IPv4 dan IPv6) menggunakan Wireshark, diperoleh beberapa kesimpulan utama sebagai berikut:

1. **Mekanisme Pelacakan Jalur Traceroute:** Protokol IP memanfaatkan field *Time-to-Live* (TTL) untuk membatasi masa hidup paket di jaringan. Mekanisme penambahan TTL secara bertahap pada traceroute memicu router perantara mengirim balik pesan kesalahan *ICMP Time-to-live exceeded (Type 11)* ketika TTL habis, yang kemudian dimanfaatkan untuk memetakan topologi hop-by-hop menuju host tujuan.
2. **Kondisi Fragmentasi Paket:** Fragmentasi IP merupakan solusi lapisan network ketika ukuran datagram melebihi kapasitas muatan maksimum media transmisi (MTU). Proses pemecahan paket ini sepenuhnya ditangani oleh router perantara sebelum diteruskan ke jalur berikutnya.
3. **Parameter Rekonstruksi Fragmen:** Untuk menyatukan kembali potongan paket di sisi penerima, IPv4 mengandalkan tiga field utama pada headernya: *Identification* (penanda kesamaan datagram induk), *Flags* (khususnya flag *More fragments* untuk mendeteksi akhir potongan), dan *Fragment Offset* (penunjuk urutan byte data).
4. **Arsitektur Pengalamatan IPv6:** IPv6 membawa perubahan struktural besar dengan memperluas ukuran alamat dari 32-bit (IPv4) menjadi 128-bit yang direpresentasikan dalam format heksadesimal, secara efektif menyelesaikan keterbatasan ruang alamat pada IPv4.
5. **Dukungan Infrastruktur DNS IPv6:** Transisi menuju lingkungan IPv6 didukung penuh oleh protokol aplikasi seperti DNS melalui penggunaan record *Query AAAA*, yang secara fungsional setara dengan record A pada IPv4 namun mengembalikan representasi alamat heksadesimal 128-bit.

