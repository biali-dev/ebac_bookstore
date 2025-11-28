from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bem-vindo à Bookstore!</h1><p>API está funcionando!</p>")