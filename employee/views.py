from django.shortcuts import render, redirect
from employee.forms import EmployeeForm
from employee.models import Employee,MarkForeign
from django.db import connection

def my_custom_sql(sql):
    cursor = connection.cursor()    
    cursor.execute(sql)
    row = cursor.fetchall()
    return row

# Create your views here.
def emp(request):
    if request.method == "POST":
        print("test")
        form = EmployeeForm(request.POST)
        print(form)
        if form.is_valid():
            try:
                form.save()
                return redirect('/employee/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request,'index.html',{'form':form})

def show(request):
    employees = Employee.objects.all()
    return render(request,"show.html",{'employees':employees})
def test_sample(request):
    result=my_custom_sql("select Name,Mark,SubjectName from Mark m join Subject s on m.Subid=s.Subid join  Student st on st.studid=m.studid;")
    print("result start for RAW Query")
    print(result)
    print("result end for RAW Query")
    print("result start for ORM")
    print(MarkForeign.objects.values('Studid__Name','Subid__SubjectName','Mark'))
    print("result end for ORM")
    
    return redirect('/employee/show')
    
def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request,'edit.html', {'employee':employee})
def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/employee/show")
    return render(request, 'edit.html', {'employee': employee})
def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/employee/show")