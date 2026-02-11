from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

"""
def january(request):
    return HttpResponse("Complete the project!")

def febuary(request):
    return HttpResponse("Walk for 20 minutes daily!")

"""


"""
def monthly_challenges_by_number(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month):
    text = ""
    if month == "january":
        text = "Complete the project!"
    elif month == "febuary":
        text = "Walk for 20 minutes daily!"
    elif month == "march":
        text = "Go to gym 5 days a week!"
    else:
        text = HttpResponseNotFound("Given month is not supported!")
        
    return HttpResponse(text)
"""


challenge = {
    "january": "Complete the project!",
    "febuary": "Walk for 20 minutes daily!",
    "march": "Go to the gym 5 days a week!",
    "april": "Read 10 pages every day!",
    "may": "Practice coding for 1 hour daily!",
    "june": "Wake up early and follow a routine!",
    "july": "Learn a new technical skill!",
    "august": "Build a mini project!",
    "september": "Revise core CS subjects!",
    "october": "Improve problem-solving skills!",
    "november": "Work on interview preparation!",
    "december": "Reflect and plan goals for next year!"
}



def index_month(request):
    list_items = ""
    months = list(challenge.keys())
    for month in months:
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{month.capitalize()}</a></li>"

        response_data = f"""<ul>{list_items}</ul>"""
    return HttpResponse(response_data)


def monthly_challenges_by_number(request, month):
    months = list(challenge.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid Month!</h1>")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])  # will automatically change to the url if changed  in url of urls in main app
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        text = challenge[month]
        response_data = f"<h1>{text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>Invalid Month!</h1>")


