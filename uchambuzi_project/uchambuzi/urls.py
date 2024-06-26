from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('data-collection-cleaning/', views.data_collection_view, name='data_collection_cleaning'),
    path('eda/', views.eda_view, name='eda-view'),
    path('clean-data/<str:filename>/', views.clean_data_view, name='clean-data'),  # Update URL pattern
    path('get_columns/', views.get_columns, name='get-columns'),

    # Add URLs for other views
]
