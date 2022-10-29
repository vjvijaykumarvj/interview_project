from.import views
from django.urls import path

app_name = 'user_application'
urlpatterns=[
    path('register/',views.Register),
    path('updating/<pk>',views.updating,name='updating'),
    path('deleting/<pk>',views.deleting,name='deleting'),
]