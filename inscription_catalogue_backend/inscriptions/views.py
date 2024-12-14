from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from .serializers import InscriptionSerializer,InscriptionPhotoSerializer,WritingScriptSerializer,MediumSerializer
from .models import Inscription,InscriptionPhoto,WritingScript,Medium
from rest_framework import viewsets

"""class InscriptionVewSet(viewsets.ModelViewSet):
    queryset = Inscription.objects.all()
    serializer_class = InscriptionSerializer"""

@csrf_exempt
def get_inscriptions(request):
    if request.method == 'GET':
        inscriptions = Inscription.objects.all()
        serializer = InscriptionSerializer(inscriptions,many=True,context={'request': request})
        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def get_inscription(request,pk):
    if request.method == 'GET':
        return _get_one_by_pk(Inscription,InscriptionSerializer,request,pk)
        
@csrf_exempt
def get_mediums(request):
    if request.method == 'GET':
        mediums = Medium.objects.all()
        serializer = MediumSerializer(mediums,many=True,context={'request':request})
        return JsonResponse(serializer.data,safe=False)
    
@csrf_exempt
def get_medium(request,pk):
    if request.method == 'GET':
        return _get_one_by_pk(Medium,MediumSerializer,request,pk)
    
@csrf_exempt
def get_writingscripts(request):
    if request.method == 'GET':
        writing_scripts = WritingScript.objects.all()
        serializer = WritingScriptSerializer(writing_scripts,many=True,context={'request':request})
        return JsonResponse(serializer.data,safe=False)
    
@csrf_exempt
def get_writingscript(request,pk):
    if request.method == 'GET':
        return _get_one_by_pk(WritingScript,WritingScriptSerializer,request,pk)

@csrf_exempt
def get_photos(request):
    if request.method == 'GET':
        return _get_all(InscriptionPhoto,InscriptionPhotoSerializer,request)
    
@csrf_exempt
def get_photo(request,pk):
    if request.method == 'GET':
        return _get_one_by_pk(InscriptionPhoto,InscriptionPhotoSerializer,request,pk)

@csrf_exempt
def get_view_photo(request,pk):
    photo = InscriptionPhoto.objects.filter(pk=pk)
    if photo:
        photo = photo[0]
    return render(request=request,template_name='index.html',context={'item':photo})

'''
AUXILIAR CODE
'''

def _get_one_by_pk(model,serializer,request,pk):
    try:
        result = model.objects.get(pk=pk)
        serializer = serializer(result,context={'request':request})
        return JsonResponse(serializer.data)
    except:
        return HttpResponse(status=404)
    
def _get_all(model,serializer,request):
    result = model.objects.all()
    s = serializer(result,many=True,context={'request':request})
    return JsonResponse(s.data,safe=False)