import sqlite3
import datetime
import numpy as np

#Biblioteca para adicionar nova amostra

def add(x):
	change = "[{\"added\": {}}]"
	conn = sqlite3.connect('db.sqlite3')
	cursor = conn.cursor()
	média = str((float(sum(x[:99])/100)))
	now = x[100]
	n = x[:99]
	x.pop(100)
	x.insert(0,now)
	x.append(média)
	x.append(np.std(n))
	lista = [(x)]
	cursor.executemany("""insert into base_amostra (date_added,x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32,x33,x34,x35,x36,x37,x38,x39,x40,x41,x42,x43,x44,x45,x46,x47,x48,x49,x50,x51,x52,x53,x54,x55,x56,x57,x58,x59,x60,x61,x62,x63,x64,x65,x66,x67,x68,x69,x70,x71,x72,x73,x74,x75,x76,x77,x78,x79,x80,x81,x82,x83,x84,x85,x86,x87,x88,x89,x90,x91,x92,x93,x94,x95,x96,x97,x98,x99,média,sigma) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", lista)
	cursor.execute("""SELECT * FROM sqlite_sequence;""")
	linha = cursor.fetchall()
	amostra_id = linha[5][1]
	amostra_id = amostra_id + 1;
	lista2 = [(now,str(amostra_id),média,change,'8','1','1')]
	cursor.executemany("""insert into django_admin_log (action_time, object_id, object_repr,change_message, content_type_id, user_id, action_flag) values (?,?,?,?,?,?,?)""", lista2)
	conn.commit()
	cursor.close()

