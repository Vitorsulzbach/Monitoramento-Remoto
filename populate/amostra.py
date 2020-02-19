import requests
import numpy as np
import datetime
import signal, os
import time
import pytz
import time

num = 0

n = 0
IP_populate = ""

if(n==0):
	IP_populate = "http://0.0.0.0:8000/entryhumidity/"
else:
	IP_populate = "http://34.95.165.121:8000/"


while(1):
    t = {"x0":np.random.normal(0,1),"x1":np.random.normal(0,1),"x2":np.random.normal(0,1),"x3":np.random.normal(0,1),"x4":np.random.normal(0,1),"x5":np.random.normal(0,1),"x6":np.random.normal(0,1),"x7":np.random.normal(0,1),"x8":np.random.normal(0,1),"x9":np.random.normal(0,1),"x10":np.random.normal(0,1),"x11":np.random.normal(0,1),"x12":np.random.normal(0,1),"x13":np.random.normal(0,1),"x14":np.random.normal(0,1),"x15":np.random.normal(0,1),"x16":np.random.normal(0,1),"x17":np.random.normal(0,1),"x18":np.random.normal(0,1),"x19":np.random.normal(0,1),"x20":np.random.normal(0,1),"x21":np.random.normal(0,1),"x22":np.random.normal(0,1),"x23":np.random.normal(0,1),"x24":np.random.normal(0,1),"date":(str((datetime.datetime.now()+datetime.timedelta(minutes = 30*num)).strftime("%Y-%m-%d %H:%M:%S"))+"+0000")}
    try:
        r = requests.post(IP_populate, data=t)
        print(r)
    except:
        print("Deu ruim no request!")
    num = num + 1
    print(str(num)+" ciclo!")

datetime.timedelta(minutes = 10)
