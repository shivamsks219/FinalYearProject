# from fileinput import filename
from tempfile import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from sentiApp import logic
# from sentiApp import upload
import os

# from logic import check



def home(request):
    myform(request)
    return render(request, 'firstpage.html')

def myform(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        comment = request.POST.get("comment")
        # filename = request.POST.get("filename")
        res=logic.check(comment)
        # if len(request.FILES) != 0:
        #     filename= request.FILES['image']
        # file_in_memory # <InMemoryUploadedFile: xxx (xxx/xxx)>
        # filename = file_in_memory.file
        #filename = request.FILES["image"].read()
        #file = request.files['image']
        

        # print(filename)
        # fi = form['filename']
        # if fi.filename:
            
        #print(upload.send(fname, comment, file))
        #fp = open(filename, 'r')
        # print(filename)
        #filename = request.POST.get("image")
        #imgres=logic.checkimg(fp)

        data={
            'Firstname':fname,
            'Lastname':lname,
            'Comments':comment,
            'Fullname':fname+" "+lname,
            'Sentiment':res,
         #   'imgSentiment':imgres
        }

        return render(request, "form.html",data)
    return render(request, "form.html")

def function(request):
    #return HttpResponse("First Web App Using Django")
    #for returning the html response without html file
    return render(request, "form.html")
    template = loader.get_template('firstpage.html')
    return HttpResponse(template.render())


# Create your views here.
