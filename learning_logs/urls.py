'''定义learning_logs的url模式'''

from django.conf.urls import url

from . import views

urlpatterns=[
	#主页
	url(r'^$',views.index,name = 'index'),

	#显示所有主题,我曹我竟然因为大小写，弄这么久
	url(r'^topics/$', views.topics, name='topics'),
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]

