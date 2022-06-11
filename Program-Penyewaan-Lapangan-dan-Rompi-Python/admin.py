from user import User
# from lapangan import Lapangan
from rompi import PaketRompi
import pymysql

db = pymysql.connect(host="localhost",user="root",password="",database="pbo_akhir")
cur = db.cursor()

class Admin(User):
    def __init__(self, username, password, id_admin, nama_admin):
        super().__init__(username, password)
        self.__id_admin = id_admin
        self.nama_admin = nama_admin

    def info_admin(self):
        print("<--Informasi Admin-->")
        print("ID Admin: {}\nNama: {}\nUsername: {}\nPassword: {}".format(self.__id_admin,self.nama_admin,self._username,self._password))

    # def tambah_lapangan(self):
    #     x = input("Masukkan jenis Lapangan : ")
    #     y = input("Masukkan tarif Lapangan : ")
    #     z = input("Masukkan status Lapangan : ")
    #     lp = Lapangan("",x, y, z)
    #     query = "INSERT INTO lapangan VALUES ({}, '{}', {}, '{}');".format(pymysql.NULL, lp.jenis_lapangan, lp.tarif_lapangan, lp.status_lapangan)
    #     cur.execute(query)
    #     db.commit()
    #     print("Lapangan Berhasil ditambahkan.")

    def tambah_rompi(self):
        a = input("Masukkan merk Rompi : ")
        b = input("Masukkan warna Rompi : ")
        c = input("Masukkan tarif Rompi : ")
        r = PaketRompi("", a, b, c, "Tersedia")
        query = "INSERT INTO rompi VALUES ({}, '{}', '{}', {}, '{}');".format(pymysql.NULL, r.merk_rompi, r.warna_rompi, r.tarif_rompi, r.status_rompi)
        cur.execute(query)
        db.commit()
        print("Paket Rompi berhasil ditambahkan.")
    
    def hapus_rompi(self):
        a = int(input("Pilih ID Paket Rompi : "))
        query_id = "SELECT * FROM rompi WHERE id_rompi = {};".format(a)
        cur.execute(query_id)
        db.commit()
        status = cur.fetchone()
        if status:
            cur.execute("DELETE FROM rompi WHERE id_rompi = {};".format(a))
            cur.execute("ALTER TABLE rompi DROP id_rompi;")
            cur.execute("ALTER TABLE rompi ADD id_rompi INT NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST;")
            db.commit()
            print("Data Paket Rompi berhasil dihapus")
        else:
            print("ID tidak ditemukan!")
            Admin.hapus_rompi(self)
    
    def edit_statusLapangan(self):
        a = int(input("Pilih ID lapangan : "))
        query_id = "SELECT status_lapangan FROM lapangan WHERE id_lapangan = {};".format(a)
        cur.execute(query_id)
        db.commit()
        status = cur.fetchone()
        if status:
            b = input("Status : ")
            query = "UPDATE lapangan SET status_lapangan = '{}' WHERE id_lapangan = {};".format(b,a)
            cur.execute(query)
            db.commit()
            print("Status berhasil diubah")
        else:
            print("ID tidak ditemukan!")
            Admin.edit_statusLapangan(self)

    def edit_statusRompi(self):
        a = int(input("Pilih ID Paket Rompi : "))
        query_id = "SELECT status_rompi FROM rompi WHERE id_rompi = {};".format(a)
        cur.execute(query_id)
        db.commit()
        status = cur.fetchone()
        if status:
            b = input("Status : ")
            query = "UPDATE rompi SET status_rompi = '{}' WHERE id_rompi = {};".format(b,a)
            cur.execute(query)
            db.commit()
            print("Status berhasil diubah")
        else:
            print("ID tidak ditemukan!")
            Admin.edit_statusRompi(self)
    
    def hapus_pemesananLapangan(self):
        a = int(input("Pilih ID pemesanan : "))
        query_id = "SELECT * FROM pemesanan_lapangan WHERE id_pemesanan = {};".format(a)
        cur.execute(query_id)
        db.commit()
        status = cur.fetchone()
        if status:
            cur.execute("DELETE FROM pemesanan_lapangan WHERE id_pemesanan = {};".format(a))
            cur.execute("ALTER TABLE pemesanan_lapangan DROP id_pemesanan;")
            cur.execute("ALTER TABLE pemesanan_lapangan ADD id_pemesanan INT NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST;")
            db.commit()
            print("Data pemesanan berhasil dihapus")
        else:
            print("ID tidak ditemukan!")
            Admin.hapus_pemesananLapangan(self)
        
    def hapus_pemesananRompi(self):
        a = int(input("Pilih ID pemesanan : "))
        query_id = "SELECT * FROM pemesanan_rompi WHERE id_pemesanan = {};".format(a)
        cur.execute(query_id)
        db.commit()
        status = cur.fetchone()
        if status:
            cur.execute("DELETE FROM pemesanan_rompi WHERE id_pemesanan = {};".format(a))
            cur.execute("ALTER TABLE pemesanan_rompi DROP id_pemesanan;")
            cur.execute("ALTER TABLE pemesanan_rompi ADD id_pemesanan INT NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST;")
            db.commit()
            print("Data pemesanan berhasil dihapus")
        else:
            print("ID tidak ditemukan!")
            Admin.hapus_pemesananRompi(self)