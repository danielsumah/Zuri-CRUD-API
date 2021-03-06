
from django.urls import path

from .views import CreateStudentViews, ReadStudentViews, UpdateStudentViews, DeleteStudentViews, StudentDetailViews

urlpatterns = [
    # path('api', home, name = 'api-home'),
    path('api/create-student', CreateStudentViews.as_view(), name = 'api-create-student'),              #create
    path('api/read-student/<int:pk>', StudentDetailViews.as_view(), name = 'read-student'),               #read
    path('api/read-all-students', ReadStudentViews.as_view(), name = 'api-read-students'),               #read
    path('api/update-student/<int:pk>', UpdateStudentViews.as_view(), name = 'api-update-student'),     #update
    path('api/delete-student/<int:pk>', DeleteStudentViews.as_view(), name = 'api-delete-student'),     #delete
]
