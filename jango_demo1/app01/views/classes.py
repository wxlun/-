from django.shortcuts import render,redirect
from app01 import models

def get_classes(request):
    cls_list=models.Classes.objects.all()
    return render(request,'get_classes.html',{'cls_list':cls_list})


def add_classes(request):
    if request.method == "GET":
        return render(request,'add_classes.html')
    elif request.method == "POST":
        title = request.POST.get('title')
        models.Classes.objects.create(titile=title)
        return redirect('/classes.html')

def del_classes(request):
    nid=request.GET.get('nid')
    models.Classes.objects.filter(id=nid).delete()
    return redirect('/classes.html')


def edit_classes(request):
    if request.method=='GET':
        nid=request.GET.get('nid')
        obj=models.Classes.objects.filter(id=nid).first()
        return render(request,'edit_classes.html',{'obj':obj})
    elif request.method=='POST':
        nid=request.GET.get('nid')
        title=request.POST.get('xxoo')
        models.Classes.objects.filter(id=nid).update(titile=title)
        return redirect('/classes.html')

def set_teacher(request):
    if request.method=='GET':
        nid=request.GET.get('nid')
        cls_obj=models.Classes.objects.filter(id=nid).first()
        cls_teacher_list=cls_obj.m.all().values_list("id","name")
        print(cls_teacher_list)
        print(list(zip(*cls_teacher_list)))
        id_list=list(zip(*cls_teacher_list))[0] if list(zip(*cls_teacher_list)) else []
        all_teacher_list=models.Teachers.objects.all()
        return render(request,
                'set_teacher.html',
                {
                    'id_list':id_list,
                    'all_teacher_list':all_teacher_list,
                    'nid':nid
                }
                )
    elif request.method=='POST':
        nid=request.GET.get('nid')
        ids=request.POST.getlist('teacher_ids')
        obj=models.Classes.objects.filter(id=nid).first()
        obj.m.set(ids)
        return redirect('/classes.html')


