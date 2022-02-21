import imp
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from django.views.generic import View
# Create your views here.

class crudview(View):
    def get(self, request):
        name1=request.GET.get('name',None)
        obj=crud.objects.create(name=name1)
        data={
            'id':obj.id,
            'name':obj.name,
        }
        return JsonResponse(data)

def home(request):
    return render(request,'index.html')


class createage(View):

    def  get(self, request):

     

        age1 = request.GET.get('age', None)



        obj = Addage.objects.create(

           

            age = age1

        )



        user = {'id':obj.id,'age':obj.age}
        
        status = "Dear {} Your Goals and Inspiration is updated"



        data = {

            'user': user,
            'status':status

        }

        return JsonResponse(data)



def sagufta(request):
    return render (request, 'testajax.html')

