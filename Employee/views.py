from django.shortcuts import render,redirect
from .models import Employee

#read
def index(request):
    employees = Employee.objects.all()
    return render(request,'index.html',{'employees':employees})

def index(request):
    search = request.GET.get('search')
    if search:
        employees = Employee.objects.filter(name__icontains=search)
    else:
        employees = Employee.objects.all()
    return render(request,'index.html',{'employees':employees})

# Create your views here.
def addEmployee(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        department = request.POST['department']
        salary = request.POST['salary']

        Employee.objects.create(name=name, email=email, department=department, salary=salary)
        return redirect('/')
    return render(request,'add_employee.html')

#update
def updateEmployee(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        employee.name = request.POST['name']
        employee.email = request.POST['email']
        employee.department = request.POST['department']
        employee.salary = request.POST['salary']
        employee.save()
        return redirect('/')
    return render(request,'update_employee.html',{'employee':employee})

#delete
def deleteEmployee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/')