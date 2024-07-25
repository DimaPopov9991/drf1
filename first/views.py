from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from first.models import Carmodel


# Create your views here.
class CarsView(APIView):
    def get(self, *args, **kwargs):
        cars=Carmodel.objects.all()
        res=[model_to_dict(car) for car in cars]


        return HttpResponse(res)

    def post(self, *args, **kwargs):
        data=self.request.data
        car=Carmodel.objects.create(**data)
        car_dict=model_to_dict(car)
        return HttpResponse(car_dict)


class CarRetriveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk=kwargs['pk']
        car=Carmodel.objects.get(pk=pk)

        return HttpResponse(model_to_dict(car))
    def put(self, *args, **kwargs):
        pk=kwargs['pk']
        print(pk)
        data=self.request.data
        try:
            car=Carmodel.objects.get(pk=pk)
        except Carmodel.DoesNotExist:
            return Response('Not Found')
        car.brand=data['brand']
        car.price=data['price']
        car.year=data['year']
        car.save()
        return HttpResponse(model_to_dict(car))
