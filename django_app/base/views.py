from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .models import graphic, humidity, temperature, globalvar, longgraphic
import graph
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.db import models
import numpy as np
from django.utils.dateparse import parse_datetime
import pytz
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseNotFound
import dateutil.parser
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test

#ex time:'2019-06-15 22:52:34.810649'

#def staff_required(login_url=None):
#    return user_passes_test(u.is_staff)

def staff_check(user):
    return user.is_staff

class tes:
	def __init__(self, b,st,x):
		self.b = b
		self.st = st
		self.x = x

def index(request):
	return render(request, 'base/index.html')

@login_required
def longGraphic(request):
	try:
		new_graph = longgraphic.objects.get(tipo=False)
		a = humidity.objects.all()
		b = [tes(float(a[i].media),float(a[i].sigma),a[i].date) for i in range(len(a))]
		b.sort(key=lambda nn: nn.x)
		st = [b[i].st for i in range(len(b))]
		x = [b[i].x for i in range(len(b))]
		b = [b[i].b for i in range(len(b))]
		g = graph.Graph(b,st,x,"humidity", float(globalvar.objects.get(name="LCh").value),float(globalvar.objects.get(name="LSCh").value),float(globalvar.objects.get(name="LICh").value),float(globalvar.objects.get(name="LSEh").value),float(globalvar.objects.get(name="LIEh").value),float(globalvar.objects.get(name="LCsh").value),float(globalvar.objects.get(name="LSCsh").value),float(globalvar.objects.get(name="LICsh").value))
		g.geraGrafico()
		new_graph.img='graphs/humidity.png'
		new_graph.cp = g.CP
		new_graph.cpk = g.CPK
		new_graph.dpm = g.DPM
		new_graph.LC = round(g.LC,4)
		new_graph.LSC = round(g.LSC,4)
		new_graph.LIC = round(g.LIC,4)
		new_graph.LCs = round(g.LCs,4)
		new_graph.LSCs = round(g.LSCs,4)
		new_graph.LICs = round(g.LICs,4)
		new_graph.LSE = round(g.LSE,4)
		new_graph.LIE = round(g.LIE,4)
		new_graph.rule1m = g.rule1HM
		new_graph.rule2m = g.rule2HM
		new_graph.rule3m = g.rule3HM
		new_graph.rule4m = g.rule4HM
		new_graph.rule1s = g.rule1HS
		new_graph.rule2s = g.rule1HS
		new_graph.rule3s = g.rule1HS
		new_graph.rule4s = g.rule1HS
		new_graph.save()
		
		
		new_graph = longgraphic.objects.get(tipo=True)
		a = temperature.objects.all()
		b = [tes(float(a[i].media),float(a[i].sigma),a[i].date) for i in range(len(a))]
		b.sort(key=lambda nn: nn.x)
		st = [b[i].st for i in range(len(b))]
		x = [b[i].x for i in range(len(b))]
		b = [b[i].b for i in range(len(b))]
		g = graph.Graph(b,st,x,"temperature", float(globalvar.objects.get(name="LCt").value),float(globalvar.objects.get(name="LSCt").value),float(globalvar.objects.get(name="LICt").value),float(globalvar.objects.get(name="LSEt").value),float(globalvar.objects.get(name="LIEt").value),float(globalvar.objects.get(name="LCst").value),float(globalvar.objects.get(name="LSCst").value),float(globalvar.objects.get(name="LICst").value))
		g.geraGrafico()
		new_graph.img='graphs/temperature.png'
		new_graph.cp = g.CP
		new_graph.cpk = g.CPK
		new_graph.dpm = g.DPM
		new_graph.LC = round(g.LC,4)
		new_graph.LSC = round(g.LSC,4)
		new_graph.LIC = round(g.LIC,4)
		new_graph.LCs = round(g.LCs,4)
		new_graph.LSCs = round(g.LSCs,4)
		new_graph.LICs = round(g.LICs,4)
		new_graph.LSE = round(g.LSE,4)
		new_graph.LIE = round(g.LIE,4)
		new_graph.rule1m = g.rule1HM
		new_graph.rule2m = g.rule2HM
		new_graph.rule3m = g.rule3HM
		new_graph.rule4m = g.rule4HM
		new_graph.rule1s = g.rule1HS
		new_graph.rule2s = g.rule1HS
		new_graph.rule3s = g.rule1HS
		new_graph.rule4s = g.rule1HS
		new_graph.save()
		
		
		longGraphics = longgraphic.objects.order_by('tipo')
		context = {'graphics':longGraphics}
	except:
		context = {}

	return render(request, 'base/long.html', context)

