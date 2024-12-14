from django.urls import path
from inscriptions import views

urlpatterns = [
    path('inscriptions/',views.get_inscriptions),
    path('inscriptions/<int:pk>',views.get_inscription),
    path('mediums/',views.get_mediums),
    path('mediums/<int:pk>',views.get_medium),
    path('writingscripts/',views.get_writingscripts),
    path('writingscripts/<int:pk>',views.get_writingscript),
    path('photos/',views.get_photos),
    path('photos/<int:pk>',views.get_photo),
    path('photos/view/<int:pk>',views.get_view_photo)
]