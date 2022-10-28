from rest_framework import serializers
from EmployeeApp.models import Department,Employee


# create serializer for each model
# serializers allow complex data such as querysets and model instances
# to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields=('DepartmentId','DepartmentName')



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee 
        fields=('EmployeeId','EmployeeName','Department','DateOfJoining','PhotoFileName')
