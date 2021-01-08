from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from .models import Song
from .serializers import SongSerializer
from rest_framework.response import Response
import joblib
import pandas as pd
from collections import Counter
import os
# Create your views here.

def predict_int(intervalle):
    switcher = {
        1: "1922 1983",
        2: "1983 1992",
        3: "1992 1996",
        4: "1996 1999",
        5: "1999 2002",
        6: "2002 2004",
        7: "2004 2005",
        8: "2005 2007",
        9: "2007 2008",
        10: "2008 2011"
    }
    date = switcher.get(intervalle).split(" ")
    return date[0],date[1]




@api_view(['GET','POST'])
def song_list(request):
    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SongSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
# Create your views here.

@api_view(['GET','PUT','DELETE'])
def song_detail(request, pk):
    try:
        song = Song.objects.get(pk=pk)
    except Song.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = SongSerializer(song)
        return Response(serializer.data)
    elif request.method == 'PUT':

        mdl2 = joblib.load(".\\prediction\\rf1.sav")
        data = JSONParser().parse(request)
        data_pd = pd.DataFrame([data])
        data_pred = mdl2.predict(data_pd.drop(["YEAR_MIN", "YEAR_MAX"], axis=1))

        YEAR_MIN, YEAR_MAX = predict_int(data_pred[0])
        data_pd["YEAR_MAX"] = float(YEAR_MAX)
        data_pd["YEAR_MIN"] = float(YEAR_MIN)

        data = data_pd.to_dict('records')

        serializer = SongSerializer(song, data=data[0])
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        song.delete()
        return HttpResponse(status=204)

@api_view(['POST'])
def predict(request):
    mdl2 = joblib.load(".\\prediction\\rf1.sav")

    data = JSONParser().parse(request)

    data_pd = pd.DataFrame([data])
    data_pred = mdl2.predict(data_pd.drop(["YEAR_MIN", "YEAR_MAX"], axis=1))

    YEAR_MIN,YEAR_MAX = predict_int(data_pred[0])
    data_pd["YEAR_MAX"] = float(YEAR_MAX)
    data_pd["YEAR_MIN"] = float(YEAR_MIN)

    data=data_pd.to_dict('records')

    serializer = SongSerializer(data=data[0])
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

