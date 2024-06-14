from django.urls import path


from .views import table_view

app_name = 'warehouse_app'

urlpatterns = [
    path('', table_view, name='main')
]