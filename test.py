from flask import Flask, redirect,render_template,request, url_for 
from class_test import tabledb
import os 
import sqlite3



# rute database file
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
    <!DOCTYPE html>
        <html>
            <head>
                <title>Tambah</title>
                <style>
                * {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}

body {{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #fef3f2 0%, #fce7db 100%);
    min-height: 100vh;
    padding: 40px 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}}

h1 {{
    text-align: center;
    color: #7c2d12;
    font-size: 2.5rem;
    margin-bottom: 40px;
    font-weight: 300;
    letter-spacing: 2px;
    animation: fadeInDown 0.8s ease;
}}

@keyframes fadeInDown {{
    from {{
        opacity: 0;
        transform: translateY(-30px);
    }}
    to {{
        opacity: 1;
        transform: translateY(0);
    }}
}}

form {{
    background: white;
    padding: 40px;
    border-radius: 8px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.08);
    max-width: 500px;
    width: 100%;
    animation: fadeInUp 1s ease;
}}

@keyframes fadeInUp {{
    from {{
        opacity: 0;
        transform: translateY(30px);
    }}
    to {{
        opacity: 1;
        transform: translateY(0);
    }}
}}

input[type="number"],
input[type="text"] {{
    width: 100%;
    padding: 15px 20px;
    margin-bottom: 20px;
    border: 2px solid #fed7aa;
    border-radius: 6px;
    font-size: 1rem;
    color: #78350f;
    transition: all 0.3s ease;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}}

input[type="number"]:focus,
input[type="text"]:focus {{
    outline: none;
    border-color: #ea580c;
    box-shadow: 0 0 0 3px rgba(234, 88, 12, 0.1);
}}

input[type="number"]::placeholder,
input[type="text"]::placeholder {{
    color: #9ca3af;
}}

input[type="submit"] {{
    width: 100%;
    padding: 15px 20px;
    background: #ea580c;
    color: white;
    border: 2px solid #ea580c;
    border-radius: 6px;
    font-size: 1rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s ease;
    text-transform: uppercase;
    letter-spacing: 1px;
}}

input[type="submit"]:hover {{
    background: #c2410c;
    border-color: #c2410c;
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(234, 88, 12, 0.25);
}}

input[type="submit"]:active {{
    transform: translateY(0);
}}

button {{
    margin-top: 20px;
    padding: 0;
    background: white;
    border: 2px solid #ea580c;
    border-radius: 6px;
    cursor: pointer;
    box-shadow: 0 2px 8px rgba(234, 88, 12, 0.15);
    transition: all 0.3s ease;
}}

button:hover {{
    background: #ea580c;
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(234, 88, 12, 0.25);
}}

button:active {{
    transform: translateY(0);
}}

button a {{
    display: block;
    padding: 12px 28px;
    color: #ea580c;
    text-decoration: none;
    font-weight: 500;
    font-size: 0.95rem;
    transition: all 0.3s ease;
}}

button:hover a {{
    color: white;
}} 
        </style>
            </head>
            <body>
            <h1>Tambah Data</h1>
                <form method='POST'>
                    <input type="number" name="nomor" placeholder="Masukkan nomor " required><br>
                    <input type="text" name="nama" placeholder="Masukkan nama " required><br>
                    <input type="number" name="harga" placeholder="Masukkan harga " required><br>
                    <input type="submit" value="Kirim Data">
                </form>
                <button>
                <a href="{url_for('index')}">← Kembali</a>
                </button>
                <footer>
                 <p>Utamakan Input Nomor yang Belum Ada untuk Menghindari Konflik Data.</p>
                </footer>
            </body>
        </html>
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
    app.run(host='0.0.0.0', port=5000, debug=True)
