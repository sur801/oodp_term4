from flask import render_template
from flask import Flask, request, flash, redirect, url_for

#from sql_connect import getPerson, getCall, getMsg
import sqlite3
from sql_conn3 import getConnection, getPerson, getCall, getMsg, setPerson, searchPerson, searchName, changePerson, deletePerson

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/', methods = ['POST','GET'])
def main(name=None):
	if(request.method == 'POST'):
		key = request.form['keyword']
		return render_template('main.html', person=searchPerson(key))
		#return render_template('searchResult.html',s_person=searchPerson(key))
	
	return render_template('main.html', name=name, person=getPerson())


@app.route('/call_hist')
def call_hist():
	return render_template('call_hist.html', call=getCall())

@app.route('/searchResult')
def searchResult():
	return render_template('searchResult.html')
	
@app.route('/sms_hist')
def sms_hist():
	return render_template('sms_hist.html', sms=getMsg())



# @app.route('/delete', methods = ['POST','GET'])
# def delete():
# 	value = request.data
# 	deletePerson(value)
# 	print (value)
# 	return redirect(url_for('editPerson'))

@app.route('/delete/<int:id>', methods = ['DELETE'])
def deleteUser(id):
	deletePerson(id)
	return redirect(url_for('main'))
	#return "ok", 200
	


@app.route('/addPerson', methods = ['POST', 'GET'])
def addPerson():
	error = None

	if request.method == 'POST':

		name = request.form['name']
		number = request.form['number']
		email = request.form['email']

		# TODO : Duplicate Check : not ready
		if searchName(number):
			error = 'Number is already in the Addressbook.'

		elif not name or not number or not email:
			error = 'Blank not allowed! Please fill in the all fields.'

		else:
			setPerson(name, number, email)
			return redirect(url_for('main'))

	return render_template('addPerson.html', error=error)


@app.route('/editPerson', methods = ['POST', 'GET'])
def editPerson():
	error=None

	if request.method == 'POST':
		name = request.form['name']
		number = request.form['number']
		email = request.form['email']

		if not name or not number or not email:
			error='Blank not allowed! Please fill in the all fields.'

		else:
			changePerson(name, number, email)
			return redirect(url_for('main'))

	return render_template('editPerson.html', error=error)

"""
@app.route('/add_entry', methods = ['POST', 'GET'])
def add_entry():
	if request.method == 'POST':
		try:
			name = request.form['name']
			number = request.form['number']
			email = request.form['email']
			
			with getConnection() as conn: 
				curs = conn.cursor()
				curs.execute("INSERT INTO ADDRESSBOOK VALUES(?, ?, ?, ?)", (None, name, number, email))

				conn.commit()

		except:
			conn.rollback()

		finally:
			return render_template('main.html')
			conn.close()
"""

app.run(debug=True, host='0.0.0.0')