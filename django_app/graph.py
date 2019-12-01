import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.dates as mdates
import numpy as np
import datetime
import pytz
import scipy.stats as sts

class Graph:
	LSC = 0.6
	LIC = -0.6
	LSE = 0.6
	LIE = -0.6
	LSCs = 1.436160911
	LICs = -0.563839089
	LSEs = 0.6
	LIEs = -0.6
	LC = 0
	LCs = 1
	c4 = 0.9896
	qtdReadings = 25
	sigmaS = (LCs/c4)*np.sqrt((1-np.square(c4)))
	LSCs = LCs+3*sigmaS
	LICs = LCs-3*sigmaS
	
	def __init__(self, samples, stndr, date, idd):
		self.samples = samples #amostras
		self.stndr = stndr #desvio
		self.date = date #data
		self.idd = idd #name
		self.calculaSize()
		if(self.size>0):
			self.date1 = date[0]
			self.date2 = date[self.size-1]
		else:
			return
		self.calculaMediaStndr()
		self.calculaSigmaCP()
		self.calculaCP()
		self.calculaCPK()
		self.calculaDPM()
		self.catchRulesM()
		self.catchRulesS()
		self.geraGraficoHumidity()
	
	def calculaSize(self):
		self.size = len(self.samples)
	
	def calculaMediaStndr(self):
		self.mediaStndr = np.mean(self.stndr)
		
	def calculaSigmaCP(self):
		self.sigmaCP =  self.mediaStndr/np.sqrt(self.qtdReadings)
	
	def calculaCP(self):
		self.CP = x = round((self.LSE-self.LIE)/(6*self.sigmaCP), 4)
		
	def calculaCPK(self):
		self.CPK = round((self.LSE-np.mean(self.samples))/(3*self.sigmaCP),4)
		if(self.CPK>round((np.mean(self.samples)-self.LIE)/(3*self.sigmaCP),4)):
			self.CPK=round((np.mean(self.samples)-self.LIE)/(3*self.sigmaCP),4)

	def calculaDPM(self):
		self.DPM = round((1-(sts.norm.cdf((self.LSC-np.mean(self.samples))/self.sigmaCP)-(sts.norm.cdf((self.LIC-np.mean(self.samples))/self.sigmaCP))))*1000000,2)

	def catchRulesM(self):
		self.rule1HM = False
		self.rule2HM = False
		self.rule3HM = False
		self.rule4HM = False
		ii1 = []
		i2  = 0
		ii2 = [0]
		if(self.size > 2):
			ii2 = self.samples[0:3]
		iii2= []
		i3  = 0
		ii3 = [0]
		if(self.size > 4):
			ii3 = self.samples[0:5]
		iii3= []
		ii4 = [0]
		if(self.size > 7):
			ii4 = self.samples[0:8]
		iii4= []
		for i in range(self.size):
			ii4.pop(0)
			ii4.append(self.samples[i])
			ii3.pop(0)
			ii3.append(self.samples[i])
			ii2.pop(0)
			ii2.append(self.samples[i])
			if(self.size > 7):
				if(((ii4[0]>self.LC)&(ii4[1]>self.LC)&(ii4[2]>self.LC)&(ii4[3]>self.LC)&(ii4[4]>self.LC)&(ii4[5]>self.LC)&(ii4[6]>self.LC)&(ii4[7]>self.LC))|((ii4[0]<self.LC)&(ii4[1]<self.LC)&(ii4[2]<self.LC)&(ii4[3]<self.LC)&(ii4[4]<self.LC)&(ii4[5]<self.LC)&(ii4[6]<self.LC)&(ii4[7]<self.LC))):
					iii4.append(i)
					self.rule4HM = True
			if(self.size > 4):
				for k in range(5):
					if((ii3[k]>self.LSC*3)|(ii3[k]<self.LIC*3)):
						i3=i3+1
					if(i3>3):
						iii3.append(i)
						self.rule3HM = True
				i3=0
			if(self.size > 2):
				for k in range(3):
					if((ii2[k]>self.LSC*(2/3)))|(ii2[k]<self.LIC*(2/3)):
						i2=i2+1
					if(i2>1):
						iii2.append(i)
						self.rule2HM = True
				i2 = 0
			if((self.samples[i]>self.LSC)|(self.samples[i]<self.LIC)):
				ii1.append(i)
				self.rule1HM = True

	def catchRulesS(self):
		self.rule1HS = False
		self.rule2HS = False
		self.rule3HS = False
		self.rule4HS = False
		ii1 = []
		i2  = 0
		ii2 = [0]
		if(self.size > 2):
			ii2 = self.stndr[0:3]
		iii2= []
		i3  = 0
		ii3 = [0]
		if(self.size > 4):
			ii3 = self.stndr[0:5]
		iii3= []
		ii4 = [0]
		if(self.size > 7):
			ii4 = self.stndr[0:8]
		iii4= []
		for i in range(self.size):
			ii4.pop(0)
			ii4.append(self.stndr[i])
			ii3.pop(0)
			ii3.append(self.stndr[i])
			ii2.pop(0)
			ii2.append(self.stndr[i])
			if(self.size > 7):
				if(((ii4[0]>self.LCs)&(ii4[1]>self.LCs)&(ii4[2]>self.LCs)&(ii4[3]>self.LCs)&(ii4[4]>self.LCs)&(ii4[5]>self.LCs)&(ii4[6]>self.LCs)&(ii4[7]>self.LCs))|((ii4[0]<self.LCs)&(ii4[1]<self.LCs)&(ii4[2]<self.LCs)&(ii4[3]<self.LCs)&(ii4[4]<self.LCs)&(ii4[5]<self.LCs)&(ii4[6]<self.LCs)&(ii4[7]<self.LCs))):
					iii4.append(i)
					self.rule4HS = True
			if(self.size > 4):
				for k in range(5):
					if((ii3[k]>self.LSC*3)|(ii3[k]<self.LIC*3)):
						i3=i3+1
					if(i3>3):
						iii3.append(i)
						self.rule3HS = True
				i3=0
			if(self.size > 2):
				for k in range(3):
					if((ii2[k]>self.LSC*(2/3)))|(ii2[k]<self.LIC*(2/3)):
						i2=i2+1
					if(i2>1):
						iii2.append(i)
						self.rule2HS = True
				i2 = 0
			if((self.stndr[i]>self.LSC)|(self.stndr[i]<self.LIC)):
				ii1.append(i)
				self.rule1HS = True

	def geraGraficoHumidity(self):
		fig, (ax1,ax2) = plt.subplots(2,1, sharey=False, figsize=(9,12))
		fig.subplots_adjust(left=0.07, bottom=0.1, right=0.8, top=0.98, wspace=0.95, hspace=0.3)
		plt.sca(ax1)
		plt.xticks(rotation=30)
		plt.plot([self.date1,self.date2],[self.LC,self.LC], 'r--', label='LC')
		plt.plot([self.date1,self.date2],[self.LSC,self.LSC], 'c--', label='LSC')
		plt.plot([self.date1,self.date2],[self.LIC,self.LIC], 'g--', label='LIC')
		plt.plot(self.date, self.samples, label='Média')
		ax1.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m/%y %H:%M:%S"))
		ax1.set_xlim([self.date1,self.date2])
		#ax1.set_ylim([-4*sigmax+m, 4*sigmax+m])
		ax1.legend(bbox_to_anchor=(1.19 ,0.98))
		plt.sca(ax2)
		plt.plot([self.date1,self.date2],[self.LCs,self.LCs], 'r--', label='LC')
		plt.plot([self.date1,self.date2],[self.LSCs,self.LSCs], 'c--', label='LSC')
		plt.plot([self.date1,self.date2],[self.LICs,self.LICs], 'g--', label='LIC')
		plt.plot(self.date, self.stndr, label='Desvio Padrão')
		ax2.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m/%y %H:%M:%S"))
		ax2.set_xlim([self.date1,self.date2])
		#ax2.set_ylim([-4*sigmaS+ms, 4*sigmaS+ms])
		ax2.legend(bbox_to_anchor=(1.06 ,0.98))

		plt.xticks(rotation=30)
		plt.legend(bbox_to_anchor=(1.015 ,0.98))
		plt.savefig(('./static/graphs/'+str(self.idd)+'.png'))