@user_passes_test(staff_check)
def recalculate(request):
	try:
		context = {	'LCt':globalvar.objects.get(name="LCt").value,
				'LSCt':globalvar.objects.get(name="LSCt").value,
				'LICt':globalvar.objects.get(name="LICt").value,
				'LCst':globalvar.objects.get(name="LCst").value,
				'LSCst':globalvar.objects.get(name="LSCst").value,
				'LICst':globalvar.objects.get(name="LICst").value,
				'LSEt':globalvar.objects.get(name="LSEt").value,
				'LIEt':globalvar.objects.get(name="LIEt").value,
				'LCh':globalvar.objects.get(name="LCh").value,
				'LSCh':globalvar.objects.get(name="LSCh").value,
				'LICh':globalvar.objects.get(name="LICh").value,
				'LCsh':globalvar.objects.get(name="LCsh").value,
				'LSCsh':globalvar.objects.get(name="LSCsh").value,
				'LICsh':globalvar.objects.get(name="LICsh").value,
				'LSEh':globalvar.objects.get(name="LSEh").value,
				'LIEh':globalvar.objects.get(name="LIEh").value
		}
	except:
		context = {}
	
	if(request.method == 'POST'):
		print(request.POST)
		date1 = str(dateutil.parser.parse(request.POST.__getitem__('date1')))+".000000"
		date2 = str(dateutil.parser.parse(request.POST.__getitem__('date2')))+".000000"
		if(request.POST.__getitem__('tipo')=='temperature'):
			a = temperature.objects.filter(date__range=[date1,date2])
		else:
			a = humidity.objects.filter(date__range=[date1,date2])
		if(len(a)==0):
			context['menssage'] = 'No samples found in between the specified dates'
			return render(request, 'base/recalculate.html', context)
		print(date1)
		print(date2)
		print(a)
		b = [tes(float(a[i].media),float(a[i].sigma),a[i].date) for i in range(len(a))]
		b.sort(key=lambda nn: nn.x)
		st = [b[i].st for i in range(len(b))]
		x = [b[i].x for i in range(len(b))]
		b = [b[i].b for i in range(len(b))]
		if(request.POST.__getitem__('tipo')=='temperature'):
			g = graph.Graph(b,st,x,"a", float(globalvar.objects.get(name="LCt").value),float(globalvar.objects.get(name="LSCt").value),float(globalvar.objects.get(name="LICt").value),float(globalvar.objects.get(name="LSEt").value),float(globalvar.objects.get(name="LIEt").value),float(globalvar.objects.get(name="LCst").value),float(globalvar.objects.get(name="LSCst").value),float(globalvar.objects.get(name="LICst").value))
		else:
			g = graph.Graph(b,st,x,"q", float(globalvar.objects.get(name="LCh").value),float(globalvar.objects.get(name="LSCh").value),float(globalvar.objects.get(name="LICh").value),float(globalvar.objects.get(name="LSEt").value),float(globalvar.objects.get(name="LIEt").value),float(globalvar.objects.get(name="LCsh").value),float(globalvar.objects.get(name="LSCsh").value),float(globalvar.objects.get(name="LICsh").value))
		g.recalculaLCs()
		if(request.POST.__getitem__('tipo')=='temperature'):
			LC = globalvar.objects.get(name="LCt")
			LC.value = round(g.LC,4)
			LC.save()
			LSC = globalvar.objects.get(name="LSCt")
			LSC.value = round(g.LSC,4)
			LSC.save()
			LIC = globalvar.objects.get(name="LICt")
			LIC.value = round(g.LIC,4)
			LIC.save()
			LCs = globalvar.objects.get(name="LCst")
			LCs.value = round(g.LCs,4)
			LCs.save()
			LSCs = globalvar.objects.get(name="LSCst")
			LSCs.value = round(g.LSCs,4)
			LSCs.save()
			LICs = globalvar.objects.get(name="LICst")
			LICs.value = round(g.LICs,4)
			LICs.save()
		else:
			LC = globalvar.objects.get(name="LCh")
			LC.value = round(g.LC,4)
			LC.save()
			LSC = globalvar.objects.get(name="LSCh")
			LSC.value = round(g.LSC,4)
			LSC.save()
			LIC = globalvar.objects.get(name="LICh")
			LIC.value = round(g.LIC,4)
			LIC.save()
			LCs = globalvar.objects.get(name="LCsh")
			LCs.value = round(g.LCs,4)
			LCs.save()
			LSCs = globalvar.objects.get(name="LSCsh")
			LSCs.value = round(g.LSCs,4)
			LSCs.save()
			LICs = globalvar.objects.get(name="LICsh")
			LICs.value = round(g.LICs,4)
			LICs.save()
		return render(request, 'base/recalculate.html', context)
	return render(request, 'base/recalculate.html', context)

