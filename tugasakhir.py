class ParkirDetail:
    def __init__(self):
        self.nama_pengguna = ""
        self.waktu_parkir = ""
        self.jenis_kendaraan = ""
        self.waktu_akhir_parkir = ""
        self.biaya_parkir = ""

    def parkir(self, nama_pengguna, waktu_parkir, jenis_kendaraan):
        self.nama_pengguna = nama_pengguna
        self.waktu_parkir = waktu_parkir
        self.jenis_kendaraan = jenis_kendaraan

    def akhiri_parkir(self, waktu_akhir_parkir):
        self.waktu_akhir_parkir = waktu_akhir_parkir

    def hitung_biaya_parkir(self):
                
        if self.jenis_kendaraan.lower() == "mobil":
            self.biaya_parkir = 5000
        else:
            self.biaya_parkir = 0

    def tampilkan_informasi(self):
        print("Nama Pengguna:", self.nama_pengguna)
        print("Waktu Parkir:", self.waktu_parkir)
        print("Jenis Kendaraan:", self.jenis_kendaraan)
        print("Waktu Akhir Parkir:", self.waktu_akhir_parkir)
        print("Biaya Parkir:", self.biaya_parkir)

if __name__ == "__main__":
    aplikasi_parkir = ParkirDetail()
    aplikasi_parkir.parkir("Leonardo", "27-12-2022 10:30", "Mobil")
    aplikasi_parkir.akhiri_parkir("27-12-2022 16:00")
    aplikasi_parkir.hitung_biaya_parkir()
    aplikasi_parkir.tampilkan_informasi()