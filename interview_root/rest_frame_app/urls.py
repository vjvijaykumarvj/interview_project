from django.urls import path,include
from rest_framework import  routers
from.import views
from django.conf import settings
from django.conf.urls.static import static


router = routers.SimpleRouter()
router.register('employee',views.Employee_crud,basename='employee')

urlpatterns=[
    path('',include(router.urls))
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
