from django.urls import path
from student_management_app.api.views import StudentCreateApi, StudentApi, StudentUpdateApi, StudentDeleteApi
urlpatterns = [
    path('student/list/',StudentApi.as_view()),
    path('student/create/',StudentCreateApi.as_view()),
    path('student/update/<int:pk>/',StudentUpdateApi.as_view()),
    path('student/<int:pk>/delete/',StudentDeleteApi.as_view()),
]