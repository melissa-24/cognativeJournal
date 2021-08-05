from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('access/', views.access),
    path('register/', views.register),
    path('signin/', views.signin),
    path('logout/', views.logout),
    path('dashboard/', views.dashboard),
    path('dashboard/updateProfile/', views.updateProfile),
    path('dashboard/category/', views.category),
    path('dashboard/createCategory/', views.createCategory),
    path('dashboard/editCategory/', views.editCategory),
    path('dashboard/updateCategory/', views.updateCategory),
    path('dashboard/addPost/', views.addPost),
    path('dashboard/createPost/', views.createPost),
    path('dashboard/editPost', views.editPost),
    path('dashboard/updatePost', views.updatePost),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)