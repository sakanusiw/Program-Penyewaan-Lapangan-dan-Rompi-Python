from prettytable import PrettyTable
import pymysql

db = pymysql.connect(host="localhost",user="root",password="",database="pbo_akhir")
cur = db.cursor()

class PaketRompi:
    def __init__(self, id_rompi, merk_rompi, warna_rompi, tarif_rompi, status_rompi):
        self.id_rompi = id_rompi
        self.merk_rompi = merk_rompi
        self.warna_rompi = warna_rompi
        self.tarif_rompi = tarif_rompi
        self.status_rompi = status_rompi

    def rompiTerang():
        query = "SELECT * FROM rompi WHERE warna_rompi = 'Terang';"
        cur.execute(query)
        db.commit()
        hasil = cur.fetchall()
        tabel = PrettyTable(["ID", "MERK", "WARNA", "TARIF", "STATUS"])
        for i in hasil:
            tabel.add_row([i[0],i[1],i[2],i[3],i[4]])
        print(tabel)

    def rompiGelap():
        query = "SELECT * FROM rompi WHERE warna_rompi = 'Gelap';"
        cur.execute(query)
        db.commit()
        hasil = cur.fetchall()    
        tabel = PrettyTable(["ID", "MERK", "WARNA", "TARIF", "STATUS"])
        for i in hasil:
            tabel.add_row([i[0],i[1],i[2],i[3],i[4]])
        print(tabel)