from user import User
import time
from pemesanan import Pemesanan
import pymysql

db = pymysql.connect(host="localhost",user="root",password="",database="pbo_akhir")
cur = db.cursor()

class Pelanggan(User):
    def __init__(self, username, password, nama_pelanggan, alamat_pelanggan, noTelp_pelanggan,jenisKelamin_pelanggan):
        super().__init__(username, password)
        self.nama_pelanggan = nama_pelanggan
        self.alamat_pelanggan = alamat_pelanggan
        self.noTelp_pelanggan = noTelp_pelanggan
        self.jenisKelamin_pelanggan = jenisKelamin_pelanggan

    def info_pelanggan(self):
        print("<--Data Pelanggan-->")
        print("Nama: {}\nUsername: {}\nPassword: {}\nAlamat: {}\nNo. Telp: {}\nJenis Kelamin: {}".format(self.nama_pelanggan,self._username,self._password,self.alamat_pelanggan,self.noTelp_pelanggan,self.jenisKelamin_pelanggan))
    
    def pesan_lapangan(self):
        print("==== Pesan Lapangan ====")
        localtime = time.asctime(time.localtime(time.time()))
        a = input("Masukkan ID Lapangan : ")
        query_id = "SELECT status_lapangan FROM lapangan WHERE id_lapangan = {};".format(a)
        cur.execute(query_id)
        db.commit()
        status = cur.fetchone()
        if status[0] != "Tersedia":
            print("Lapangan sudah disewa!")
            Pelanggan.pesan_lapangan(self)
        elif status[0] == "Tersedia":
            b = input("Masukkan tanggal sewa : ")
            c = input("Masukkan jam sewa : ")
            d = int(input("Masukkan durasi sewa (jam) : "))
            query_tarif = "SELECT tarif_lapangan FROM lapangan WHERE id_lapangan = {};".format(a)
            cur.execute(query_tarif)
            db.commit()
            tarif = cur.fetchone()
            harga = int(tarif[0]) * d   
            pms = Pemesanan("",localtime,b,c,d,harga,a,"")
            query = "INSERT INTO pemesanan_lapangan VALUES ({}, {}, '{}', '{}', '{}', {}, {});".format(pymysql.NULL,pms.id_lapangan,pms.tanggal_pemesanan,pms.tanggal_sewa,pms.jam_sewa,pms.durasi_sewa,pms.harga_sewa)
            cur.execute(query)
            db.commit()
            print("Lapangan Berhasil dipesan.")
            print("\tTanggal Pemesanan : {}\n\tID Lapangan : {}\n\tTanggal Sewa : {}\n\tJam Sewa : {}\n\tDurasi Sewa : {}\n\tHarga Sewa : Rp{}".format(localtime,a,b,c,d,harga))
            cur.execute("UPDATE lapangan SET status_lapangan = 'Disewa' WHERE id_lapangan = {};".format(a))
            db.commit()

    def pesan_rompi(self):
        print("==== Pesan Paket Rompi ====")
        localtime = time.asctime(time.localtime(time.time()))
        a = input("Masukkan ID Paket Rompi : ")
        query_id = "SELECT status_rompi FROM rompi WHERE id_rompi = {};".format(a)
        cur.execute(query_id)
        db.commit()
        status = cur.fetchone()
        if status[0] != "Tersedia":
            print("Paket Rompi sudah disewa!")
            Pelanggan.pesan_rompi(self)
        elif status[0] == "Tersedia":
            b = input("Masukkan tanggal sewa : ")
            c = input("Masukkan jam sewa : ")
            d = int(input("Masukkan durasi sewa (jam) : "))
            query_tarif = "SELECT tarif_rompi from rompi WHERE id_rompi = {};".format(a)
            cur.execute(query_tarif)
            db.commit()
            tarif = cur.fetchone()
            harga = int(tarif[0]) * d   
            pms = Pemesanan("",localtime,b,c,d,harga,"",a)
            query = "INSERT INTO pemesanan_rompi VALUES ({}, {}, '{}', '{}', '{}', {}, {});".format(pymysql.NULL,pms.id_rompi,pms.tanggal_pemesanan,pms.tanggal_sewa,pms.jam_sewa,pms.durasi_sewa,pms.harga_sewa)
            cur.execute(query)
            db.commit()
            print("Paket Rompi Berhasil dipesan.")
            print("\tTanggal Pemesanan : {}\n\tID Paket Rompi : {}\n\tTanggal Sewa : {}\n\tJam Sewa : {}\n\tDurasi Sewa : {}\n\tHarga Sewa : Rp{}".format(localtime,a,b,c,d,harga))
            cur.execute("UPDATE rompi SET status_rompi = 'Disewa' WHERE id_rompi = {};".format(a))
            db.commit()