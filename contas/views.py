from django.shortcuts import render, redirect
from .models import Transacao
from .form import TransacaoForm
import datetime

def home(request):
    data = {}
    #data['transacoes'] = ['Transação 01', 'Transação 02', 'Transação 03']
    data['transacoes'] = Transacao.descricao
    data['now'] = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now

    return render(request, 'contas/home.html', data)

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)

def nova_transacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    return render(request, 'contas/form.html', data)