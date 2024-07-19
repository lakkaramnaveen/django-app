from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.DetailsTable.as_view()),
    path('update/<int:pk>',views.DetailsUpdate.as_view()),
    path('delete/<int:pk>',views.DetailsDelete.as_view()),

]
