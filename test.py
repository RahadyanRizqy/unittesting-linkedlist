import unittest
from linkedlist import LinkedList

class MyUnitTesting(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.ll1 = LinkedList(1,2,3,4,5,6,7,8)
        self.list1 = [1,2,3,4,5,6,7,8]

    def testSameIndex(self):
        self.assertEqual(self.ll1.getIndex(4), self.list1.index(4))
        self.assertTrue(self.ll1.getIndex(4) == self.list1.index(4))
        # BENAR KARENA INDEX DARI ANGKA 4 PADA LINKEDLIST SAMA DENGAN INDEX DARI ANGKA 4 LIST

    def testSameAppend(self):
        self.ll1.insertAtEnd(0)
        self.list1.append(0)
        ll1_last = self.ll1[self.ll1.__len__() - 1]
        list1_last = self.list1[-1]
        # OTOMATIS PANJANG ELEMEN BERTAMBAH 1 YANG BERARTI 9 ELEMEN
        # INDEKS ELEMEN AKHIR = PANJANG ELEMEN - 1
        self.assertEqual(ll1_last, list1_last)
        self.assertTrue(ll1_last == list1_last)
        # BENAR KARENA INSERTATEND MEMASUKKAN ELEMEN DI AKHIR LINKEDLIST SEBAGAIMANA APPEND DI LIST

    def testGetElement(self):
        self.assertEqual(self.ll1[5], self.list1[5])
        self.assertTrue(self.ll1[5] == self.list1[5])
        # BENAR KARENA GETITEM PADA LINKEDLIST MELAKUKAN IMITASI SEBAGAIMANA INDEXING PADA LIST

    def testSameLength(self):
        self.assertCountEqual(self.ll1, self.list1)
        self.assertTrue(self.ll1.__len__() == self.list1.__len__())
        # BENAR KARENA LINKEDLIST SUDAH ITERABLE SEHINGGA DAPAT MENGHITUNG BANYAKNYA ELEMEN

    def testSameListPop(self):
        ll1_pop_value = self.ll1.listPop()
        list1_pop_value = self.list1.pop()
        self.assertEqual(ll1_pop_value, list1_pop_value)
        # SALAH HARUSNYA MENGHILANGKAN ELEMEN DAN MENGELUARKAN ELEMEN YANG DIHILANGKAN
        # listPop() harusnya mengeluarkan 8 dan tetapi mengeluarkan None
        # Sehingga None != 8 menghasilkan fail
        self.assertFalse(ll1_pop_value == list1_pop_value)
        # Dapat dibuktikan bahwa dengan assertFalse bernilai true, bahwa perbandingan hasil return tidak sesuai

if __name__ == '__main__':
    unittest.main()