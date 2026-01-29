from abc import ABC, abstractmethod

class BarangElektronik(ABC):
    def __init__(self, nama, harga_dasar):
        self.nama = nama
        self.__stok = 0
        self.__harga_dasar = harga_dasar

    def get_stok(self):
        return self.__stok

    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
            return
        self.__stok += jumlah
        print(f"Berhasil menambahkan stok {self.nama}: {jumlah} unit.")

    def _get_harga_dasar(self):
        return self.__harga_dasar

    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass

class Laptop(BarangElektronik):
    def __init__(self, nama, harga_dasar, processor):
        super().__init__(nama, harga_dasar)
        self.processor = processor

    def tampilkan_detail(self):
        print(f"[LAPTOP] {self.nama} | Proc: {self.processor}")

    def hitung_harga_total(self, jumlah):
        pajak = 0.10
        harga = self._get_harga_dasar()
        total_pajak = harga * pajak * jumlah
        subtotal = (harga * jumlah) + total_pajak

        print(f"Harga Dasar: Rp {harga:,.0f} | Pajak(10%): Rp {harga * pajak:,.0f}")
        print(f"Beli: {jumlah} unit | Subtotal: Rp {subtotal:,.0f}")

        return subtotal

class Smartphone(BarangElektronik):
    def __init__(self, nama, harga_dasar, kamera):
        super().__init__(nama, harga_dasar)
        self.kamera = kamera

    def tampilkan_detail(self):
        print(f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}")

    def hitung_harga_total(self, jumlah):
        pajak = 0.05
        harga = self._get_harga_dasar()
        total_pajak = harga * pajak * jumlah
        subtotal = (harga * jumlah) + total_pajak

        print(f"Harga Dasar: Rp {harga:,.0f} | Pajak(5%): Rp {harga * pajak:,.0f}")
        print(f"Beli: {jumlah} unit | Subtotal: Rp {subtotal:,.0f}")

        return subtotal

def proses_transaksi(daftar_barang):
    print("\n--- STRUK TRANSAKSI ---")
    total = 0

    for i, item in enumerate(daftar_barang, start=1):
        barang, jumlah = item
        print(f"{i}. ", end="")
        barang.tampilkan_detail()
        total += barang.hitung_harga_total(jumlah)
        print()

    print("------------------------------")
    print(f"TOTAL TAGIHAN: Rp {total:,.0f}")
    print("------------------------------")


print("--- SETUP DATA ---")

laptop = Laptop("ROG Zephyrus", 20_000_000, "Ryzen 9")
smartphone = Smartphone("iPhone 13", 15_000_000, "12MP")

laptop.tambah_stok(10)
smartphone.tambah_stok(-5)
smartphone.tambah_stok(20)

keranjang = [
    (laptop, 2),
    (smartphone, 1)
]

proses_transaksi(keranjang)