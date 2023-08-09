from django.contrib import admin
from django.urls import path
from portfolioapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index', views.index, name= 'index'),
    path('projects', views.projects, name= 'projects'),
    path('experience', views.experience, name= 'experience'),
    path('contact', views.contact, name= 'contact'),
    # path('EET', views.EET, name= 'EET'),
    path('contact_success', views.contact_me, name= 'contact'),
    path('upload/', views.upload_file, name='upload'), 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)