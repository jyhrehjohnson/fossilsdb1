from django.urls import path
from . import views

app_name = 'casts'
urlpatterns = [
    path('fossil/', views.FossilListView.as_view(), name='fossil_list_view'),  # casts/
    path('fossil/<int:pk>/', views.FossilDetailView.as_view(), name='fossil_detail_view')  # casts/1
]
