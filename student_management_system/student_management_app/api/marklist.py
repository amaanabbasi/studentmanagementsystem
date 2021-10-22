    path('marklist/list/',StudentApi.as_view()),
    path('marklist/create/',StudentCreateApi.as_view()),
    path('marklist/update/<int:pk>/',StudentUpdateApi.as_view()),
    path('marklist/<int:pk>/delete/',StudentDeleteApi.as_view()),