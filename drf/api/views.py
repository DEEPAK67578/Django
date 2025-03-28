from django.shortcuts import render
from django.http import JsonResponse
import json

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Dummy
from rest_framework import generics
from .serializer import DummySerializer
from django.shortcuts import get_object_or_404
from rest_framework import mixins,permissions,authentication
# Create your views here.


# Normal Django API View
def api_home(request):
    body = request.body
    jsondata = {}
    try:
        jsondata = json.loads(body)  # Some data needs to be parsed like this
    except:
        pass
    data = {"name": "Deepak", "age": 21}
    print(jsondata)
    return JsonResponse(data)

#docorator view
@api_view(["GET", "POST"])
def descoratorAPIVIEW(request): #Too much work,so using serializer
    if request.method == "GET":
        modelInstance = Dummy.objects.all()
        return Response(modelInstance.values(), status=200)
    else:
        data = request.data
        if "title" in data and "price" in data:
            obj = Dummy(
                title=data.get("title"),
                content=data.get("content"),
                price=data.get("price"),
            )
            obj.save()
            return Response({"message": "Created Successully"}, status=204)
        else:
            return Response({"Error"})

@api_view(["GET", "POST","PUT","PATCH","DELETE"])
def decoratorAPIViewV2(request):
      if request.method == "GET":
        modelInstance = Dummy.objects.all()
        data = DummySerializer(modelInstance,many=True)
        return Response(data.data, status=200)
      elif request.method == "POST":
        data = request.data
        seraializedData = DummySerializer(data=data)
        if(seraializedData.is_valid()):
            seraializedData.save()
            return Response({"message":"Data Created Successfully"})
        return Response(seraializedData.errors)
      elif request.method == "PUT":
           data = request.data
           if(data.get("id") is not None):
                instance = get_object_or_404(Dummy.objects.all(),pk=request.data.get("id"))
                seraializedData = DummySerializer(instance,data=data)
                print(seraializedData)
                if(seraializedData.is_valid()):
                    seraializedData.save()
                    return Response(seraializedData.data,200)
                return Response(seraializedData.errors)
           else:
                return Response({"message":"Provide the id to update the data"},400)
      elif request.method == "PATCH":
           data = request.data
           if(data.get("id") is not None):
                instance = get_object_or_404(Dummy.objects.all(),pk=request.data.get("id"))
                seraializedData = DummySerializer(instance,data=data,partial=True)
                if(seraializedData.is_valid()):
                    seraializedData.save()
                    return Response(seraializedData.data,200)
                return Response(seraializedData.errors)
           else:
                return Response({"message":"Provide the id to update the data"},400)
      else:
           pk = request.data.get("id")
           if pk is not None:
               obj = get_object_or_404(Dummy.objects.all(),pk=pk)
               obj.delete()
               return Response({"message":"Deleted the Data"},200)
           else:
               return Response({"Provide the ID to Delete"})

#Generic Views
class DummyCreateGenericVIew(generics.CreateAPIView):
    serializer_class = DummySerializer
    queryset = Dummy.objects.all()
    lookup_field = "pk"


    def perform_create(self, serializer):
        content = serializer.validated_data.get("content")
        if content is None:
            content = serializer.validated_data.get("title")
        serializer.save(content = content)

class DummyRetrieveGenericView(generics.RetrieveAPIView):
    serializer_class = DummySerializer
    queryset = Dummy.objects.all()
    lookup_field = "pk"

class DummyListGenericView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]
    serializer_class = DummySerializer
    queryset = Dummy.objects.all()
    lookup_field = "pk"

class DummyUpdateGenericView(generics.UpdateAPIView):
    serializer_class = DummySerializer
    queryset = Dummy.objects.all()
    lookup_field = "pk"

class DummyDeleteGenericView(generics.DestroyAPIView):
    serializer_class = DummySerializer
    queryset = Dummy.objects.all()
    lookup_field = "pk"

class CustomGenericView(generics.GenericAPIView,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    serializer_class = DummySerializer
    queryset = Dummy.objects.all()
    lookup_field = "pk"

    def get(self,request,*args,**kwargs):
       if(kwargs.get("pk")):
           return self.retrieve(request,*args,**kwargs)
       else:
          return self.list(request,*args,**kwargs)