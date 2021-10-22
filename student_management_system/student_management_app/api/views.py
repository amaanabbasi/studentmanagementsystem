from rest_framework import generics
from rest_framework.response import Response
from student_management_app.api.serializers import MarkListSerializer, StudentSerializer
from student_management_app.models import MarkList, Student


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