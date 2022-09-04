from distutils.log import error
import re
from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse
from django.http import Http404,HttpResponseNotFound,HttpResponseRedirect
from django.template.loader import render_to_string
# Create your views here.
months = {
    "January" : "DO prepare for gate exams",
    "February" : None,
    "March" : " Get Domain for a Website and make it fully functional",
    "April" : "Get Domain for a Website and make it functional  and     functional",
    "May" : "Get Domain for a Website and make it functional and functional",   
    "June" : "Get Domain for a Website and make it functional and functional and do love",
    "July" : "Do Freelancing functional and functional and do love",
    "August" : "Be Gate qualified ",
    "September" : "Got placed for a good paying internship",
    "October" : "help Your Home ",
    "November" : "become CEO of a Startup",
    "December" : None,
    
}
def index(request):
    # list_of_months = "";
    # months_ki_list = list(months.keys())
    # for month in month:
       
    #     monthc = month.capitalize()
    #     path_of_redirection = reverse("monthly-challenge",args=[monthc])
    #     # list_of_months+=f"<a href='{path_of_redirection}'> <h1>{month}</h1></a>"
    # html_string = render_to_string("challenges/challenges.html")
    # return HttpResponse(html_string)
    list_of_months = list(months.keys())
    return render(request, 'challenges/index.html' , {
        "months_list": list_of_months
    })
    # return render(request, 'challenges/challenges.html')
def challenges_by_number(request,month):
    target_month = list(months.keys())
    if(month>12):
        return HttpResponseNotFound("Error Page Not Found")
    else:
        redirect_url = reverse("monthly-challenge", args=[target_month[month-1]]) # here we are constructing urls by using name {monthly-challenge} and args are totally optional and we are using args because our url has dynamic parameters {january,february ,etc ..}
        return HttpResponseRedirect(redirect_url)
    
def monthly_challenge(request,month):
    try:
        task = months[month]
        return render(request ,"challenges/challenges.html",{
            "title_month" : month ,
            "task" : task
        })
        # return HttpResponse(f"<h1>{months[month]}</h1>")
    except :
        raise Http404()

   
    
        
    

