import os
import Get_files as Gf
import time
import signal

def timer(signum, frame):
	Gf.get_files()
	Gf.add_files_to_db()
	signal.alarm(100)

signal.signal(signal.SIGALRM, timer)
signal.alarm(1)

#Loop infinito
while(True):
	time.sleep(1000)
