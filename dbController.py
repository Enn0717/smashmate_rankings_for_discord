import sqlite3
import getFromSite

dbname = ("users.db")
conn = sqlite3.connect(dbname,isolation_level=None)
cursor = conn.cursor()

def dbinit():
	sql = """CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, name, rate, smashmate_id,discord_id)"""
	cursor.execute(sql)
	
def dbinsertNameAndSmashmateId(name,smashmate_id):
	sql="""INSERT INTO users(name,smashmate_id) VALUES(?,?)"""
	data=((name,smashmate_id))
	cursor.execute(sql,data)
	
def dbPrintall():
	sql="""SELECT * FROM users"""
	cursor.execute(sql)
	sql='select * from users order by rate;'
	cursor.execute(sql)
	return cursor.fetchall()
	
def dbdelete(discord_id):
	cursor.execute("delete from users where discord_id=?",(discord_id,))

def dbMakeUser(name,discord_id):
	if dbCheckUserExists(discord_id):
		return dbCheckUserExists(discord_id)
	else:
		sql="""INSERT INTO users(name, discord_id) VALUES (?,?) """
		data=((name,discord_id))
		cursor.execute(sql,data)

def dbNameUpdate(name,discord_id):
	sql='UPDATE users SET name = ? WHERE discord_id = ?;'
	data=(name,discord_id)
	cursor.execute(sql,data)

def dbCheckUserExists(discord_id):
	sql = 'select * from users where discord_id = ? '
	data = (discord_id, )
	if cursor.execute(sql, data).fetchall():
		return cursor.execute(sql, data).fetchall()
	else:
		return False

def dbUpdaterate(discord_id,rate):
	sql = 'UPDATE users SET rate = ? WHERE discord_id = ?;'
	data=(rate,discord_id)
	cursor.execute(sql,data)

def dbUpdaterateBysmashmate_id(smashmate_id,rate):
	sql = 'UPDATE users SET rate = ? WHERE smashmate_id = ?;'
	data=(rate,smashmate_id)
	cursor.execute(sql,data)

def dbSetSmashmate_id(discord_id,smashmate_id):
	sql = 'UPDATE users SET smashmate_id = ? WHERE discord_id = ?;'
	data=(smashmate_id,discord_id)
	cursor.execute(sql,data)

def dbReadSmashmateID(discord_id):
	sql = 'select smashmate_id from users where discord_id = ? '
	data = (discord_id, )
	return cursor.execute(sql, data).fetchall()[0][0]

def dbReadname(discord_id):
	sql = 'select name from users where discord_id = ? '
	data = (discord_id, )
	return cursor.execute(sql, data).fetchall()[0][0]