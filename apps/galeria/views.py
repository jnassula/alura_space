from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.forms import FotografiaForms
from django.contrib import auth, messages
from apps.galeria.models import Fotografia


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(
        publicada=True
    )
    return render(request, 'galeria/index.html', {'cards': fotografias})


def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})


def buscar(request):
    if not request.user.is_authenticated:
        return redirect('login')

    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(
        publicada=True
    )

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
    return render(request, 'galeria/index.html', {'cards': fotografias})


def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado!')
        return redirect('login')

    form = FotografiaForms()
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fotografia inserida!')
            return redirect('index')
    return render(request, 'galeria/nova_imagem.html', {'form': form})


def editar_imagem(request, foto_id: int):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)

    if request.method == 'POST':
        form = FotografiaForms(
            request.POST, request.FILES, instance=fotografia
        )
        if form.is_valid():
            print(request.POST)
            form.save()
            messages.success(request, 'Fotografia alterada com sucesso!')
            return redirect('index')

    return render(
        request,
        'galeria/editar_imagem.html',
        {'form': form, 'foto_id': foto_id},
    )


def deletar_imagem(request, foto_id: int):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Removido com sucesso')
    return redirect('index')


def filtro(request, categoria: str):
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(
        publicada=True, categoria=categoria
    )

    return render(request, 'galeria/index.html', {'cards': fotografias})
