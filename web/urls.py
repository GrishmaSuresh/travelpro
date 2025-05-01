from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('home', views.home),
    path('about', views.about),
    path('destination', views.destiny),
    path('services', views.services),
    path('gallery', views.gallery),
    path('blogs', views.blogs),
    path('success', views.success),
    path('packages', views.packages),
    path('post', views.post),
    path('bill', views.bill)

]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
