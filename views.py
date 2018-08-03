# coding=utf-8
from django.shortcuts import render_to_response
from TestModel.models import Test
import hashlib


def hello(request):
    return render_to_response("index.html")


def testdb(request):
    test1 = Test(name='何伟',
                 password=hashlib.md5('123').hexdigest(),
                 type=True)
    test1.save()
    return render_to_response('index.html')


def getALl(request):
    data = Test.objects.all()
    return render_to_response('manager.html', locals())