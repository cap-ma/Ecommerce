from django.urls import path

from . import views
from .views import CategoryList,ProductListCaegoryBased
app_name = 'store'

urlpatterns = [
    path('',CategoryList.as_view()),
    path('<str:name>/', ProductListCaegoryBased.as_view()),
]