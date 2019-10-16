from django.shortcuts import render,redirect
from app01 import models


def get_students(request):
    stu_list=models.Student.objects.all()
    return render(request,'get_students.html',{'stu_list':stu_list})

def add_students(request):
    if request.method=='GET':
        cs_list=models.Classes.objects.all()
        return render(request,'add_students.html',{'cs_list':cs_list})
    elif request.method=='POST':
        u=request.POST.get("username")
        a=request.POST.get("age")
        g=request.POST.get("gender")
        c=request.POST.get("cs")
        models.Student.objects.create(
            username=u,
            age=a,
            gender=g,
            cs_id=c
        )
        return redirect('/students.html')

def del_students(request):
    nid=request.GET.get('nid')
    models.Student.objects.filter(id=nid).delete()
    return redirect('/students.html')

def edit_students(request):
    if request.method=="GET":
        nid=request.GET.get('nid')
        obj=models.Student.objects.filter(id=nid).first()
        cls_list=models.Classes.objects.values('id','titile')
        return render(request,'edit_students.html',{'obj':obj,'cls_list':cls_list})
    elif request.method=="POST":
        nid=request.GET.get("nid")
        u=request.POST.get('username')
        a=request.POST.get("age")
        g=request.POST.get("gender")
        c=request.POST.get("class_id")
        models.Student.objects.filter(id=nid).update(username=u,age=a,gender=g,cs_id=c)
        return redirect('/students.html')