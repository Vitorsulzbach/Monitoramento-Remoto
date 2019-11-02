import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.dates as mdates
import numpy as np
import datetime
import pytz
import scipy.stats as sts

mode = 0
pos = 3
recalculate = False

#x=[datetime.datetime(2019, 6, (1+int(i/24)),(i%24),00) for i in range(100)]
#b=[]
#st=[]
#for i in range(100):
#	nn=[]
#	for j in range(100):
#		nn.append(np.random.normal(0,1))
#	st.append(np.std(nn))
#	b.append(sum(nn)/100)

def gerargra(b,st,x,idd):
	LSC = 0.6
	LIC = -0.6
	m = 0
	ms = 1
	sigmax = 0.1
	c4 = 0.9896
	LSE = 0.8
	LIE = -0.8
	sigmaS = (ms/c4)*np.sqrt((1-np.square(c4)))
	LSCs = ms+3*sigmaS
	LICs = ms-3*sigmaS
	date1 = x[0]
	date2 = x[len(x)-1]
	n=len(b)
	nn = 100
	fig, (ax1,ax2) = plt.subplots(2,1, sharey=False, figsize=(9,12))
	fig.subplots_adjust(left=0.07, bottom=0.1, right=0.8, top=0.98, wspace=0.95, hspace=0.3)
	plt.sca(ax1)

	#Poluição das amostras para causar saída de controle
	if(mode==1):
		for i in range(8):
			b.pop(pos+i)
			b.insert(pos+i, m+0.03)
			st.pop(pos+i)
			st.insert(pos+i, ms+0.02)
	if(mode==2):
		for i in range(8):
			b.pop(pos+i)
			b.insert(pos+i, m-0.03)
			st.pop(pos+i)
			st.insert(pos+i, ms-0.02)
	if(mode==3):
		num=[1,1,0,1,1]
		for i in range(5):
			b.pop(pos+i)
			b.insert(pos+i, m+(sigmax*num[i]+0.03))
			st.pop(pos+i)
			st.insert(pos+i, ms+(sigmaS*num[i]+0.02))
	if(mode==4):
		num=[1,1,0,1,1]
		for i in range(5):
			b.pop(pos+i)
			b.insert(pos+i, m-(sigmax*num[i]+0.03))
			st.pop(pos+i)
			st.insert(pos+i, ms-(sigmaS*num[i]+0.02))
	if(mode==4):
		num=[1,1,0,1,1]
		for i in range(5):
			b.pop(pos+i)
			b.insert(pos+i, m-(sigmax*num[i]+0.03))
			st.pop(pos+i)
			st.insert(pos+i, ms-(sigmaS*num[i]+0.02))
	if(mode==5):
		num=[1,0,1]
		for i in range(3):
			b.pop(pos+i)
			b.insert(pos+i, m+((2*sigmax*num[i])+0.03))
			st.pop(pos+i)
			st.insert(pos+i, ms+((2*sigmaS*num[i])+0.02))
	if(mode==6):
		num=[1,0,1]
		for i in range(3):
			b.pop(pos+i)
			b.insert(pos+i, m-((2*sigmax*num[i])+0.03))
			st.pop(pos+i)
			st.insert(pos+i, ms-((2*sigmaS*num[i])+0.02))
	if(mode==7):
		b.pop(pos)
		b.insert(pos, m+((3*sigmax)+0.03))
		st.pop(pos)
		st.insert(pos, ms+((3*sigmaS)+0.02))
	if(mode==8):
		b.pop(pos)
		b.insert(pos, m-((3*sigmax)+0.03))
		st.pop(pos)
		st.insert(pos, ms-((3*sigmaS)+0.02))
	if(mode==9):
		for i in range(8):
			b.pop(pos+i)
			b.insert(pos+i, 1)
			st.pop(pos+i)
			st.insert(pos+i, 2)
	if(recalculate == True):
		m = sum(b)/n
		ms = sum(st)/n
		sigmax =  ms/np.sqrt(nn)
		LSC = 3*sigmax+m
		LIC = -3*sigmax+m

	mcp = sum(st)/n
	sigmacp =  mcp/np.sqrt(nn)

	plt.xticks(rotation=30)
	plt.plot([date1,date2],[m,m], 'r--', label='LC')
	plt.plot([date1,date2],[LSC,LSC], 'c--', label='LSC')
	plt.plot([date1,date2],[LIC,LIC], 'g--', label='LIC')
	plt.plot(x, b, label='Média')

	ii1 = []
	i2  = 0
	ii2 = b[0:3]
	iii2= []
	i3  = 0
	ii3 = b[0:5]
	iii3= []
	ii4 = b[0:8]
	iii4= []
	for i in range(len(b)):
		ii4.pop(0)
		ii4.append(b[i])
		ii3.pop(0)
		ii3.append(b[i])
		ii2.pop(0)
		ii2.append(b[i])
		if(((ii4[0]>m)&(ii4[1]>m)&(ii4[2]>m)&(ii4[3]>m)&(ii4[4]>m)&(ii4[5]>m)&(ii4[6]>m)&(ii4[7]>m))|((ii4[0]<m)&(ii4[1]<m)&(ii4[2]<m)&(ii4[3]<m)&(ii4[4]<m)&(ii4[5]<m)&(ii4[6]<m)&(ii4[7]<m))):
			iii4.append(i)
		for k in range(5):
			if((ii3[k]>(sigmax))|(ii3[k]<(-sigmax))):
				i3=i3+1
			if(i3>3):
				iii3.append(i)
		i3=0
		for k in range(3):
			if((ii2[k]>(m+2*sigmax))|(ii2[k]<(m-2*sigmax))):
				i2=i2+1
			if(i2>1):
				iii2.append(i)
		i2 = 0
		if((b[i]>LSC)|(b[i]<LIC)):
			ii1.append(i)
	lm = (LSE-(sum(b)/n))/(3*sigmacp)
	if(lm>((m-LIE)/(3*sigmacp))):
		lm=((sum(b)/n)-LIE)/(3*sigmacp)
	Ppm=(1-(sts.norm.cdf(((LSC-m)/sigmax))-sts.norm.cdf(((LIC-m)/sigmax))))*1000000
	text1 = 'LC: ' + str(round(m,8))
	text2 = 'LSC: ' + str(round(LSC,8))
	text3 = 'LIC: ' + str(round(LIC,8))
	text4 = 'CP: ' + str(round((LSE-LIE)/(6*sigmacp),4))
	text5 = 'CPK: ' + str(round(lm,4))
	text9 = 'Características Gerais:'
	text10 = 'DPM: ' + str(round((1-(sts.norm.cdf(((LSC-(sum(b)/n))/sigmacp))-sts.norm.cdf(((LIC-m)/sigmacp))))*1000000,1))
	plt.gcf().text(0.82, 0.86, text1, fontsize=10)
	plt.gcf().text(0.82, 0.84, text2, fontsize=10)
	plt.gcf().text(0.82, 0.82, text3, fontsize=10)
	plt.gcf().text(0.81, 0.78, text9, fontsize=10)
	plt.gcf().text(0.82, 0.76, text4, fontsize=10)
	plt.gcf().text(0.82, 0.74, text5, fontsize=10)
	plt.gcf().text(0.82, 0.72, text10, fontsize=10)
	if((len(ii1)+len(iii2)+len(iii3)+len(iii4))>0):
		plt.gcf().text(0.805, 0.69, 'FORA DE CONTROLE:',color='red', fontsize=12)
		if(len(iii4)>0):
			plt.gcf().text(0.82, 0.67, 'regra 4',color='red', fontsize=12)
		if(len(iii3)>0):
			plt.gcf().text(0.82, 0.65, 'regra 3',color='red', fontsize=12)
		if(len(iii2)>0):
			plt.gcf().text(0.82, 0.63, 'regra 2',color='red', fontsize=12)
		if(len(ii1)>0):
			plt.gcf().text(0.82, 0.61, 'regra 1',color='red', fontsize=12)
	
	ax1.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m/%y %H:%M:%S"))
	ax1.set_xlim([date1,date2])
	ax1.set_ylim([-4*sigmax+m, 4*sigmax+m])
	ax1.legend(bbox_to_anchor=(1.06 ,0.98))

	plt.sca(ax2)

	if(recalculate==True):
		sigmaS = (ms/c4)*np.sqrt((1-np.square(c4)))
		LSCs = ms+3*sigmaS
		LICs = ms-3*sigmaS

	plt.plot([date1,date2],[ms,ms], 'r--', label='LC')
	plt.plot([date1,date2],[LSCs,LSCs], 'c--', label='LSC')
	plt.plot([date1,date2],[LICs,LICs], 'g--', label='LIC')
	plt.plot(x, st, label='Desvio Padrão')

	ii1 = []
	i2  = 0
	ii2 = st[0:3]
	iii2= []
	i3  = 0
	ii3 = st[0:5]
	iii3= []
	ii4 = st[0:8]
	iii4= []
	for i in range(len(st)):
		ii4.pop(0)
		ii4.append(st[i])
		ii3.pop(0)
		ii3.append(st[i])
		ii2.pop(0)
		ii2.append(st[i])
		if(((ii4[0]>ms)&(ii4[1]>ms)&(ii4[2]>ms)&(ii4[3]>ms)&(ii4[4]>ms)&(ii4[5]>ms)&(ii4[6]>ms)&(ii4[7]>ms))|((ii4[0]<ms)&(ii4[1]<ms)&(ii4[2]<ms)&(ii4[3]<ms)&(ii4[4]<ms)&(ii4[5]<ms)&(ii4[6]<ms)&(ii4[7]<ms))):
			iii4.append(i)
		for k in range(5):
			if((ii3[k]>(ms+sigmaS))|(ii3[k]<(ms-sigmaS))):
				i3=i3+1
				if(i3==4):
					print(i)
					print(len(st))
			if(i3>3):
				iii3.append(i)
		i3=0
		for k in range(3):
			if((ii2[k]>(ms+2*sigmaS))|(ii2[k]<(ms-2*sigmaS))):
				i2=i2+1
			if(i2>1):
				iii2.append(i)
		i2 = 0
		if((st[i]>LSCs)|(st[i]<LICs)):
			ii1.append(i)

	text6 = 'LC: ' + str(round(ms,8))
	text7 = 'LSC: ' + str(round(LSCs,8))
	text8 = 'LIC: ' + str(round(LICs,8))
	plt.gcf().text(0.82, 0.36, text6, fontsize=10)
	plt.gcf().text(0.82, 0.34, text7, fontsize=10)
	plt.gcf().text(0.82, 0.32, text8, fontsize=10)
	if(len(iii4)>0):
		plt.gcf().text(0.82, 0.28, 'regra 4',color='red', fontsize=12)
	if(len(iii3)>0):
		#iii3.append(1)
		plt.gcf().text(0.82, 0.26, 'regra 3',color='red', fontsize=12)
	if(len(iii2)>0):
		plt.gcf().text(0.82, 0.24, 'regra 2',color='red', fontsize=12)
	if(len(ii1)>0):
		plt.gcf().text(0.82, 0.22, 'regra 1',color='red', fontsize=12)

	ax2.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m/%y %H:%M:%S"))
	ax2.set_xlim([date1,date2])
	ax2.set_ylim([-4*sigmaS+ms, 4*sigmaS+ms])
	ax2.legend(bbox_to_anchor=(1.06 ,0.98))

	plt.xticks(rotation=30)
	plt.legend(bbox_to_anchor=(1.015 ,0.98))

	plt.savefig(('./static/graphs/'+str(idd)+'.png'))

