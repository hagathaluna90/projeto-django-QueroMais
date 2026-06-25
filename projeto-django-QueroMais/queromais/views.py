# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, "inicio.html")

def login(request):
    return render(request, "login.html")

def catalogo(request):
    return render(request, "catalogo.html")

def catalogo(request):

    doces = [
        {
            "id": 1,
            "nome": "Brigadeiros",
            "descricao": "Deliciosos brigadeiros, com uma mistura suculenta dos melhores ingredientes.",
            "preco": "02,50",
            "imagem": "img/brigadeiro.png"
        },
        {
            "id": 2,
            "nome": "Bolo de pote",
            "descricao": "Camadas generosas de massa fofinha e recheio cremoso.",
            "preco": "05,00",
            "imagem": "img/bolo-pote.png"
        },
        {
            "id": 3,
            "nome": "Cocada de doce de leite",
            "descricao": "A combinação perfeita entre coco fresco e a cremosidade do doce de leite.",
            "preco": "03,50",
            "imagem": "img/cocada.png"
        }
    ]

    salgados = [
        {
            "id": 1,
            "nome": "Pippo's de churrasco",
            "descricao": "Tradicional milho de sabor crocante, assado e com tempero de churrasco.",
            "preco": "04,50",
            "imagem": "img/pippo.png"
        },
        {
            "id": 2,
            "nome": "Ki queijo",
            "descricao": "O salgadinho Ki queijinho entrega a crocância perfeita com um sabor marcante de queijo.",
            "preco": "02,00",
            "imagem": "img/ki-queijo.png"
        },
        {
            "id": 3,
            "nome": "Torcida Pimenta",
            "descricao": "Sabor intenso, notas salgadas com a picância da pimenta vermelha.",
            "preco": "02,00",
            "imagem": "img/torcida.png"
        }
    ]

    gelados = [
        {
            "id": 1,
            "nome": "Sorvete de chocolate",
            "descricao": "Cremoso e feito com cacau selecionado.",
            "preco": "04,50",
            "imagem": "img/sorvete-chocolate.png"
        },
        {
            "id": 2,
            "nome": "Açaí 500ml",
            "descricao": "Açaí puro e refrescante, ideal para qualquer hora do dia.",
            "preco": "16,90",
            "imagem": "img/acai-500.png"
        },
        {
            "id": 3,
            "nome": "Sorvete de morango",
            "descricao": "Sorvete de baunilha com calda de morango e cobertura especial.",
            "preco": "04,50",
            "imagem": "img/sorvete-morango.png"
        }
    ]

    variados = [
        {
            "id": 1,
            "nome": "Cherry Pop",
            "descricao": "Este pirulito tradicional combina o delicioso sabor de cereja.",
            "preco": "00,50",
            "imagem": "img/cherry-pop.png"
        },
        {
            "id": 2,
            "nome": "Paçoca",
            "descricao": "Doce tradicional brasileiro feito à base de amendoim torrado, açúcar e sal.",
            "preco": "00,50",
            "imagem": "img/pacoca.png"
        },
        {
            "id": 3,
            "nome": "Chiclet poosh!",
            "descricao": "Massa pela sua casquinha crocante e pelo seu recheio líquido que traz uma explosão de sabor.",
            "preco": "00,50",
            "imagem": "img/chiclet-poosh.png"
        }
    ]

    context = {
        "doces": doces,
        "salgados": salgados,
        "gelados": gelados,
        "variados": variados,
    }

    return render(request, "catalogo.html", context)