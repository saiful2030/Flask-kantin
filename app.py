from flask import Flask, render_template, request, redirect, flash
from flask import render_template
from mysql import connector
from flask import request, redirect, url_for, session


app = Flask(__name__)


app.secret_key = 'kantin amikom'


db = connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='kantin'
)

if db.is_connected():
    print('Koneksi berhasil dibuka')


# Page login


@app.route('/')
def home():
    if not session.get('loggedin'):
        return redirect('/login')
    else:
        return redirect('/order/')

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = db.cursor()
        cursor.execute(
            'SELECT level FROM login WHERE username = %s AND password = %s',
            (username, password,)
        )
        user = cursor.fetchone()
        if user and user[0] == 'kasir':
            session['loggedin'] = True
            message = 'Berhasil login!'
            return redirect('/order/')
        elif user and user[0] == 'user':
            session['loggedin'] = True
            message = 'Berhasil login!'
            return redirect('/menu/')
        elif user and user[0] == 'dapur':
            session['loggedin'] = True
            message = 'Berhasil login!'
            return redirect('/dapur/')
        else:
            message = 'Silakan masukkan Username/kata sandi yang benar!'
    return render_template('login.html', message=message)


###################################################################################################################################


# Page Kasir


# Page Menu


@app.route('/edit_menu/')
def edit_menu():
    cursor = db.cursor()
    cursor.execute('select * from menu')
    result = cursor.fetchall()
    cursor.close()
    return render_template('kasir/edit_menu.html', hasil = result)

@app.route('/tambah_menu/')
def tambah_menu():
    return render_template('kasir/tambah_menu.html')

@app.route('/proses_tambah_menu/', methods = ['POST'])
def tambah_menu_baru():
    nama_menu = request.form['nama_menu']
    deskripsi = request.form['deskripsi']
    harga2 = request.form['harga2']
    kategori = request.form['kategori']
    cur = db.cursor()
    cur.execute("INSERT INTO menu (nama_menu, deskripsi, harga2, kategori) VALUES (%s, %s, %s, %s)", (nama_menu, deskripsi, harga2, kategori))
    db.commit()
    return redirect(url_for('edit_menu'))

@app.route('/hapus_menu/<id>', methods = ['GET'])
def hapus_menu(id):
    cur = db.cursor()
    cur.execute('DELETE from menu where id=%s', (id,))
    db.commit()
    return redirect(url_for('edit_menu'))

@app.route('/ubah_menu/<id>', methods=['GET'])
def ubah_menu(id):
    cur = db.cursor()
    cur.execute('select * from menu where id=%s', (id,))
    res = cur.fetchall()
    cur.close()
    return render_template('kasir/edit_menu2.html', hasil = res)

@app.route('/proses/ubah_menu/', methods=['POST'])
def proses_ubah_menu():
    nama_menu = request.form['nama_menu']
    nama_menu2 = request.form['nama_menu2']
    deskripsi = request.form['deskripsi']
    harga2 = request.form['harga2']
    kategori = request.form['kategori']
    cur = db.cursor()
    sql = "UPDATE menu SET nama_menu=%s, deskripsi=%s, harga2=%s, kategori=%s WHERE nama_menu=%s"
    values = (nama_menu2, deskripsi, harga2, kategori, nama_menu)
    cur.execute(sql, values)
    db.commit()
    return redirect(url_for('edit_menu'))


###################################################################################################################################


# Page order


@app.route('/order/')
def order():
    cursor = db.cursor()
    cursor.execute('select * from pesanan')
    result = cursor.fetchall()
    cursor.close()
    return render_template('kasir/order.html', hasil = result)

@app.route('/tambah_order/')
def tambah_order():
    return render_template('kasir/tambah_order.html')

@app.route('/proses_tambah_order/', methods = ['POST'])
def tambah_order_baru():
    nama = request.form['nama']
    meja = request.form['meja']
    nama_menu = request.form['nama_menu']
    harga2 = request.form['harga2']
    catatan = request.form['catatan']
    cur = db.cursor()
    cur.execute("INSERT INTO pesanan (nama, meja,nama_menu, harga2, catatan) VALUES (%s,%s,%s, %s, %s)", (nama, meja, nama_menu, harga2, catatan))
    db.commit()
    return redirect(url_for('order'))

@app.route('/ubah_order/<id>', methods=['GET'])
def ubah_order(id):
    cur = db.cursor()
    cur.execute('select * from pesanan where id=%s', (id,))
    res = cur.fetchall()
    cur.close()
    return render_template('kasir/edit_order.html', hasil = res)

@app.route('/proses/ubah_order/', methods = ['POST'])
def proses_ubah_order():
    nama = request.form['nama']
    nama_baru = request.form['nama_baru']
    meja = request.form['meja']
    nama_menu = request.form['nama_menu']
    harga2 = request.form['harga2']
    catatan = request.form['catatan']
    cur = db.cursor()
    sql = "UPDATE pesanan SET nama=%s, meja=%s, nama_menu=%s, harga2=%s, catatan=%s WHERE nama=%s"
    values = (nama_baru, meja, nama_menu, harga2, catatan, nama)
    cur.execute(sql, values)
    db.commit()
    return redirect(url_for('order'))


###################################################################################################################################


# Page Payment


@app.route('/payment/')
def payment():
    cursor = db.cursor()
    cursor.execute('select * from payment')
    result = cursor.fetchall()
    cursor.close()
    return render_template('kasir/payment.html',hasil = result)

@app.route('/tambah_payment/')
def tambah_payment():
    return render_template('kasir/tambah_payment.html')

@app.route('/proses_tambah_payment/', methods = ['POST'])
def tambah_payment_baru():
    kasir = request.form['kasir']
    hari = request.form['hari']
    income = request.form['income']
    cur = db.cursor()
    cur.execute("INSERT INTO payment (kasir, hari, income) VALUES (%s, %s, %s)", (kasir, hari, income))
    db.commit()
    return redirect(url_for('payment'))


###################################################################################################################################


# Page Support


@app.route('/support/')
def support():
    return render_template('kasir/support.html')


###################################################################################################################################


# Page User


@app.route('/menu/')
def menu():
    cursor = db.cursor()
    cursor.execute('select * from menu')
    result = cursor.fetchall()
    cursor.close()
    return render_template('user/menu.html',hasil = result)

@app.route('/makanan/')
def makanan():
    cursor = db.cursor()
    cursor.execute('SELECT * FROM menu WHERE kategori = %s', ('makanan',))
    result = cursor.fetchall()
    cursor.close()
    return render_template('user/makanan.html', hasil = result)

@app.route('/minuman/')
def minuman():
    cursor = db.cursor()
    cursor.execute('SELECT * FROM menu WHERE kategori = %s', ('minuman',))
    result = cursor.fetchall()
    cursor.close()
    return render_template('user/minuman.html',hasil = result)


###################################################################################################################################

# Dapur


@app.route('/dapur/')
def dapur():
    cursor = db.cursor()
    cursor.execute('select * from pesanan')
    result = cursor.fetchall()
    cursor.close()
    return render_template('dapur/dapur.html',hasil = result)


@app.route('/hapus_order_dapur/<id>', methods = ['GET'])
def hapus_order_dapur(id):
    cur = db.cursor()
    cur.execute('DELETE from pesanan where id=%s', (id,))
    db.commit()
    return redirect(url_for('dapur'))


###################################################################################################################################

# General


@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('login'))


###################################################################################################################################


if __name__== '__main__':
    app.run()
    