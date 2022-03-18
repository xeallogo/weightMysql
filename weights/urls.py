from django.conf.urls import url 
from weights import views 
 
urlpatterns = [ 
    url(r'^api/weights$', views.weight_list),
    url(r'^api/weights/(?P<pk>[0-9]+)$', views.weight_detail)
]