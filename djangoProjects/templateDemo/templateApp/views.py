from django.shortcuts import render

# Create your views here.
def renderTemplate(request):
    myDict={"name":"Raghav"}
    return render(request, 'templateApp/firstTemplate.html', context=myDict)
