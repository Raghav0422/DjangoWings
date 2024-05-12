from django.shortcuts import render

# Create your views here.
def renderTemplate(request):
    myDict={"name":"Raghav"}
    return render(request, 'templateApp/firstTemplate.html', context=myDict)

def employeeInfo(request):
    myDict={"name":"Raghav","id":2025933,"sal":27000}
    return render(request,'templateApp/employeeTemplate.html',myDict)
