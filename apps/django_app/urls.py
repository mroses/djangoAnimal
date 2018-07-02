from django.conf.urls import url
import views
#/=>blogs_app is the root url for this app
urlpatterns = [
    #/blogs_app/ is actually what the below url is looking for since the root app is /blogs_app/...even though the url pattern says empty with r'^$'..^ signifies start or url and $ signifies the end of url
    url(r'^$', views.index),
    #localhost:8000/blogs_app/show_form
    url(r'^show_form', views.index),
]
