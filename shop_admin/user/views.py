from django.shortcuts import render

# Create your views here.

def user_index(request):
    if request.method == 'GET':
        return render(request,'User/index.html')