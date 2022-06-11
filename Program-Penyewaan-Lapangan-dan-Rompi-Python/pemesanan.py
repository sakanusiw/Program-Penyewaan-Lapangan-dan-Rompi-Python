from prettytable import PrettyTable
import pymysql

db = pymysql.connect(host="localhost",user="root",password="",database="pbo_akhir")
cur = db.cursor()

class Pemesanan:
    def __init__(self, id_pemesanan, tanggal_pemesanan, tanggal_sewa, jam_sewa, durasi_sewa, harga_sewa, id_lapangan, id_rompi):
        self.id_pemesanan = id_pemesanan
        self.tanggal_pemesanan = tanggal_pemesanan
        self.tanggal_sewa = tanggal_sewa
        self.jam_sewa = jam_sewa
        self.durasi_sewa = durasi_sewa
        self.harga_sewa = harga_sewa
        self.id_lapangan = id_lapangan
        self.id_rompi = id_rompi

    def info_pemesananLapangan():
        query = "SELECT * FROM pemesanan_lapangan;"
        cur.execute(query)
        db.commit()
        hasil = cur.fetchall()
        tabel = PrettyTable(["ID", "TGL PESAN", "TGL SEWA", "JAM", "DURASI", "HARGA", "ID LAP"])
        for i in hasil:
            tabel.add_row([i[0],i[2],i[3],i[4],i[5],i[6],i[1]])
        print(tabel)
        cur.execute("SELECT SUM(harga_sewa) FROM pemesanan_lapangan;")
        db.commit()
        total = cur.fetchone()
        print("Total pendapatan = {}".format(int(total[0])))

    def info_pemesananRompi():
        query = "SELECT * FROM pemesanan_rompi;"
        cur.execute(query)
        db.commit()
        hasil = cur.fetchall()
        tabel = PrettyTable(["ID", "TGL PESAN", "TGL SEWA", "JAM", "DURASI", "HARGA", "ID ROMPI"])
        for i in hasil:
            tabel.add_row([i[0],i[2],i[3],i[4],i[5],i[6],i[1]])
        print(tabel)
        cur.execute("SELECT SUM(harga_sewa) FROM pemesanan_rompi;")
        db.commit()
        total = cur.fetchone()
        print("Total pendapatan = Rp{}".format(int(total[0])))