from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'base'

urlpatterns = [
	#pagina inicial
	path('', views.index, name='index'),
	path('new_graph/', views.new_graph, name='new_graph'),
	path('graphs/', views.graphs, name='graphs'),
]
