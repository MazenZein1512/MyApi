from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
#    path('add/', views.addItem),
    path('upload', views.UploadFileView.as_view(), name='upload-file'),
]
