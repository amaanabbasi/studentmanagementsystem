from rest_framework import  serializers
from student_management_app.models import MarkList, Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class MarkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarkList
        fields = '__all__'
