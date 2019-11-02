from django import forms
from .models import graphic

class graphicForm(forms.ModelForm):
	class Meta:
		model = graphic
		fields = ['year','month','day','hour','minu','year1','month1','day1','hour1','minu1']
		labels = {'year':'Ano Inicial', 'month':'Mês Inicial','day':'Dia Inicial','hour':'Hora Inicial','minu':'Minuto Inicial','year1':'Ano Final', 'month1':'Mês Final','day1':'Dia Final','hour1':'Hora Final','minu1':'Minuto Final'}
