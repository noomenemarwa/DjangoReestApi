
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from EmployeeApp.models import Department,Employee
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer
from django.core.files.storage import default_storage

# Create your views here.

# ****************************Crud for Department*********************

# Csrf exempt is a cool feature of django which allows by passing of csrf verification by django.
@csrf_exempt
# Get Departments
def get_department_api(request,id=0):
    # Get request
    if request.method=='GET':
        # get all departments
        departments = Department.objects.all()
        # serialized the queryset (convert to serializer)
        departments_serializer=DepartmentSerializer(departments,many=True)
        # return the data
        return JsonResponse(departments_serializer.data,safe=False)
    
    
@csrf_exempt 
# Create Departments
def create_department_api(request):  
    if request.method=='POST':
        # convert the request to save in the model 
        department_data=JSONParser().parse(request)
        departments_serializer=DepartmentSerializer(data=department_data)
        # if valide data save in department model
        if departments_serializer.is_valid():
            departments_serializer.save()
            # return success message
            return JsonResponse("Added Successfully",safe=False)
            # return error message
        return JsonResponse("Failed to Add",safe=False)

@csrf_exempt
# Update Department 
def update_department_api(request):     
    if request.method=='PUT':
        department_data=JSONParser().parse(request)
        # get department object with id 
        department=Department.objects.get(DepartmentId=department_data['DepartmentId'])
        departments_serializer=DepartmentSerializer(department,data=department_data)
        #  if data valid save the updated value 
        if departments_serializer.is_valid():
            departments_serializer.save()
            # return success response
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")

@csrf_exempt
# Delete Department    
def delete_department_api(request,id):    
    # Delete request    
    if request.method=='DELETE':
        # get dapartment with id 
        department=Department.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully",safe=False)




# ****************************Crud for Employee*********************



@csrf_exempt
# Get Employees
def get_employee_api(request,id=0):
    # Get request
    if request.method=='GET':
        # get all Employees
        Employees = Employee.objects.all()
        # serialized the queryset (convert to serializer)
        Employees_serializer=EmployeeSerializer(Employees,many=True)
        # return the data
        return JsonResponse(Employees_serializer.data,safe=False)

@csrf_exempt 
# Create Employees
def create_employee_api(request):  
    if request.method=='POST':
        # convert the request to save in the model 
        emplyee_data=JSONParser().parse(request)
        emplyees_serializer=EmployeeSerializer(data=emplyee_data)
        # if valide data save in Employee model
        if emplyees_serializer.is_valid():
            emplyees_serializer.save()
            # return success message
            return JsonResponse("Added Successfully",safe=False)
            # return error message
        return JsonResponse("Failed to Add",safe=False)


@csrf_exempt
# Update Employees
def update_employee_api(request):     
    if request.method=='PUT':
        employee_data=JSONParser().parse(request)
        # get department object with id 
        employee=Employee.objects.get(EmployeeId=employee_data['EmployeeId'])
        employees_serializer=EmployeeSerializer(employee,data=employee_data)
        #  if data valid save the updated value 
        if employees_serializer.is_valid():
            employees_serializer.save()
            # return success response
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")


@csrf_exempt
# Delete Employees   
def delete_employee_api(request,id):    
    # Delete request    
    if request.method=='DELETE':
        # get employee with id 
        employee=Employee.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt
# Save Files
def save_files(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name, safe =False)