from urllib import request
from django.shortcuts import render
from django.shortcuts import redirect
from django.db import connection
from .forms import *
from django.http import HttpResponse
from django.views.static import serve
import os

k = 0

def home(request):
    global k
    k=0
    return render(request,'flights/index.html')

def login(request):
    return render(request,'flights/proceed.html')

def select(request):
    return render(request,'flights/techstu.html')

def select1(request):
    return render(request,'flights/techstu2.html')

def home1(request,name):
    context = {"name":name}
    return render(request,'flights/index1.html',context)

def notes(request,name):
    context = {"name":name}
    return render(request,'flights/notes.html',context)

def popular(request,name):
    context = {"name":name}
    return render(request,'flights/index1.html',context)

def thisweek(request,name):
    context = {"name":name}
    return render(request,'flights/index1.html',context)

def live(request,name,sub):
    context = {"name":name,"sub":sub}
    cursor = connection.cursor()
    sql = "Select * from Course_Details where  course = '"+sub+"'"
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        context["data"] = data

    except:
        pass
    return render(request,'flights/live.html',context)

def forum(request,name):
    context = {"name":name}
    return render(request,'flights/forum.html',context)

def upcoming(request,name,sub):
    context = {"name": name}
    cursor = connection.cursor()
    sql = "Select * from Course_Details where  course = '" + sub + "'"
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        context["data"] = data

    except:
        pass
    return render(request, 'flights/upcoming.html', context)

def profile(request,foo):
    context = {"name": foo}
    global k
    if k == 0:
        cursor = connection.cursor()
        sql = "Select * from Student where user_name=" + foo
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            context["data"] = data
        except:
            pass
        return render(request, 'flights/profile.html', context)
    else:
        cursor = connection.cursor()
        sql = "Select * from Student where teacher_name=" + foo
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            context["data"] = data
        except:
            pass
        return render(request, 'flights/profile.html', context)

def subscribe(request):
        import smtplib
        from email.mime.text import MIMEText

        smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
        smtp_ssl_port = 465
        username = 'brothersjunction@gmail.com'
        password = 'brothers123'
        sender = 'brothersjunction@gmail.com'
        targets = ['lancedsilva2000@gmail.com', 'codestacks123@gmail.com']

        msg = MIMEText('Hi, how are you today?')
        msg['Subject'] = 'Hello'
        msg['From'] = sender
        msg['To'] = ', '.join(targets)

        server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
        server.login(username, password)
        server.sendmail(sender, targets, msg.as_string())
        server.quit()   
        return render(request, 'flights/index.html')


def userlogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            email = form.cleaned_data['Email']
            password = form.cleaned_data['Password']
            cursor = connection.cursor()
            sql = "Select * from Student where email = '"+email+"' and pass = '"+password+"'"
            cursor.execute(sql)
            data = cursor.fetchall()
            if not data :
                return redirect("http://127.0.0.1:8000/userlogin")
            else:
                string = "http://127.0.0.1:8000/home/"+data[0][0]
                return redirect(string)
    return render(request, 'flights/login.html', )

def teacherlogin(request):
    global k
    k=1
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            email = form.cleaned_data['Email']
            password = form.cleaned_data['Password']
            cursor = connection.cursor()
            sql = "Select * from Teacher where email = '" + email + "' and pass = '" + password + "'"
            cursor.execute(sql)
            data = cursor.fetchall()
            if not data:
                return redirect("http://127.0.0.1:8000/teacherlogin")
            else:
                string = "http://127.0.0.1:8000/home/" + data[0][0]
                return redirect(string)
    return render(request, 'flights/login1.html', )


# full_name    | varchar(50) | YES  |     | NULL    |       |
# | course       | varchar(50) | YES  |     | NULL    |       |
# | info         | varchar(30) | YES  |     | NULL    |       |
# | c_date       | date        | YES  |     | NULL    |       |
# | youtube_link | varchar(30) | YES  |     | NULL



def usersignin(request):
    if request.method == 'POST':
        form = studentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            cursor = connection.cursor()
            sql = "insert into Student values('"+name+"','"+email+"','"+password+"')"
            cursor.execute(sql)
            return redirect("http://127.0.0.1:8000/login")
    return render(request, 'flights/signup.html', )


def teachersignin(request):
    if request.method == 'POST':
        form = teacherForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            education = form.cleaned_data['education']
            job = form.cleaned_data['job']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            cursor = connection.cursor()
            sql = "insert into Teacher values('" + name + "',"+age+",'" + education + "','" +job+"','"+email+"','"+ password + "')"
            cursor.execute(sql)
            return redirect("http://127.0.0.1:8000/login")
    return render(request, 'flights/signup1.html', )

def course(request,foo):
    if k==0:
        return render(request, 'flights/accessdenied.html')
    context = {"name": foo}
    if request.method == 'POST':
        form = courseForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['name']
            course = form.cleaned_data['course']
            info = form.cleaned_data['info']
            date = form.cleaned_data['date']
            link = form.cleaned_data['link']
            link = link.split("/")
            cursor = connection.cursor()
            sql = "insert into Course_Details values('" + name + "','" + course + "','" +info+"','"+date +"','"+ link[-1] + "')"
            cursor.execute(sql)
            string = "http://127.0.0.1:8000/home/" + foo
            return redirect(string)
    return render(request, 'flights/data.html', context)


def download(request):
    filepath = 'templates/flights/new.pdf'
    with open('C:/Users/acer/OneDrive/Desktop/miniproject/templates/flights/new.pdf', 'rb') as pdf:
            response = HttpResponse(pdf.read())
            response['content_type'] = 'application/pdf'
            response['Content-Disposition'] = 'attachment;filename=file.pdf'
            return response




