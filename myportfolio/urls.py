from django.urls import path
# from . import views

# urlpatterns = [
#     path('index-image/', views.index, name='index'),
#     # path('success/', views.success, name='success'),
# ]
from .views import index

urlpatterns = [
    path('index-image/', index, name='index-image'),
]