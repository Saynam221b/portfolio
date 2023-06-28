from django.contrib import admin
from django.urls import path
from portfolioapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(' ', views.index, name= 'index'),
    path('projects', views.projects, name= 'projects'),
    path('experience', views.experience, name= 'experience'),
    path('contact', views.contact, name= 'contact'),
    path('contact_success', views.contact_me, name= 'contact'),
    


]