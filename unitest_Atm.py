import unittest
from ATM import nasabah2


class Test(unittest.TestCase):
    def test_Nabung(self):
        test1=nasabah2.saldoNambah(60000)
        self.assertEqual(test1,100000)
    def test_Narik(self):
        test1=nasabah2.saldoNgurang(60000)
        self.assertEqual(test1,40000)
    def test_Narik2(self):
        test1=nasabah2.saldoNgurang(20000)
        self.assertEqual(test1,'Maaf saldo anda tidak mencukupi')
        

if __name__ == '__main__':
    unittest.main()
