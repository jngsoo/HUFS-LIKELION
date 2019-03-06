from django.contrib import admin
from django.urls import path, include
import blog.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('<int:blog_id>', blog.views.detail, name="detail"),
    path('new/', blog.views.new, name="new"),
    path('create', blog.views.create, name="create"),
    path('index', blog.views.index, name="index"),
]