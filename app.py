from flask import Flask, render_template,request, redirect, url_for
from models import MPeserta

application = Flask(__name__)

@application.route('/')
def index():
    model = MPeserta()
    container = []
    container = model.getProgram()
    return render_template('index.html',container=container)

@application.route('/daftar')
def daftar():
    model = MPeserta()
    container = []
    container = model.selectDB()
    return render_template('daftarproduk.html', container=container)
	
@application.route('/insert', methods=['GET', 'POST'])
def insert():
	if request.method == 'POST':
		nama = request.form['namalengkap']
		nik = request.form['nik']
		email = request.form['email']
		nowa = request.form['nowa']
		program = request.form['program']
		data = (nama, nik, email, nowa, program)
		model = MPeserta()
		model.insertDB(data)
		return redirect(url_for('daftar'))
	else:
		model = MPeserta()
		program = []
		program = model.getProgram()
		return render_template('insert_form.html',program=program)

@application.route('/input/<no>', methods=['GET', 'POST'])
def input(no):
	if request.method == 'POST':
		nama = request.form['namalengkap']
		nik = request.form['nik']
		email = request.form['email']
		nowa = request.form['nowa']
		program = request.form['program']
		data = (nama, nik, email, nowa, program)
		model = MPeserta()
		model.insertDB(data)
		return redirect(url_for('daftar'))
	else:
		no = no
		model = MPeserta()
		program = []
		program = model.getProgram()
		return render_template('insert_form.html',program=program,no=no)

@application.route('/update/<no>')
def update(no):
	model = MPeserta()
	program = []
	program = model.getProgram()
	data = model.getDBbyNo(no)
	return render_template('updateform.html', data = data, program=program)

@application.route('/update_process', methods=['GET', 'POST'])
def update_process():
	id = request.form['idpeserta']
	nama = request.form['namalengkap']
	nik = request.form['nik']
	email = request.form['email']
	nowa = request.form['nowa']
	program = request.form['program']
	data = (nama, nik, email, nowa, program,id)
	model = MPeserta()
	model.updateDB(data)
	
	return redirect(url_for('daftar'))

@application.route('/delete/<no>')
def delete(no):
    model = MPeserta()
    model.deleteDB(no)
    return redirect(url_for('daftar'))
                            
if __name__ == '__main__':
    application.run(debug=True)