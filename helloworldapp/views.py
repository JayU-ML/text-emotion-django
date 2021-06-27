# from .models import Post
from django.views import generic
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
import logging
import requests
import sys
import io
from django.shortcuts import render
from django.http.response import HttpResponse
from braces.views import JSONResponseMixin
from django.http import JsonResponse
from django.conf import settings

# 日本語を受信時にエラーにならないようにする為に必要。
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# def helloworldfunction(request):
#     return render(request, 'index.html')


def get(request):
    if request.method == "POST":

        text = request.POST.get('text', None)

        # key = 'AIzaSyCAXFvYgTVg6ivXm6xrT2It3VjzgOFF6no' # TEXTEMOTION_KEY
        # url = f'https://language.googleapis.com/v1/documents:analyzeSentiment?key={key}' # TEXTEMOTION_URL
        
        # key = settings.TEXTEMOTION_KEY
        # url = settings.TEXTEMOTION_URL
        
        url = settings.TEXTEMOTION_URL
        
        header = {'Content-Type': 'application/json'}

        body = {
            "document": {
                "type": "PLAIN_TEXT",
                "language": "JA",
                "content": text
            }
        }

        res = requests.post(url, headers=header, json=body)
        result = res.json()

        myapp_data = {
            'emotion': result['documentSentiment']['magnitude'],
            'emotion_json': result,
            'text': text,
        }

        return JsonResponse(myapp_data, safe=False)


def helloworldfunction(request):

    text = 'ありがとうございます！'
    key = 'AIzaSyCAXFvYgTVg6ivXm6xrT2It3VjzgOFF6no'
    url = f'https://language.googleapis.com/v1/documents:analyzeSentiment?key={key}'
    header = {'Content-Type': 'application/json'}

    body = {
        "document": {
            "type": "PLAIN_TEXT",
            "language": "JA",
            "content": text
        }
    }

    res = requests.post(url, headers=header, json=body)
    result = res.json()

    myapp_data = {
        'data_explain': result,

    }
    return render(request, 'index.html', myapp_data)