@login_required
def new_graph(request):
	if(request.method == 'POST'):
		# ~ form = graphicForm(request.POST)
		# ~ if(form.is_valid()):
		print(request.POST)
		date1 = str(dateutil.parser.parse(request.POST.__getitem__('date1')))+".000000"
		date2 = str(dateutil.parser.parse(request.POST.__getitem__('date2')))+".000000"
		new_graph = graphic()
		# ~ new_graph = form.save(commit=False)
		# ~ date1 = new_graph.year+"-"+new_graph.month+"-"+new_graph.day+" "+new_graph.hour+":"+new_graph.minu+":00.000000"
		# ~ date2 = new_graph.year1+"-"+new_graph.month1+"-"+new_graph.day1+" "+new_graph.hour1+":"+new_graph.minu1+":00.000000"
		if(request.POST.__getitem__('tipo')=='temperature'):
			a = temperature.objects.filter(date__range=[date1,date2])
		else:
			a = humidity.objects.filter(date__range=[date1,date2])
		if(len(a)==0):
			context={'menssage':'No samples found in between the specified dates'}
			return render(request, 'base/new_graph.html', context)
		# ~ a = humidity.objects.filter(date__range=[str(dateutil.parser.parse(date1)),str(dateutil.parser.parse(date2))])
		print(date1)
		print(date2)
		print(a)
		b = [tes(float(a[i].media),float(a[i].sigma),a[i].date) for i in range(len(a))]
		b.sort(key=lambda nn: nn.x)
		st = [b[i].st for i in range(len(b))]
		x = [b[i].x for i in range(len(b))]
		b = [b[i].b for i in range(len(b))]
		new_graph.date1 = date1
		new_graph.date2 = date2
		new_graph.save()
		
		if(request.POST.__getitem__('tipo')=='temperature'):
			g = graph.Graph(b,st,x,new_graph.id, float(globalvar.objects.get(name="LCt").value),float(globalvar.objects.get(name="LSCt").value),float(globalvar.objects.get(name="LICt").value),float(globalvar.objects.get(name="LSEt").value),float(globalvar.objects.get(name="LIEt").value),float(globalvar.objects.get(name="LCst").value),float(globalvar.objects.get(name="LSCst").value),float(globalvar.objects.get(name="LICst").value))
		else:
                    g = graph.Graph(b,st,x,new_graph.id, float(globalvar.objects.get(name="LCh").value),float(globalvar.objects.get(name="LSCh").value),float(globalvar.objects.get(name="LICh").value),float(globalvar.objects.get(name="LSEh").value),float(globalvar.objects.get(name="LIEh").value),float(globalvar.objects.get(name="LCsh").value),float(globalvar.objects.get(name="LSCsh").value),float(globalvar.objects.get(name="LICsh").value))
		g.geraGrafico()
		if(request.POST.__getitem__('tipo')=='temperature'):
			new_graph.tipo = True
		new_graph.img='graphs/'+str(new_graph.id)+'.png'
		new_graph.cp = g.CP
		new_graph.cpk = g.CPK
		new_graph.dpm = g.DPM
		new_graph.LC = round(g.LC,4)
		new_graph.LSC = round(g.LSC,4)
		new_graph.LIC = round(g.LIC,4)
		new_graph.LCs = round(g.LCs,4)
		new_graph.LSCs = round(g.LSCs,4)
		new_graph.LICs = round(g.LICs,4)
		new_graph.LSE = round(g.LSE,4)
		new_graph.LIE = round(g.LIE,4)
		new_graph.rule1m = g.rule1HM
		new_graph.rule2m = g.rule2HM
		new_graph.rule3m = g.rule3HM
		new_graph.rule4m = g.rule4HM
		new_graph.rule1s = g.rule1HS
		new_graph.rule2s = g.rule1HS
		new_graph.rule3s = g.rule1HS
		new_graph.rule4s = g.rule1HS
		new_graph.save()
		return HttpResponseRedirect(reverse('base:graphs'))
	return render(request, 'base/new_graph.html')

