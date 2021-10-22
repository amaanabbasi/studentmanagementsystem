from django.urls import path
from student_management_app.api.views import MarkListApi, MarkListCreateApi, MarkListDeleteApi, MarkListDownloadAPI, MarkListUpdateApi, StudentCreateApi, StudentApi, StudentUpdateApi, StudentDeleteApi
urlpatterns = [
    path('student/list/',StudentApi.as_view()),
    path('student/create/',StudentCreateApi.as_view()),
    path('student/update/<int:pk>/',StudentUpdateApi.as_view()),
    path('student/<int:pk>/delete/',StudentDeleteApi.as_view()),

    path('marklist/list/',MarkListApi.as_view()),
    path('marklist/create/',MarkListCreateApi.as_view()),
    path('marklist/update/<int:pk>/',MarkListUpdateApi.as_view()),
    path('marklist/<int:pk>/delete/',MarkListDeleteApi.as_view()),

    path('download/marklist/<str:year>/<str:course_name>/', MarkListDownloadAPI.as_view())
]