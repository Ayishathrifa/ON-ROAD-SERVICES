from django.http import HttpResponse
from django.shortcuts import render, redirect
from onroadservice.models import *

# Create your views here.
def loginn(request):
    return render(request,"index.html")

def loginn_post(request):
    un=request.POST['textfield']
    pw=request.POST['textfield2']
    res=login.objects.filter(username=un,password=pw)
    if res.exists():
        if res[0].usertype == 'admin':
            request.session['lg'] = 'lin'
            return redirect('/homepage')
        elif res[0].usertype == 'worker':
            request.session['lg'] = 'lin'
            request.session['lid']=res[0].id
            request.session['lg']='lin'
            return redirect('/workerhomepage')
        elif res[0].usertype == 'user':
            request.session['lg'] = 'lin'
            request.session['lid']=res[0].id
            return redirect('/userhomepage')
        else:
            return HttpResponse("not found")
    else:
        return HttpResponse("invalid username or password")


def homepage(request):
    if request.session['lg']!='lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    return render(request,"admin/admin_homepage1.html")

def addservice(request):
    if request.session['lg']!='lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')


    return render(request,"admin/add_service.html")
def addservice_post(request):
    if request.session['lg']!='lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')


    servicename=request.POST['textfield']
    print(servicename)
    a=service()
    a.service_name=servicename
    a.save()
    return HttpResponse('<script>alert("Service added successully");window.location="/homepage"</script>')



def viewservice(request):
    if request.session['lg']!='lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')


    res=service.objects.all()
    return render(request,"admin/view_service.html",{'data':res})




def viewworker(request):
    if request.session['lg']!='lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')


    res=worker.objects.filter(LOGIN__usertype='pending')
    return render(request,"admin/view_worker.html",{'data':res})



def viewuser(request):
    if request.session['lg']!='lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')


    res=user.objects.all()
    return render(request,"admin/view_user.html",{'data':res})


def changepw(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    return render(request, "admin/Change_password.html")

def changepw_post(request):
    if request.session['lg']!='lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')


    currentpw=request.POST['textfield']
    newpw=request.POST['textfield2']
    confirmpw=request.POST['textfield3']
    print(currentpw, newpw, confirmpw)
    res = login.objects.filter( password=currentpw)
    if res.exists():
        if newpw==confirmpw:
            login.objects.filter(usertype='admin').update(password=confirmpw)
            return HttpResponse('<script>alert("Success");window.location="/"</script>')
        else:
            return HttpResponse('<script>alert("invalid");window.location="/changepw"</script>')


def register_worker(request):
    return render(request,"worker/worker_reg1.html")


def register_worker_post(request):
    name=request.POST['textfield']
    available=request.POST['textfield2']
    longi=request.POST['textfield3']
    lati=request.POST['textfield4']
    phone=request.POST['textfield5']
    mail=request.POST['textfield6']
    pw=request.POST['textfield7']

    if login.objects.filter(username=mail).exists():
        return HttpResponse('<script>alert("Email already registered");window.location="/register_worker"</script>')
    print(name,available,longi,lati,phone,mail,pw)

    obj=login()
    obj.username=mail
    obj.password=pw
    obj.usertype='pending'
    obj.save()



    b=worker()
    b.worker_name=name
    b.availability=available
    b.latitude=longi
    b.longitude=lati
    b.phone_no=phone
    b.LOGIN=obj
    b.save()

    return HttpResponse('<script>alert("Registered");window.location="/"</script>')

def worker_view_service(request):
    if request.session['lg']!='lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    g = own_service.objects.filter(WORKER__LOGIN=request.session['lid'])
    a = []
    for i in g:
        a.append(i.id)
    res = service.objects.all().exclude(id__in=a)
    return render(request, "worker/worker_service_view.html", {'data': res})

def addtoown(request,id):
    if request.session['lg']!='lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')


    lid=worker.objects.get(LOGIN=request.session['lid'])
    obj=own_service()
    obj.SERVICE_id=id
    obj.WORKER_id=lid.id
    obj.save()

    return HttpResponse('<script>alert("Added to own service");window.location="/view_ownservice"</script>')

def view_ownservice(request):
    if request.session['lg']!='lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')


    res=own_service.objects.all()
    return render(request,"worker/own_service_view.html", {'data': res})

def delete_ownsevice(request,sid):
    if request.session['lg']!='lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')


    own_service.objects.filter(id=sid).delete()
    return HttpResponse('<script>alert("deleted");window.location="/view_ownservice"</script>')

def workerhomepage(request):
    if request.session['lg']!='lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')


    return render(request,"worker/worker_homepage1.html")

def accept_worker(request,id):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    login.objects.filter(id=id).update(usertype = 'worker')
    return HttpResponse('<script>alert("Accepted");window.location="/verifiedworker"</script>')

