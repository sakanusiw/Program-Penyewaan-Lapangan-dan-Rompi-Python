import getpass

class User:
    def __init__(self, username, password):
        self._username = username
        self._password = password

    def _authentication(self):
        username = input("Masukkan username : ")
        password = getpass.getpass("Masukkan password : ")

        while username != self._username or password != self._password:
            print("Gagal login. Username atau Password Salah!")
            print("="*20)
            print("Masukkan data yang benar!")
            username = input("Masukkan username : ")
            password = getpass.getpass("Masukkan password : ")

        if username == self._username or password == self._password:
            print("\n#### Sukses login ####")
            print("=== SELAMAT DATANG ===")