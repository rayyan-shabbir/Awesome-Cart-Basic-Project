"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from . import views

# Code till Video 6

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name="index"),    # 1st arg: endpoint which we write in url after IP & port, 2nd arg: function in views which we want to display, 3rd arg: name of this page or this url which we can acces (using this name) across anywhere in our website package. 
#     path('about/', views.about, name="about"),
#     path('file', views.myviewfile, name="file"),
#     path('facebook/', views.facebook, name="facebook"),
#     path('cwhDjango/', views.cwhDjango, name="cwhDjango")
# ]


# Code for Video 7 (Laying the pipeline)
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name="index"),
#     path('removepunc/', views.removepunc, name='removepunc'),
#     path('capitalizefirst/', views.capfirst, name='capfirst'),
#     path('newlineremove/', views.newlineremove, name='newlineremove'),
#     path('spaceremove/', views.spaceremove, name='spaceremove'),
#     path('charcount/', views.charcount, name='charcount')
# ]

# Templates
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name="index"),
#     path('morerender/', views.moreRender, name= "moreRender")
# ]

# Text Utils Home Page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('analyze/', views.analyze, name='analyze'),
]
