from django.urls import path
from payoffs import views
urlpatterns = [
    path('', views.show, name='index'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]