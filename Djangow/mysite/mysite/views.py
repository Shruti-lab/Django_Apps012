#made by user
from django.http import HttpResponse
from django.shortcuts import render

def index(requests):
    params={'name':'shruti','place':'japan'}
    return render(requests,'index.html',params)

def analyze(requests):
    #get the text
    txt = requests.GET.get('text','default')

    #check box values
    removepunc = requests.GET.get('removepunc','off')
    caps = requests.GET.get('fullcaps','off')
    #analyze the text
    if removepunc =="on":
        analyzed=""
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in txt:
            if char not in punctuations:
                analyzed=analyzed+char
        params = {'purpose':'Remove punctuations','analyzed_text':analyzed}
        return render(requests,'analyze.html',params)
    elif caps=='on':
        analyzed=""
        for char in txt:
            analyzed=analyzed+char.upper()
        params = {'purpose':'Converted to upper case','analyzed_text':analyzed}
        return render(requests,'analyze.html',params)
    else:
        return HttpResponse("Error")


def about(requests):
    return HttpResponse("<h1>about the website</h1>")


def capitalizefirst(requests):
    return HttpResponse("Capitalize first")

def removepunc(requests):
    return HttpResponse("Remove punctuation")


def newlineremove(requests):
    return HttpResponse("new line <a href='/'>back button</a>")
def charcount(requests):
    return HttpResponse("Remove punctuation")

