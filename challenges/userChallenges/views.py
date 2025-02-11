from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
# Create your views here.

months_dict = {
    'january': 'First month',
    'february': 'Second month',
    'march': 'Third month',
    'april': 'Fourth month',
    'may': 'Fifth month',
    'june': 'Sixth month',
    'july': 'Seventh month',
    'august': 'Eighth month',
    'september': 'Ninth month',
    'october': 'Tenth month',
    'november': 'Eleventh month',
    'december': 'Twelfth month'
    }

def resToMonth(request,month):
    try:
        monthData = months_dict[month]
        return HttpResponse(monthData)
    except:
        return HttpResponseNotFound("No Existing Month")
    
def resToMonthNum(request, month):
    months = list(months_dict.keys())
    print(months)
    try:
        redirectMonth = months[month-1]
        redirectPath = reverse("month-challege",args=[redirectMonth]) #/challenge/<month>
        # redirectPath = "/month/" + redirectMonth
        return HttpResponseRedirect(redirectPath)
    except:
        return HttpResponseNotFound("No Existing Month")
    

def index(request):
    months = list(months_dict.keys())
    startText = "<ul>"
    for month in months:
        redirectPath = reverse("month-challege",args=[month]) #/challenge/<month>
        text = f'<li><a href="{redirectPath}">{month}</a></li>'
        startText+=text
    startText+="</ul>"
    return HttpResponse(startText)