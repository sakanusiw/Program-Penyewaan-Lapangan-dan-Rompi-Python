from user import User
class Pemilik(User):
    def __init__(self, username, password, id_pemilik, nama_pemilik):
        super().__init__(username, password)
        self.__id_pemilik = id_pemilik
        self.nama_pemilik = nama_pemilik

    def info_pemilik(self):
        print("<--Informasi Pemilik-->")
        print("ID Pemilik: {}\nNama: {}\nUsername: {}\nPassword: {}".format(self.__id_pemilik,self.nama_pemilik,self._username,self._password))