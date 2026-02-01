import sqlite3 
import os 
databasename = os.getcwd() + '/tes.db'

class tabledb:
    def __init__(self,nomor=0,nama='',harga=0):
        self.nomor = nomor 
        self.nama = nama 
        self.harga = harga 

    
    def setnomor(self,nomor):
        self.nomor = nomor


    def setnama(self,nama):
        self.nama = nama 

    def setharga(self,harga):
        self.harga = harga

    
    # fitur tambah 
    def tambah(self):
        conn = sqlite3.connect(databasename)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO dbtes VALUES(?,?,?)',(self.nomor,self.nama,self.harga))
    
        conn.commit()
        cursor.close()
        conn.close()
    

    # fitur ubah 
    # menerima dua function 
    def ubah(self):
        conn = sqlite3.connect(databasename)
        cursor = conn.cursor()
        cursor.execute('UPDATE dbtes SET nama=?,harga=? WHERE nomor=?',(self.nama,self.harga,self.nomor))

        conn.commit()
        cursor.close()
        conn.close()

    # load isi database dan edit berdasarkan angka id
    def load(self,id):
        conn = sqlite3.connect(databasename)
        cursor = conn.cursor()
        for nomor,nama,harga in cursor.execute('SELECT * FROM dbtes'):
            if nomor ==id:
                self.nomor = nomor 
                self.nama = nama 
                self.harga = harga
        cursor.close()
        conn.close()

    # hapus isi database
    # dari nomor
    def hapus(self):
        conn = sqlite3.connect(databasename)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM dbtes WHERE nomor=?',(self.nomor,))
        conn.commit()
        cursor.close()
        conn.close()
