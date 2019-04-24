"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
#from django.urls import path,include
from django.conf.urls import include,url
app_name='learning_logs'
urlpatterns = [
    url(r'^admin/', admin.site.urls),#这是修改后的
	#url(r'^admin/',include(admin.site.urls)),#这个是书中原来的程序
	#url(r'^users/','users.urls','users'),
    url(r'^users/',include(('users.urls','users'),namespace = 'users')),
	url(r'',include(('learning_logs.urls','learning_logs'),namespace = 'learning_logs')),#这是修改后的

	#url(r'', include('learning_logs.urls', namespace='learning_logs')),#这是书中原来的

	#path(' ', include('learning_logs.urls', namespace=app_name)),

]