def verifiedworker(request):
    if request.session['lg']!='lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')


    res = worker.objects.filter(LOGIN__usertype='worker')
    return render(request,"admin/verified_worker_view.html",{'data':res})

def ratingsreview(request):
    if request.session['lg']!='lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    print(request.session['lid'])
    # res=rating_reviews.objects.filter(WORKER__LOGIN_id=request.session['lid'])
    res=rating_reviews.objects.filter(WORKER=worker.objects.get(LOGIN=request.session['lid']))
    print(res)
    return render(request,"worker/view_ratingreview.html",{'data':res})

def registration_user(request):


    return render(request, "user/user_reg1.html")

def registration_user_post(request):



    uname=request.POST['textfield']
    mail=request.POST['textfield2']
    cont_no=request.POST['textfield3']
    pw=request.POST['textfield4']
    cpw=request.POST['textfield5']
    obj = login.objects.filter(username=mail)
    print(uname,mail,cont_no,pw,cpw)
    if obj.exists():
        return HttpResponse('<script>alert("Email already exists");window.location="/registration_user"</script>')
    else:
        if pw == cpw:
            obj=login()
            obj.username=mail
            obj.password=pw
            obj.usertype='user'
            obj.save()

            c= user()
            c.user_name=uname
            c.email=mail
            c.contact_no=cont_no
            c.LOGIN=obj
            c.save()
            return HttpResponse('<script>alert("Register successfull");window.location="/"</script>')
        else:
            return HttpResponse('<script>alert("Password and confirm password not matching");window.location="/registration_user"</script>')

def userhomepage(request):
    if request.session['lg']!='lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')


    return render(request,"user/user_home1.html")

def viewservices(request):
    if request.session['lg']!='lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')


    res = service.objects.all()
    return render(request, "user/user_view_service.html", {'data': res})

def user_view_workers(request,sid):
    if request.session['lg']!='lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')


    res = own_service.objects.filter(SERVICE=sid)
    return render(request,"user/user_req_worker.html",{'data':res})

def long_lat(request,id):
    if request.session['lg']!='lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')


    return render(request,"user/Lat_Long_req.html",{'id':id})
def long_lat_post(request,id):
    if request.session['lg']!='lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')


    lat=request.POST['textfield']
    long=request.POST['textfield2']
    date=request.POST['textfield3']
    lid=login.objects.get(id=request.session['lid'])
    print(lid)

    import datetime
    t=datetime.datetime.now().strftime("%H:%M:%S")


    obj=request_service()
    obj.latitude=lat
    obj.longitude=long
    obj.Date=date
    obj.status='pending'
    obj.OWN_SERVICE_id=id

    obj.time=t
    obj.save()
    return HttpResponse('<script>alert("Request send successfully");window.location="/viewservices"</script>')

def view_user_request(request):
    if request.session['lg']!='lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')


    lid = request_service.objects.filter(OWN_SERVICE__WORKER__LOGIN_id=request.session['lid'],status='pending')
    return render(request, "worker/User_request_view.html",{'data': lid})

def accept_request(request,id):
    if request.session['lg']!='lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')


    lid = request_service.objects.filter(id=id).update(status='approved')
    lid = request_service.objects.filter(OWN_SERVICE__WORKER__LOGIN_id=request.session['lid'], status='approved')
    return HttpResponse('<script>alert("Accepted");window.location="/view_user_request"</script>')

def reject_request(request,id):
    if request.session['lg']!='lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')


    lid = request_service.objects.filter(id=id).update(status='approved')
    return HttpResponse('<script>alert("Rejected");window.location="/view_user_request"</script>')

def user_view_request_status(request):
    if request.session['lg']!='lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')


    lid = request_service.objects.filter(USER__LOGIN_id=request.session['lid'])
    print(lid)
    print(request.session['lid'])

    return render(request, "user/user_view_status.html",{'data': lid})

def rate_review(request,id):
    if request.session['lg']!='lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')


    return render(request, "user/rate&review.html",{'id':id})
def rate_review_post(request):
    if request.session['lg']!='lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')


    rat=request.POST['textfield']
    revw=request.POST['textfield2']


    obj =rating_reviews()
    obj.Ratings=rat
    obj.Reviews=revw
    obj.save()

    return HttpResponse('<script>alert("Ratings send successfully");window.location="/user_view_request_status"</script>')

def user_view_ratings(request,id):
    if request.session['lg']!='lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')


    res = rating_reviews.objects.filter(WORKER=id)
    print(res)
    return render(request,"user/user_view_ratings.html",{'data':res})

def delete_service(request,id):
    if request.session['lg']!='lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')


    service.objects.filter(id=id).delete()
    return HttpResponse('<script>alert("deleted");window.location="/viewservice"</script>')

def logout(request):
    request.session['lg']=""
    return redirect('/')


