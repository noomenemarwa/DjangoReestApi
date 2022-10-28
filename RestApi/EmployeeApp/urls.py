from django.urls import re_path
from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

        #urls for CRUD Department
        re_path(r'^department$',views.get_department_api),
        re_path(r'^createdepartment$',views.create_department_api),
        re_path(r'^updatedepartment$',views.update_department_api),
        re_path(r'^deletedepartment/([0-9]+)$',views.delete_department_api),
        
        #urls for CRUD Employee
        re_path(r'^employee$',views.get_employee_api),
        re_path(r'^createemployee$',views.create_employee_api),
        re_path(r'^updateemployee$',views.update_employee_api),
        re_path(r'^deleteemployee/([0-9]+)$',views.delete_employee_api),

        re_path(r'^employee/savefile',views.save_files)

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)