import pysftp
import paramiko
import Db_adder as db
import os

def get_files():
	localpath = '/home/vitor/django/TCC/Files/'
	myHostname = "192.168.25.3"
	myUsername = "pi"
	myPassword = "7038"
	cnopts = pysftp.CnOpts()
	cnopts.hostkeys = None 
	namefile = []
	with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword, cnopts=cnopts) as sftp:
		sftp.cwd('/home/pi/CEP/')
		directory_structure = sftp.listdir_attr()
		for i in range(len(directory_structure)):
			namefile.append(directory_structure[i].filename)
		for s in namefile:
			remotepath='/home/pi/CEP/'+s
			sftp.get(remotepath,(localpath+s))
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname = myHostname, username = myUsername, password = myPassword)
	ssh.invoke_shell()
	for j in namefile:
		ssh.exec_command (('rm ./CEP/'+j))

def add_files_to_db():
	path = '/home/vitor/django/TCC/Files/'
	files = []
	for r, d, f in os.walk(path):
		for file in f:
			if '.txt' in file:
				files.append(os.path.join(r, file))

	for i in range(len(files)):
		files[i] = files[i][29:]
		f = open((path+files[i]),'rt')
		inf = f.read()
		f.close()
		x = []
		buff=-1
		for n in range(len(inf)):
			if(inf[n]=='/'):
				x.append(float(inf[(buff+1):n]))
				buff=n
		x.append(inf[(buff+1):])
		db.add(x)
		del(x)
		os.system(('rm ' + path + files[i]))

