from prettytable import PrettyTable
import pymysql

db = pymysql.connect(host="localhost",user="root",password="",database="pbo_akhir")
cur = db.cursor()

class Lapangan:
    def __init__(self, id_lapangan, jenis_lapangan, tarif_lapangan, status_lapangan):
        self.id_lapangan = id_lapangan
        self.jenis_lapangan = jenis_lapangan
        self.tarif_lapangan = tarif_lapangan
        self.status_lapangan = status_lapangan
       
    def vinyl():
        query = "SELECT * FROM lapangan WHERE jenis_lapangan = 'Vinyl';"
        cur.execute(query)
        db.commit()
        hasil = cur.fetchall()
        tabel = PrettyTable(["ID", "JENIS", "TARIF", "STATUS"])
        for i in hasil:
            tabel.add_row([i[0],i[1],i[2],i[3]])
        print(tabel)

    def sintetis():
        query = "SELECT * FROM lapangan WHERE jenis_lapangan = 'Sintetis';"
        cur.execute(query)
        db.commit()
        hasil = cur.fetchall()
        tabel = PrettyTable(["ID", "JENIS", "TARIF", "STATUS"])
        for i in hasil:
            tabel.add_row([i[0],i[1],i[2],i[3]])
        print(tabel)