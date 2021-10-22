from rest_framework import generics
from rest_framework.response import Response
from student_management_app.api.serializers import MarkListSerializer, StudentSerializer
from student_management_app.models import MarkList, Student
from rest_framework.views import APIView
import csv
from django.http import HttpResponse

class StudentCreateApi(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentApi(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDeleteApi(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class MarkListCreateApi(generics.CreateAPIView):
    queryset = MarkList.objects.all()
    serializer_class = MarkListSerializer


class MarkListApi(generics.ListAPIView):
    queryset = MarkList.objects.all()
    serializer_class = MarkListSerializer


class MarkListUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = MarkList.objects.all()
    serializer_class = MarkListSerializer

class MarkListDeleteApi(generics.DestroyAPIView):
    queryset = MarkList.objects.all()
    serializer_class = MarkListSerializer



class MarkListDownloadAPI(APIView):
    def get(self, request, year, course_name, format=None):
        
        # This response object will be used to store the csv file or the attachment file.
        response = HttpResponse(content_type='text/csv')
        # csv writer object creation
        writer = csv.writer(response)
        # writing the header of the csv file
        writer.writerow(['student_uid', 'student_name', 'marks_scored_percentage', 'course_name', 'year'])
        # filtering marklist based on the year and coursename.
        filtered_mark_list = MarkList.objects.filter(year=year, course_name=course_name).values_list('student_uid', 'student_name', 'marks_scored_percentage', 'course_name', 'year')
        for student_marks in filtered_mark_list:
            writer.writerow(student_marks)
        # Giving the file a name export.csv    
        response['Content-Disposition'] = 'attachment; filename="export.csv"'
        return response
