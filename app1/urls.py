from app1 import views
from django.conf.urls import url
#app ki new url file banane tym likhna h
app_name ='app1'

urlpatterns = [
    # about is calling the views.about function
    url(r'^home/$',views.register,name="home"),

]