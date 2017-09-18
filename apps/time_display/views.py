from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime

# the index function is called when root is visited
def index(request):
    context = {
    "time":strftime("%Y-%m-%d %H:%M %p", gmtime())

    }
    print context
    return render(request,'time_display/index.html', context)

# def new(request):
#     response = "hello new page"
#     return HttpResponse(response)
#
# def create(request):
#     # response = "create"
#     return redirect('/')
# #
# def show(request, number):
#     response = 'blog display' + number +  '-number'
#     return HttpResponse(response)
# #
# def edit(request, number):
#     response = number
#     return HttpResponse(response)
#
# def destroy(request, number):
#     response = number + ' destroyed'
#     return HttpResponse(response)
