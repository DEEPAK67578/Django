from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import Http404,HttpResponseNotFound,HttpResponseRedirect
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
        return render(request, "challenges/challenge.html",{
            "description": monthData,
            "title": month.capitalize()
        })
        # renderData = render_to_string("challenges/challenge.html")
        # return HttpResponse(renderData)
    except:
        return HttpResponseNotFound("No Existing Month")
    
def resToMonthNum(request, month):
    months = list(months_dict.keys())
    print(months)
    try:
        redirectMonth = months[month-1]
        redirectPath = reverse("month-challenge",args=[redirectMonth]) #/challenge/<month>
        # redirectPath = "/month/" + redirectMonth
        return HttpResponseRedirect(redirectPath)
    except:
        # html = render_to_string("404.html")
        # return HttpResponseNotFound(html)
        return Http404()
    

def index(request):
    months = list(months_dict.keys())
    return render(request,"challenges/index.html",{
        "months":months
    })