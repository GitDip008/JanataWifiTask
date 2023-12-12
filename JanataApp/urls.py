from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('get_data/', views.get_data, name='get_data'),  # Endpoint to fetch data
#     path('update_data/<int:pk>/', views.update_data, name='update_data'),  # Endpoint to update data
#     path('delete_data/<int:pk>/', views.delete_data, name='delete_data'),  # Endpoint to delete data
# ]

urlpatterns = [
    path('', views.index, name='index'),

]

