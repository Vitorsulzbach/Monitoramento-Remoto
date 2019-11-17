from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .forms import graphicForm, graphicForm2
from .models import graphic, humidity, temperature
import graphgenerator
import datetime
import tes
from django.views.decorators.csrf import csrf_exempt
from django.db import models
import numpy as np
from django.utils.dateparse import parse_datetime
import pytz
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseNotFound

#ex time:'2019-06-15 22:52:34.810649'

def index(request):
	return render(request, 'base/index.html')

@login_required
def new_graph(request):
	if(request.method == 'POST'):
		form = graphicForm(request.POST)
		if(form.is_valid()):
			new_graph = form.save(commit=False)
			date1 = new_graph.year+"-"+new_graph.month+"-"+new_graph.day+" "+new_graph.hour+":"+new_graph.minu+":00.000000"
			date2 = new_graph.year1+"-"+new_graph.month1+"-"+new_graph.day1+" "+new_graph.hour1+":"+new_graph.minu1+":00.000000"
			a = amostra.objects.filter(date__range=[date1,date2])
			n=len(a)
			b = [tes.tes(float(a[i].media),float(a[i].sigma),a[i].date) for i in range(n)]
			b.sort(key=lambda nn: nn.x)
			st = [b[i].st for i in range(len(b))]
			x = [b[i].x for i in range(len(b))]
			b = [b[i].b for i in range(len(b))]
			new_graph.save()
			graphgenerator.gerargra(b,st,x,new_graph.id)
			new_graph.img='graphs/'+str(new_graph.id)+'.png'
			new_graph.save()
			return HttpResponseRedirect(reverse('base:graphs'))
	else:
        	form = graphicForm()
	context= {'form': form}
	return render(request, 'base/new_graph.html',context)

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
