from django.urls import path



from blog import views


app_name = 'blog'


urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('modify/<int:pk>/', views.modify, name='modify'),

    path('write/', views.write, name='write'),
    

]
