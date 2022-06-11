#Import Class
from admin import Admin
from pemesanan import Pemesanan
from pemilik import Pemilik
from pelanggan import Pelanggan
from lapangan import Lapangan
from rompi import PaketRompi

#Instansiasi Objek admin
a = Admin("admin", "admin", 1, "Teguh")
#Instansiasi Objek pemilik
pm = Pemilik("pemilik", "pemilik", 11, "Saka Nusi")
#Objek pelanggan
pl = Pelanggan("ivan", "ivanatch", "Ivan Bhagaskara", "Sleman", "0812343", "Laki-laki")


#Fungsi untuk menu info lapangan
def InfoLapangan():
    print("==== Informasi Lapangan ====")
    if log == 1:
        print("1. Lapangan Vinyl\n2. Lapangan Sintetis\n3. Back")
        x = int(input("Pilih opsi : "))
        if x == 1:
            Lapangan.vinyl()
            print("Ubah status? (Y/T)")
            y = input("Pilih Opsi : ")
            if y == "Y" or y == "y":
                a.edit_statusLapangan()
                InfoLapangan()
            elif y == "T" or y == "t":
                InfoLapangan()
        elif x == 2:
            Lapangan.sintetis()
            print("Ubah status? (Y/T)")
            y = input("Pilih Opsi : ")
            if y == "Y" or y == "y":
                a.edit_statusLapangan()
                InfoLapangan()
            elif y == "T" or y == "t":
                InfoLapangan()
        elif x == 3:
           menuAdmin()
        else:
            print("Opsi Error")
            InfoLapangan()
    elif log == 2 or 3:
        print("1. Lapangan Vinyl\n2. Lapangan Sintetis\n3. Back")
        x = int(input("Pilih opsi : "))
        if x == 1:
            Lapangan.vinyl()
            InfoLapangan()
        elif x == 2:
            Lapangan.sintetis()
            InfoLapangan()
        elif x == 3:
            if log == 2:
                menuPemilik()
            elif log == 3:
                menuLapangan()
        else:
            print("Opsi Error")
            InfoLapangan()

#Fungsi untuk menu info Paket Rompi
def InfoRompi():
    print("==== Informasi Paket Rompi ====")
    if log == 1:
        print("1. Paket Rompi warna terang\n2. Paket Rompi warna gelap\n3. Tambah Paket Rompi\n4. Hapus Paket Rompi\n5. Back")
        x = int(input("Pilih opsi : "))
        if x == 1:
            PaketRompi.rompiTerang()
            print("Ubah status? (Y/T)")
            y = input("Pilih Opsi : ")
            if y == "Y" or y == "y":
                a.edit_statusRompi()
                InfoRompi()
            elif y == "T" or y == "t":
                InfoRompi()
        elif x == 2:
            PaketRompi.rompiGelap()
            print("Ubah status? (Y/T)")
            y = input("Pilih Opsi : ")
            if y == "Y" or y == "y":
                a.edit_statusRompi()
                InfoRompi()
            elif y == "T" or y == "t":
                InfoRompi()
        elif x == 3:
            a.tambah_rompi()
            InfoRompi()
        elif x == 4:
            a.hapus_rompi()
            InfoRompi()
        elif x == 5:
           menuAdmin()
        else:
            print("Opsi Error")
            InfoRompi()
    elif log == 2 or 3:
        print("1. Paket Rompi warna terang\n2. Paket Rompi warna gelap\n3. Back")
        x = int(input("Pilih opsi : "))
        if x == 1:
            PaketRompi.rompiTerang()
            InfoRompi()
        elif x == 2:
            PaketRompi.rompiGelap()
            InfoRompi()
        elif x == 3:
            if log == 2:
                menuPemilik()
            elif log == 3:
                menuRompi()
        else:
            print("Opsi Error")
            InfoRompi()

#Fungsi untuk menu lapangan
def menuLapangan():
    print("==== Menu Lapangan ====")
    print("1. Info Lapangan\n2. Pesan lapangan\n3. Back")
    menu = int(input("Pilih Opsi : "))
    if menu == 1:
        InfoLapangan()
    elif menu == 2:
        pl.pesan_lapangan()
        menuLapangan()
    elif menu == 3:
        menuPelanggan()
    else:
        print("Opsi Error")
        menuLapangan()

