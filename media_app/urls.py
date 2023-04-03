from django.urls import path
from . import views


urlpatterns = [
   path('', views.Homepage.as_view(), name='homepage'),
   path('upload-new-file/', views.AddImagesView.as_view(), name='add_new_img'),
   path('update-img/<int:id>/', views.UpdateImage.as_view(), name='update_img'),
   
]

