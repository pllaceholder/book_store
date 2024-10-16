"""
URL configuration for book_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from book_shelf import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('books_list_template_view/', views.BooksListTemplateView.as_view(), name='books_list_template_view'),
    path('books_list/', views.BooksList.as_view(), name='books_list'),
    path('books/<int:pk>/', views.BooksDetail.as_view(), name='book_detail'),
    path('books/<int:pk>/update/', views.BooksUpdate.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', views.BooksDelete.as_view(), name='book_delete'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
