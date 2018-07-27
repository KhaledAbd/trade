from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Triko_Model, Trader, color
from .forms import TradersForm


# Create your views here.

def home(request):
    triko = Triko_Model.objects.all()
    return render(request, 'Triko/show.html', {'triko': triko})


def show_details(request, id):
    cloth = get_object_or_404(Triko_Model, pk=id)
    cols = color.objects.filter(triko_model__id=id)

    return render(request, 'Triko/model_show.html', {'cloth': cloth, 'colors': cols})


def get_Model(request, id):
    cloth = get_object_or_404(Triko_Model, pk=id)
    if request.method == 'POST':
        form = TradersForm(request.POST)
        if form.is_valid():
            form_date = form.cleaned_data
            _model = Trader(model_define=cloth, telephone=form_date['telephone'],
                            email_facebook=form_date['email_facebook'], address=form_date['address'],
                            quentity=form_date['quentity'], name=form_date['name'])
            _model.save()
        return redirect('/')
    else:
        form = TradersForm(request.POST)
        return render(request, 'Triko/Trader.html', {'form': form, 'cloth': cloth})


def Like(request, id):
    cloth = get_object_or_404(Triko_Model, pk=id)
    cloth.like = cloth.like + 1
    cloth.save()
    return redirect(reverse('Triko:triko_model'))


def change_pic(request, id):
    img = get_object_or_404(color, pk=id)
    render(request, 'Triko/model_show.html', {'img': img})
