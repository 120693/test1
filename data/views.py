from django.shortcuts import render
from django.views import generic
from .models import Data
# Create your views here.

class DataListView(generic.ListView):
    model = Data