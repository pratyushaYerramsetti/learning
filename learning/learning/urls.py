"""learning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from courses import views as v
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
    
# from django.contrib.auth import logout    
admin.site.site_header = "Learning Admin"
admin.site.site_title  ==  "Learning Admin Portal"
admin.site.index_title  ==  "Welcome page admin"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('base/', TemplateView.as_view(template_name='base.html'), name='base'),
    path('logged_out/', TemplateView.as_view(template_name='logged_out.html'), name='logged_out'),
    # path('cse/', TemplateView.as_view(template_name='cse.html'), name='cse'),
    path('ece/', TemplateView.as_view(template_name='ece.html'), name='ece'),
    path('eee/', TemplateView.as_view(template_name='eee.html'), name='eee'),
    path('civil/', TemplateView.as_view(template_name='civil.html'), name='civil'),
    path('mech/', TemplateView.as_view(template_name='mech.html'), name='mech'),
    path('it/', TemplateView.as_view(template_name='it.html'), name='it'),

    path('',TemplateView.as_view(template_name = 'start.html'),name = 'start'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/',v.signup,name = 'signup'),
    # path('hello/',v.books_list,name='books_list')
    # path('cse/',v.books_list,name='cse')
    
    path('cse/',v.books_list,name='cse')
    
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