#Fungsi untuk menu rompi
def menuRompi():
    print("==== Menu Paket Rompi ====")
    print("1. Info Paket Rompi\n2. Pesan Paket Rompi\n3. Back")
    menu = int(input("Pilih Opsi : "))
    if menu == 1:
        InfoRompi()
    elif menu == 2:
        pl.pesan_rompi()
        menuRompi()
    elif menu == 3:
        menuPelanggan()
    else:
        print("Opsi Error")
        menuRompi()

def menuPemesanan():
    print("==== Menu Info Pemesanan ====")
    print("1. Data Transaksi Pemesanan Lapangan\n2. Data Transaksi Pemesanan Paket Rompi\n3. Back")
    menu = int(input("Pilih Opsi : "))
    if menu == 1:
        if log == 1:
            Pemesanan.info_pemesananLapangan()
            print("Hapus data pemesanan? (Y/T)")
            x = input("Pilih Opsi : ")
            if x == "Y" or x == "y":
                a.hapus_pemesananLapangan()
                menuPemesanan()
            elif x == "T" or x == "t":
                menuPemesanan()
            else:
                print("Opsi Error")
        elif log == 2:
            Pemesanan.info_pemesananLapangan()
            menuPemesanan()
    elif menu == 2:
        if log == 1:
            Pemesanan.info_pemesananRompi()
            print("Hapus data pemesananan? (Y/T)")
            x = input("Pilih Opsi : ")
            if x == "Y" or x == "y":
                a.hapus_pemesananRompi()
                menuPemesanan()
            elif x == "T" or x == "t":
                menuPemesanan()
            else:
                print("Opsi Error")
        elif log == 2:
            Pemesanan.info_pemesananRompi()
            menuPemesanan()
    elif menu == 3:
        if log == 1:
            menuAdmin()
        elif log == 2:
            menuPemilik()
    else:
        print("Opsi Error")
        menuPemesanan()

#Fungsi untuk menu khusus admin
def menuAdmin():
    print("1. Lapangan \n2. Paket Rompi \n3. Data Pemesanan \n4. Info akun \n5. Logout")
    menu = int(input("Pilih Opsi : "))
    if menu == 1:
        InfoLapangan()
    elif menu == 2:
        InfoRompi()
    elif menu == 3:
        menuPemesanan()
    elif menu == 4:
        a.info_admin()
        menuAdmin()
    elif menu == 5:
        main()
    else:
        print("Opsi Error")
        menuAdmin()

#Fungsi untuk menu khusus pelanggan
def menuPelanggan():
    print("1. Pesan/Lihat Lapangan \n2. Pesan/Lihat Paket Rompi \n3. Info akun \n4. Logout")
    menu = int(input("Pilih Opsi : "))
    if menu == 1:
        menuLapangan()
    elif menu == 2:
        menuRompi()
    elif menu == 3:
        pl.info_pelanggan()
        menuPelanggan()
    elif menu == 4:
        main()
    else:
        print("Opsi Error")
        menuPelanggan()

#Fungsi untuk menu khusus pemilik
def menuPemilik():
    print("1. Lapangan \n2. Paket Rompi \n3. Data Pemesanan \n4. Info akun \n5. Logout")
    menu = int(input("Pilih Opsi : "))
    if menu == 1:
        InfoLapangan()
    elif menu == 2:
        InfoRompi()
    elif menu == 3:
        menuPemesanan()
    elif menu == 4:
        pm.info_pemilik()
        menuPemilik()
    elif menu == 5:
        main()
    else:
        print("Opsi Error")
        menuPemilik()

#Fungsi utama untuk program
def main():
    print("Login sebagai :")
    print("1. Admin\n2. Pemilik\n3. Pelanggan\n4. Exit")
    global log
    log = int(input("Pilih Opsi : "))
    if log == 1:
        a._authentication()
        menuAdmin()
    elif log == 2:
        pm._authentication()
        menuPemilik()
    elif log == 3:
        pl._authentication()
        menuPelanggan()
    elif log == 4:
        exit()
    else:
        print("Error")
        main()

main()