from django.urls import path
from .views import asosiy_menyu, news, detail


urlpatterns = [
    path('home', asosiy_menyu, name='asosiy'),
    path('news/', news, name= 'news'),
    path('detail/<int:id>/', detail, name='detail')

]