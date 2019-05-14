from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('(?P<id>)', views.detail, name='detail'),
	path('search/', views.search, name='search')
]