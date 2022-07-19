from django.urls import path, re_path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    
    re_path(r'^Recipes/$', views.RecipeAPI),
    re_path(r'^Recipes/([0-9]+)$', views.RecipeAPI),
    
    re_path(r'^Member/$', views.MemberAPI),
    re_path(r'^Member/([0-9]+)$', views.MemberAPI),
    
    re_path(r'^SaveFile$', views.SaveFile),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)