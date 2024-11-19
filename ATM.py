class nasabah():
    def __init__(self,nama,password,saldo):
        self.nama = nama
        self.password = password
        self.rekening = saldo
        self.blokir = False
    
    def saldoNambah(self,jumlah):
        self.rekening = self.rekening + jumlah
        return self.rekening

    def saldoNgurang(self,jumlah):
        if self.rekening > 50000:
            self.rekening = self.rekening - jumlah
            return self.rekening
        else:
            return 'Maaf saldo anda tidak mencukupi'
    
    def getSaldo(self):
        return self.rekening
    
    def setTerblokir(self):
        self.blokir = True
        print('!'*5,'Maaf ATM anda telah terblokir, silakan kunjungi kantor bank terdekat untuk aktivasi kembali')
        return self.blokir

class ATM():
    def __init__(self,nama):
        self.aktif = False
        self.nama = nama

    def mainMenu(self,nasabah):
        if self.aktif:
            pilihan = int(input('1. Penarikan\n2. Cek Saldo\n3. Menabung\n4. Keluar \n= '))
            if pilihan==1:
                self.penarikan(nasabah)
            elif pilihan==2:
                self.cekSaldo(nasabah)
            elif pilihan==3:
                self.menabung(nasabah)
            elif pilihan==4:
                self.logout(nasabah)
            else:
                print('!'*5,'Pilihan anda tidak sesuai')
                self.mainMenu(nasabah)
        else:
            self.logout(nasabah)
    
    def login(self,nasabah):
        self.aktif = True
        print('-'*20,'Selamat Datang di ATM Bank {}'.format(self.nama), '-'*20)
        i = 0
        while (int(input('Silahkan Masukkan Pin anda: ')) != nasabah.password):
            if i<=1:
                print('Maaf kata sandi salah!')
                i+=1
            else:
                print('!'*5,'ATM Anda telah terblokir karena salah memasukkan pin 3 kali')
                return nasabah.setTerblokir()
        else:
            print('*'*20,'Selamat datang {}'.format(nasabah.nama),'*'*20)
        return self.aktif
    
    def logout(self, nasabah):
        self.aktif = False
        print('*'*20,'Sampai Jumpa {}'.format(nasabah.nama),'*'*20)
        return self.aktif

    def penarikan(self, nasabah):
        jumlahPenarikan = int(input('masukkan nominal penarikan yang akan anda lakukan: '))
        hasil = nasabah.saldoNgurang(jumlahPenarikan)
        if hasil == "Maaf saldo anda tidak mencukupi":
            inputan = input('Maaf saldo anda tidak mencukupi, ingin transaksi lain? \n ya atau tidak : ')
            if inputan == "ya":
                return self.mainMenu(nasabah)
            else:
                return self.logout(nasabah)
        else:
            self.cekSaldo(nasabah)
    
    def cekSaldo(self,nasabah):
        print('Sisa saldo anda adalah: {}'.format(nasabah.getSaldo()))
        if input('Ingin melakukan transaksi lain? \n ya atau tidak : ') != 'ya':
                return self.logout(nasabah)
        return self.mainMenu(nasabah)

    def menabung(self,nasabah):
        tabung = int(input('Silakan Masukkan nominal yang ingin anda tabung : '))
        nasabah.saldoNambah(tabung)
        self.cekSaldo(nasabah)


def mainProgram(bank, nasabah):
    bank.login(nasabah)
    if not(nasabah.blokir):
        bank.mainMenu(nasabah)

nasabah1 = nasabah('Lawliet',123456,100000)
nasabah2 = nasabah('Yagami Light',654321,40000)
listNasabah = [nasabah1,nasabah2]
Bank = ATM('Cuan Cuan')

# mainProgram(Bank,nasabah1)
mainProgram(Bank,nasabah2)  

