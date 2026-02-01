from flask import Flask, redirect,render_template,request, url_for 
from class_test import tabledb
import os 
import sqlite3

databasename = os.getcwd() + '/tes.db'



app = Flask(__name__)



@app.route('/')
def index():
    conn = sqlite3.connect(databasename)
    cursor = conn.cursor() 
    container = []
    for nomor,nama,harga in cursor.execute('SELECT * FROM dbtes'):
        model = tabledb(nomor,nama,harga)
        container.append(model)
    conn.commit()
    cursor.close()
    conn.close()
    return render_template('index.html',container=container)

@app.route('/tambah',methods=['GET','POST'])
def tambah():
    if request.method =='POST':
        nomor = int(request.form['nomor'])
        nama = request.form['nama']
        harga = int(request.form['harga'])
        model = tabledb(nomor,nama,harga)
        model.tambah()
        return redirect(url_for('index'))
    return f"""
        <h1>Tambah</h1>
        <form method='POST'>  
        <input type='number' name='nomor' placeholder='masukan nomor'><br>
        <input type="text" name="nama" placeholder="masukan nama"><br>
        <input type="number" name="harga" placeholder="masukan harganya"><br>
        <input type="submit" value="kirim">
        </form>
        <button>
        <a href="{url_for('index')}">Kembali</a>
        </button>
    """
@app.route('/ubah/<int:id>',methods=['GET','POST'])
def ubah(id):
    model = tabledb()
    model.load(id)
    if request.method=='POST':
        nomor = int(request.form['nomor'])
        nama = request.form['nama']
        harga = int(request.form['harga'])
        model = tabledb(nomor,nama,harga)
        model.ubah()
        return redirect(url_for('index'))
    return f"""
    <h1>Ubah</h1>
     <form method='POST'>  
        <input type='number' name='nomor' placeholder='masukan nomor'><br>
        <input type="text" name="nama" placeholder="masukan nama"><br>
        <input type="number" name="harga" placeholder="masukan harganya"><br>
        <input type="submit" value="kirim"><br> 
    </form> 
     <button>
        <a href="{url_for('index')}">Kembali</a>
        </button>
    """

# hapus 
@app.route('/hapusdata/<int:id>')
def hapus(id):
   model = tabledb()
   model.load(id)
   model.hapus()
   return redirect(url_for('index'))
   


if __name__=="__main__":
    app.run(debug=True)