@login_required
def graphs(request):
	graphics = graphic.objects.order_by('-date_added')
	context = {'graphics':graphics}
	return render(request, 'base/graphs.html', context)


@csrf_exempt
def entrytemperature(request):
	if(request.method == 'POST'):
		a = temperature()
		a.x0=request.POST.__getitem__('x0')
		a.x1=request.POST.__getitem__('x1')
		a.x2=request.POST.__getitem__('x2')
		a.x3=request.POST.__getitem__('x3')
		a.x4=request.POST.__getitem__('x4')
		a.x5=request.POST.__getitem__('x5')
		a.x6=request.POST.__getitem__('x6')
		a.x7=request.POST.__getitem__('x7')
		a.x8=request.POST.__getitem__('x8')
		a.x9=request.POST.__getitem__('x9')
		a.x10=request.POST.__getitem__('x10')
		a.x11=request.POST.__getitem__('x11')
		a.x12=request.POST.__getitem__('x12')
		a.x13=request.POST.__getitem__('x13')
		a.x14=request.POST.__getitem__('x14')
		a.x15=request.POST.__getitem__('x15')
		a.x16=request.POST.__getitem__('x16')
		a.x17=request.POST.__getitem__('x17')
		a.x18=request.POST.__getitem__('x18')
		a.x19=request.POST.__getitem__('x19')
		a.x20=request.POST.__getitem__('x20')
		a.x21=request.POST.__getitem__('x21')
		a.x22=request.POST.__getitem__('x22')
		a.x23=request.POST.__getitem__('x23')
		a.x24=request.POST.__getitem__('x24')
		n = [a.x0,a.x1,a.x2,a.x3,a.x4,a.x5,a.x6,a.x7,a.x8,a.x9,a.x10,a.x11,a.x12,a.x13,a.x14,a.x15,a.x16,a.x17,a.x18,a.x19,a.x20,a.x21,a.x22,a.x23,a.x24]
		ar = []
		for nn in n:
			ar.append(float(nn));
		a.media = str(np.mean(ar))
		a.sigma = str(np.std(ar))
		a.save()
		return HttpResponse(status=200);
	else:
		return HttpResponse(status=403);

@csrf_exempt
def entryhumidity(request):
	if(request.method == 'POST'):
		a = humidity()
		a.x0=request.POST.__getitem__('x0')
		a.x1=request.POST.__getitem__('x1')
		a.x2=request.POST.__getitem__('x2')
		a.x3=request.POST.__getitem__('x3')
		a.x4=request.POST.__getitem__('x4')
		a.x5=request.POST.__getitem__('x5')
		a.x6=request.POST.__getitem__('x6')
		a.x7=request.POST.__getitem__('x7')
		a.x8=request.POST.__getitem__('x8')
		a.x9=request.POST.__getitem__('x9')
		a.x10=request.POST.__getitem__('x10')
		a.x11=request.POST.__getitem__('x11')
		a.x12=request.POST.__getitem__('x12')
		a.x13=request.POST.__getitem__('x13')
		a.x14=request.POST.__getitem__('x14')
		a.x15=request.POST.__getitem__('x15')
		a.x16=request.POST.__getitem__('x16')
		a.x17=request.POST.__getitem__('x17')
		a.x18=request.POST.__getitem__('x18')
		a.x19=request.POST.__getitem__('x19')
		a.x20=request.POST.__getitem__('x20')
		a.x21=request.POST.__getitem__('x21')
		a.x22=request.POST.__getitem__('x22')
		a.x23=request.POST.__getitem__('x23')
		a.x24=request.POST.__getitem__('x24')
		n = [a.x0,a.x1,a.x2,a.x3,a.x4,a.x5,a.x6,a.x7,a.x8,a.x9,a.x10,a.x11,a.x12,a.x13,a.x14,a.x15,a.x16,a.x17,a.x18,a.x19,a.x20,a.x21,a.x22,a.x23,a.x24]
		ar = []
		for nn in n:
			ar.append(float(nn));
		a.media = str(np.mean(ar))
		a.sigma = str(np.std(ar))
		a.save()
		return HttpResponse(status=200);
	else:
		return HttpResponseNotFound(status=403);
