from django.shortcuts import render

# Create your views here.
def rendering_data(request):
    d={'name':'Vijay','age':26}
    return render(request,'rendering_data.html',context=d)