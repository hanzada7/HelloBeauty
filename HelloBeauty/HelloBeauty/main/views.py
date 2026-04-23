from django.http import HttpResponse

def home(request):
    return HttpResponse("Привет! Это мой сайт для продажи косметики. Здесь вы найдете лучшие продукты для ухода за кожей и макияжа. Добро пожаловать в мир красоты!")