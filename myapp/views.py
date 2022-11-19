from django.shortcuts import HttpResponseRedirect, render  
from django.http import HttpResponse  
from myapp.functions import handle_uploaded_file  
from myapp.forms import StudentForm   
from django.core.exceptions import ObjectDoesNotExist
# from myapp.form import EmployeeForm  
# import csv
from django.core.mail import send_mail  
from django.conf import settings

def mail(request):  
    subject = "Greetings"  
    msg     = "Congratulations for your success"  
    to      = "hiraltarpara2011@gmail.com"  
    res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])  
    if(res == 1):  
        msg = "Mail Sent Successfuly"  
    else:  
        msg = "Mail could not sent"  
    return HttpResponse(msg)  

def index(request):  
    if request.method == 'POST':
        # print("hi")  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid(): 
            handle_uploaded_file(request.FILES['file'])  
            student.save()
            return render(request,"index.html",{'form':student}) 
            # return HttpResponse("File uploaded successfuly")  
    else:  
        student = StudentForm() 
        # print("hi2") 
        # print(request.method)
        return render(request,"index.html",{'form':student})  



def setsession(request):  
    request.session['sname'] = 'irfan'  
    request.session['semail'] = 'irfan.sssit@gmail.com'  
    return HttpResponse("session is set")  
def getsession(request):  
    studentname = request.session['sname']  
    studentemail = request.session['semail']  
    return HttpResponse(studentname+" "+studentemail);  



def setcookie(request):  
    response = HttpResponse("Cookie Set")  
    response.set_cookie('java-tutorial', 'javatpoint.com')  
    return response  
def getcookie(request):  
    tutorial  = request.COOKIES['java-tutorial']  
    return HttpResponse("java tutorials @: "+  tutorial);  

def getfile(request):   #make file
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    writer = csv.writer(response)  
    writer.writerow(['1001', 'John', 'Domil', 'CA'])  
    writer.writerow(['1002', 'Amit', 'Mukharji', 'LA', '"Testing"'])  
    return response 

# from myapp.models import Student import csv  
# def getfile(request):   #using database 
#     response = HttpResponse(content_type='text/csv')  
#     response['Content-Disposition'] = 'attachment; filename="file.csv"'  
#     stdu = StudentForm.objects.all()  
#     writer = csv.writer(response)  
#     for std in stdu:  
#         writer.writerow([stdu.eid,stdu.ename,stdu.econtact])  
#     return response 

def getpdf(request):  
    response = HttpResponse(content_type='application/pdf')  
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'  
    p = canvas.Canvas(response)  
    p.setFont("Times-Roman", 55)  
    p.drawString(100,700, "Hello, Javatpoint.")  
    p.showPage()  
    p.save()  
    return response  

# def getdata(request):  
#     # data = StudentForm.objects.get(id=12)  
#     # return HttpResponse(data)  #It shows the following exception because no record is available at id 12.
#     try:  
#         data = StudentForm.objects.get(id=12)  
#     except ObjectDoesNotExist:  
#         return HttpResponse("Exception: Data not found")  
#     return HttpResponse(data);  





# def emp(request):  
#     if request.method == "POST":  
#         form = EmployeeForm(request.POST)  
#         if form.is_valid():  
#             try:  
#                 return redirect('/')  
#             except:  
#                 pass  
#     else:  
#         form = EmployeeForm()  
#     return render(request,'index.html',{'form':form})  



  
# def index(request):
#     template = loader.get_template("index.html")
#     name = {
#         "student":"hiral"
#     }
#     return HttpResponse(template.render(name))

# def index(request):
    # now = datetime.datetime.now()
    # html = "<html><body><h3>now time is  %s.</h3></body></htm>"%now
    # return HttpResponse(html)

# @require_http_methods(["GET"])  
# def hello(request):  
#     return HttpResponse('<h1>This is Http GET request.</h1>')
