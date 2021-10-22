
# Student API

GET /api/v1/student/list -> Get list of students 

POST /api/v1/student/create -> Create students

UPDATE /api/v1/student/update/<int:pk> -> Update Student

DELETE /api/v1/student/<int:pk>/delete/ -> Delete Student


# Marklist API

GET /api/v1/marklist/list -> Get marklist

POST /api/v1/marklist/create -> Create marklists

UPDATE /api/v1/marklist/update/<int:pk> -> Update marklist

DELETE /api/v1/marklist/<int:pk>/delete/ -> Delete marklist


# Download Marklist API (based on year, course_name)

GET /api/v1/download/marklist/<str:year>/<str:course_name>/
