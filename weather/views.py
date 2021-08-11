from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
    else :
        city = ''

    return render(request, 'index.html', {'city': city})
