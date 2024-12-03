from django.shortcuts import render
from . models import Agriculture
import joblib


def home(request):
    last_agriculture_data = Agriculture.objects.order_by('-id').first()
    return render(request, 'home.html', {'last_agriculture_data':last_agriculture_data})


def predect(request):
    return render(request, 'predect.html')


def result(request):
    cls = joblib.load('crop_app.pkl')

    lis = []

    lis.append(request.GET['N'])
    lis.append(request.GET['P'])
    lis.append(request.GET['K'])
    lis.append(request.GET['temp'])
    lis.append(request.GET['humid'])
    lis.append(request.GET['ph'])
    lis.append(request.GET['rainfall'])

    out = cls.predict([lis])

    return render(request, 'result.html', {'ans': out})