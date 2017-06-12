import sqlite3
import datetime

# Use 4 spaces as indent


def getConnection():
    return sqlite3.connect('addressbook.db')

def getPerson():
    # Connection 으로부터 Cursor 생성
    conn = getConnection()

    curs = conn.cursor()

    # SQL문 실행
    sql = "SELECT * FROM addressbook ORDER BY name"
    curs.execute(sql)

    # 데이타 Fetch
    row = curs.fetchall()

    # Connection 닫기
    conn.close()

    return row


def setPerson(name, number, email):
    conn = getConnection()
    curs = conn.cursor()

    curs.execute("INSERT INTO ADDRESSBOOK VALUES(?, ?, ?, ?)", (None, name, number, email))

    conn.commit()

    conn.close()

def searchPerson(key):
    conn = getConnection()
    curs = conn.cursor()

    curs.execute("SELECT * FROM ADDRESSBOOK WHERE name LIKE ?", ('%{}%'.format(key),))
    row1 = curs.fetchall()

    curs.execute("SELECT * FROM ADDRESSBOOK WHERE number LIKE ?", ('%{}%'.format(key),))
    row2 = curs.fetchall()

    curs.execute("SELECT * FROM ADDRESSBOOK WHERE email LIKE ?", ('%{}%'.format(key),))
    row3 = curs.fetchall()

    conn.close()


    if key == "":
        return row1

    else:
        return row1 + row2 + row3

def searchById(id):
    conn = getConnection()
    curs = conn.cursor()

    curs.execute("SELECT * FROM ADDRESSBOOK WHERE id=?", (id,))
    row = curs.fetchall()

    conn.close()

    return row

def deletePerson(key):
    conn = getConnection()
    curs = conn.cursor()

    curs.execute('''DELETE FROM ADDRESSBOOK WHERE id = ?''', (key,))

    conn.commit()

    conn.close()

def writePerson(name, number, email):
    conn = getConnection()
    curs = conn.cursor()

    curs.execute("UPDATE ADDRESSBOOK SET name = ? , number = ?, email = ? WHERE name= ?", (name,number,email,name))

    conn.commit()

    conn.close()


def getCall():
    conn = getConnection()

    curs = conn.cursor()

    sql = "select * from call"
    curs.execute(sql)

    row = curs.fetchall()

    for hist in range(len(row)):
        if searchName(row[hist][1]) != []:
            result = searchName(row[hist][1])
            row[hist] = row[hist][:1] + (result[0][1],) + row[hist][2:]

    conn.close()

    return row


def addCall(number):
    conn = getConnection()

    curs = conn.cursor()
    now = datetime.datetime.now()
    time = str(now.year) +'-'+  str(now.month) +'-' + str(now.day) + ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
    curs.execute("INSERT INTO call VALUES(?, ?, ?, ?)", (time, number, 0, 20))
    conn.commit()

    conn.close()


def addSms(number, text):
    conn = getConnection()

    curs = conn.cursor()
    now = datetime.datetime.now()
    time = str(now.year) +'-'+  str(now.month) +'-' + str(now.day) + ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
    curs.execute("INSERT INTO sms VALUES(?, ?, ?, ?)", (time, number, 0 , str(text)))
    conn.commit()

    conn.close()    

def setCall():
    conn = getConnection()

    cur = conn.cursor()

    # TODO : query

    conn.commit()

    conn.close()

    return; # maybe TODO


def getMsg():
    conn = getConnection()

    curs = conn.cursor()

    sql = "select * from sms"
    curs.execute(sql)

    row = curs.fetchall()

    for hist in range(len(row)):
        if searchName(row[hist][1]) != []:
            result = searchName(row[hist][1])
            row[hist] = row[hist][:1] + (result[0][1],) + row[hist][2:]

    conn.close()

    return row


def searchName(num):
    conn = getConnection()
    curs = conn.cursor()

    curs.execute("SELECT * FROM ADDRESSBOOK WHERE number=?", (num,))
    row = curs.fetchall()

    conn.close()

    return row


def changePerson(name, number, email, id):
    conn = getConnection()
    curs = conn.cursor()

    curs.execute("""UPDATE ADDRESSBOOK SET name = ? ,number = ?,email = ? WHERE id= ? """,
  (name,number,email,id))

    conn.commit()

    conn.close()
